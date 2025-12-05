🚀 LLM Scientific Experiment Assistant

A modular system that integrates a local LLM (Ollama) into scientific workflows for:

numerical experiments

traffic-simulation evaluations

domain-shift reasoning for autonomous-driving sensors

The LLM is used as a structured reasoning engine inside Python pipelines.

🧠 1. System Overview

This project demonstrates how an LLM can be integrated into computational tasks like:

stability & accuracy evaluation of numerical solvers

traffic policy analysis

transfer learning interpretation

🔄 Workflow
Input (.txt / .csv)
      ↓
Prompt Builder
      ↓
Ollama (local LLM)
      ↓
JSON Parsing + Validation
      ↓
Module Logic (Numerical / Policy / Transfer)
      ↓
Markdown Output (.md)


All modules are independent.

📂 2. Repository Structure
llm-scientific-experiment-assistant/
│
├── data/
│   ├── numerical_input.txt
│   ├── numerical_sample.csv
│   ├── policy_input.txt
│   ├── policy_sample.csv
│   ├── transfer_input.txt
│
├── outputs/
│   ├── numerical_result.md
│   ├── policy_result.md
│   ├── transfer_result.md
│   ├── numerical_output_raw.txt
│
├── src/
│   ├── main.py
│   ├── ollama_client.py
│   ├── numerical_module.py
│   ├── policy_module.py
│   ├── transfer_module.py
│
└── README.md

⚙️ 3. Installation
1️⃣ Install Ollama

Download:
https://ollama.com/download

Pull a model:

ollama pull llama3

2️⃣ Create a virtual environment
python -m venv .venv


Activate (PowerShell):

. .venv/Scripts/activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ 4. Running the Modules
A. Transfer Learning Analysis
python src/main.py --mode transfer --input data/transfer_input.txt


Output → outputs/transfer_result.md

B. Numerical Method Analysis
python src/main.py --mode numerical --input data/numerical_input.txt


Output → outputs/numerical_result.md

C. Traffic Policy Evaluation
python src/main.py --mode policy --input data/policy_input.txt


Output → outputs/policy_result.md

🔢 5. Numerical Module

This module:

loads numerical solver results (Euler & RK4)

sends structured prompts to the LLM

extracts:

best method

reasoning

convergence behavior

LaTeX bullets

outputs a Markdown research summary

🚦 6. Policy Evaluation Module

This module:

loads traffic-policy experiment data

analyzes delays, congestion, throughput

identifies best-performing policy

writes a structured .md file

🤖 7. Transfer Learning Module

This module:

evaluates domain shift

proposes transfer-learning strategies

outputs both JSON + table summaries

📘 8. Example Output (Rendered)
Structured Summary
field	value
domain_shift_description	...
transfer_strategy	...
autonomous_driving_relevance	...
📦 9. Dependencies
pandas  
requests  
python-dotenv  
tabulate  


Requires Ollama running locally.

🏁 10. Summary

This repository provides a reproducible workflow where a local LLM:

interprets numerical experiments

evaluates traffic policies

analyzes transfer learning scenarios

Outputs are structured Markdown files suitable for logs, reports, and coursework.
