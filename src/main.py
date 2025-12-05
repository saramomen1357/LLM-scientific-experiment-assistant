import argparse
from pathlib import Path

from policy_module import run_policy_module
from numerical_module import run_numerical_module
from transfer_module import run_transfer_module


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "outputs"


def main():
    parser = argparse.ArgumentParser(
        description="LLM-Driven Scientific Experiment Assistant"
    )
    parser.add_argument(
        "--mode",
        choices=["policy", "numerical", "transfer"],
        required=True,
        help="Which analysis module to run.",
    )
    parser.add_argument(
        "--model",
        default="llama3",
        help="Ollama model name (default: llama3).",
    )
    parser.add_argument(
        "--input",
        type=str,
        default=None,
        help="Optional path to CSV input file (else use default sample).",
    )

    args = parser.parse_args()

    input_path = Path(args.input) if args.input else None

    if args.mode == "policy":
        run_policy_module(input_path, args.model, DATA_DIR, OUTPUT_DIR)
    elif args.mode == "numerical":
        run_numerical_module(input_path, args.model, DATA_DIR, OUTPUT_DIR)
    elif args.mode == "transfer":
        run_transfer_module(input_path, args.model, DATA_DIR, OUTPUT_DIR)
    else:
        raise ValueError(f"Unknown mode: {args.mode}")


if __name__ == "__main__":
    main()
