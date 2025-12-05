🚀 LLM Scientific Experiment Assistant
Author: Sara Momen

A modular system that integrates a locally hosted LLM (Ollama) into scientific workflows for:

Numerical Method Analysis (Euler vs RK4)

Traffic Policy Evaluation (signal-cycle performance)

Transfer Learning Interpretation (domain shift + adaptation strategies)

The model is used programmatically, not as a chatbot. Each module produces validated JSON and Markdown research reports.

🧠 1. System Overview

This project demonstrates how a local LLM can be integrated into:

numerical experiments

traffic-simulation style evaluations

domain-shift reasoning for autonomous-driving sensors

The LLM acts as a structured reasoning engine inside Python pipelines.

Workflow
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


All modules are independent and follow the same pattern.

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

https://ollama.com/download

Pull a model (example):

ollama pull llama3

2️⃣ Create virtual environment
python -m venv .venv
. .venv/Scripts/activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ 4. Running the Modules
A. Transfer Learning Analysis
python src/main.py --mode transfer --input data/transfer_input.txt


Generates:

outputs/transfer_result.md

B. Numerical Method Analysis (Euler vs RK4)
python src/main.py --mode numerical --input data/numerical_input.txt


Uses:

data/numerical_sample.csv


Outputs:

outputs/numerical_result.md

C. Traffic Policy Evaluation
python src/main.py --mode policy --input data/policy_input.txt


Uses synthetic or provided CSV:

data/policy_sample.csv


Outputs:

outputs/policy_result.md

🔢 5. Numerical Module Details

The numerical module:

Loads numerical experiment CSV (Euler/RK4 values)

Sends structured prompt to LLM

Receives JSON with:

best_method

reason

observations

latex_bullets

Converts JSON → Markdown table

Saves research-style summary

This enables automated evaluation of ODE solver behavior.

🚦 6. Policy Evaluation Module Details

The policy module:

Loads synthetic traffic experiment data

Extracts per-policy:

congestion level

average delay

arrival rate

LLM identifies:

strongest policy

performance trends

potential improvements

Outputs a Markdown report summarizing the entire experiment.

This mimics traffic-signal comparative evaluation.

🤖 7. Transfer Learning Module Details

This module:

Reads a sensor observation description

LLM classifies scenario

Describes the domain shift

Recommends adaptation strategies:

fine-tuning

augmentation

domain-adversarial training

States how the adaptation affects perception performance

Outputs Markdown with both JSON and structured table.

📘 8. Example Output Format

Example content inside a generated Markdown file:

# Transfer Learning Analysis

**Model:** llama3

## Raw JSON Output
{ ... }

## Structured Summary
| field | value |
|-------|--------|
| domain_shift_description | ... |
| transfer_strategy | ... |
| autonomous_driving_relevance | ... |


All modules follow the same format for consistency.

📦 9. Dependencies
pandas
requests
python-dotenv
tabulate


Ollama must be running before use.

🏁 10. Summary

This project provides:

programmatic LLM integration

structured scientific reasoning

numerical experiment evaluation

traffic policy comparison

transfer-learning domain-shift analysis

The system is modular, reproducible, and suitable for automation or extension.
