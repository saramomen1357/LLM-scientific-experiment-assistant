from __future__ import annotations

import json
from pathlib import Path
import pandas as pd

from ollama_client import call_ollama


def _extract_json_block(text: str) -> str:
    """Extract the first valid JSON object from text."""
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end < start:
        raise ValueError("No JSON object found in LLM response.")
    return text[start : end + 1]


def run_transfer_module(input_path: Path, model: str | None, data_dir: Path, output_dir: Path) -> None:
    """Run transfer learning analysis using a local LLM."""
    
    if model is None:
        model = "llama3"

    output_dir.mkdir(parents=True, exist_ok=True)
    out_md = output_dir / "transfer_result.md"

    task_text = input_path.read_text(encoding="utf-8")

    # Build the prompt safely (NO triple quotes)
    prompt_lines = [
        "You are an expert in transfer learning for autonomous driving.",
        "",
        "Task specification:",
        task_text,
        "",
        "Your job:",
        "Return a JSON object ONLY with keys:",
        "- \"domain_shift_description\": short paragraph",
        "- \"transfer_strategy\": list of 2–4 concrete methods",
        "- \"autonomous_driving_relevance\": 1–2 sentences",
        "",
        "STRICT RULES:",
        "- Output ONLY valid JSON",
        "- No markdown fences",
        "- No commentary",
    ]
    prompt = "\n".join(prompt_lines)

    print(f"[TRANSFER] Calling model '{model}' via Ollama...")
    raw = call_ollama(model, prompt)

    try:
        json_str = _extract_json_block(raw)
        data = json.loads(json_str)
    except Exception as e:
        print("[TRANSFER] ERROR: invalid JSON from LLM\n")
        print(raw)
        raise e

    # Convert to markdown table
    df = pd.DataFrame({
        "field": list(data.keys()),
        "value": [
            json.dumps(v, ensure_ascii=False, indent=2) if isinstance(v, (list, dict)) else str(v)
            for v in data.values()
        ]
    })

    table_md = df.to_markdown(index=False)

    # Build markdown report manually
    report = (
        "# Transfer Learning Analysis (LLM-Assisted)\n\n"
        f"**Model used:** {model}\n\n"
        "## Raw JSON Output\n\n"
        "```json\n"
        f"{json_str}\n"
        "```\n\n"
        "## Structured Summary\n\n"
        f"{table_md}\n"
    )

    out_md.write_text(report, encoding="utf-8")
    print(f"[TRANSFER] Report saved to: {out_md.resolve()}")
