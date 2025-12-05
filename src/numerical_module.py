from pathlib import Path
import json

import numpy as np
import pandas as pd

from ollama_client import call_ollama


def build_numerical_experiment() -> pd.DataFrame:
    """
    Simple ODE: y' = y, y(0) = 1, solution y(t) = exp(t).
    Compare Euler vs RK4 at different step sizes at t=1.0.
    """
    t_final = 1.0
    true_value = np.exp(t_final)
    step_sizes = [0.5, 0.25, 0.1]

    def euler(h: float) -> float:
        y = 1.0
        t = 0.0
        while t < t_final - 1e-12:
            y = y + h * y
            t += h
        return y

    def rk4(h: float) -> float:
        y = 1.0
        t = 0.0
        while t < t_final - 1e-12:
            k1 = y
            k2 = y + 0.5 * h * k1
            k3 = y + 0.5 * h * k2
            k4 = y + h * k3
            y = y + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
            t += h
        return y

    rows = []
    for h in step_sizes:
        y_euler = euler(h)
        y_rk4 = rk4(h)
        rows.append({
            "method": "euler",
            "step_size": h,
            "approx_value": y_euler,
            "abs_error": abs(y_euler - true_value),
        })
        rows.append({
            "method": "rk4",
            "step_size": h,
            "approx_value": y_rk4,
            "abs_error": abs(y_rk4 - true_value),
        })

    return pd.DataFrame(rows)


def build_numerical_prompt(table_md: str) -> str:
    return f"""
You are analyzing numerical methods for solving an ODE.

We solved y' = y, y(0) = 1, true solution y(1) = e.

Here is a table of results for different methods and step sizes:

{table_md}

Columns:
- method: Euler or RK4
- step_size: integration step size
- approx_value: numerical approximation at t=1
- abs_error: absolute error

Tasks:
1. Explain which method appears more accurate and why.
2. Describe how step size affects error for each method.
3. Comment on stability and convergence behavior in general terms.
4. Output STRICT JSON ONLY with this schema:

{{
  "best_method": "string",
  "reason": "string",
  "observations": ["string", "string"],
  "latex_bullets": ["string", "string"]
}}
"""


def run_numerical_module(input_path: Path | None, model: str, data_dir: Path, output_dir: Path) -> None:
    df = build_numerical_experiment()
    csv_path = data_dir / "numerical_sample.csv"
    data_dir.mkdir(exist_ok=True, parents=True)
    df.to_csv(csv_path, index=False)

    table_md = df.to_markdown(index=False)
    prompt = build_numerical_prompt(table_md)
    raw = call_ollama(model, prompt)

    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        print("[NUMERICAL] ERROR: invalid JSON from LLM")
        print(raw)
        return

    output_dir.mkdir(exist_ok=True, parents=True)
    report_md = output_dir / "numerical_report.md"

    lines = [
        "# Numerical Experiment Report",
        "",
        f"**Best method:** {result['best_method']}",
        "",
        f"**Reason:** {result['reason']}",
        "",
        "## Observations",
    ]
    for obs in result["observations"]:
        lines.append(f"- {obs}")
    lines.append("")
    lines.append("## LaTeX Bullets")
    lines.append("")
    lines.append("\\begin{itemize}")
    for b in result["latex_bullets"]:
        lines.append(f"  {b}")
    lines.append("\\end{itemize}")
    lines.append("")

    report_md.write_text("\n".join(lines), encoding="utf-8")
    print(f"[NUMERICAL] Done. Wrote {report_md}")
