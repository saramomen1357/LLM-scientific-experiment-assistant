from pathlib import Path
import pandas as pd

from ollama_client import call_ollama


def run_policy_module(input_path: Path, model_name: str, data_dir: Path, output_dir: Path) -> None:
    """
    LLM-assisted traffic policy analysis.

    - Builds a small synthetic policy experiment table (no external CSV needed)
    - Reads a natural-language scenario from input_path
    - Calls the local LLM via Ollama
    - Saves a Markdown report to outputs/policy_result.md
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    # 1) Synthetic "experiment" data – this replaces the CSV completely
    rows = [
        {"policy": "A_60s_cycle", "arrival_rate": 10, "congestion_level": 0.5, "avg_delay_sec": 35.0},
        {"policy": "B_45s_cycle", "arrival_rate": 10, "congestion_level": 0.4, "avg_delay_sec": 30.0},
        {"policy": "C_30s_cycle", "arrival_rate": 10, "congestion_level": 0.6, "avg_delay_sec": 42.0},
        {"policy": "A_60s_cycle", "arrival_rate": 6, "congestion_level": 0.3, "avg_delay_sec": 22.0},
        {"policy": "B_45s_cycle", "arrival_rate": 6, "congestion_level": 0.25, "avg_delay_sec": 20.0},
        {"policy": "C_30s_cycle", "arrival_rate": 6, "congestion_level": 0.35, "avg_delay_sec": 27.0},
    ]
    df = pd.DataFrame(rows)

    # (Optional) still save a CSV so the repo has "data"
    csv_path = output_dir / "policy_sample.csv"
    df.to_csv(csv_path, index=False)

    # Markdown table for the prompt + report
    table_md = df.to_markdown(index=False)

    # 2) Read the scenario description from the input file
    if input_path.is_file():
        scenario_text = input_path.read_text(encoding="utf-8").strip()
    else:
        scenario_text = "Signal timing experiment with three policies under varying arrival rates."

    # 3) Build LLM prompt (no JSON required → no parsing headaches)
    prompt = f"""
You are an expert in traffic signal control and policy evaluation for autonomous-driving
and infrastructure-based sensing.

We ran a small synthetic experiment comparing three signal policies on an urban approach.

SCENARIO DESCRIPTION (from user):
\"\"\"{scenario_text}\"\"\"

EXPERIMENT TABLE (Markdown):

{table_md}

Columns:
- policy: label of the signal control policy
- arrival_rate: approximate vehicle arrival rate (veh/min)
- congestion_level: normalized congestion indicator in [0, 1]
- avg_delay_sec: average per-vehicle delay in seconds

TASK:
1. Identify which policy performs best and under what conditions.
2. Explain in 2–3 sentences how this relates to policy evaluation for autonomous driving
   and traffic digital twins.
3. Give 3 short bullet points that could go into a research logbook.

Return a concise, well-structured answer in plain Markdown. Do NOT return JSON.
"""

    print("[POLICY] Calling model", repr(model_name), "via Ollama...")
    analysis_md = call_ollama(model_name, prompt)

    # 4) Build final Markdown report
    report = f"""# Policy Evaluation Module (LLM-Assisted)

**Model:** `{model_name}`

## Synthetic Experiment Data

{table_md}

## LLM Analysis

{analysis_md}
"""

    out_md = output_dir / "policy_result.md"
    out_md.write_text(report, encoding="utf-8")
    print(f"[POLICY] Report saved to: {out_md.resolve()}")
