⭐ LLM Scientific Experiment Assistant

A modular Python system that uses a local LLM (Ollama) to perform structured scientific reasoning.

📌 What This Project Does

This project turns a local LLM into a scientific computation assistant by integrating it into Python workflows.
Instead of chatting, the LLM:

interprets numerical experiments (Euler vs RK4)

evaluates traffic-signal policies using synthetic datasets

explains transfer-learning strategies for autonomous-driving sensors

produces structured JSON + Markdown reports

Every module reads simple .txt inputs, generates prompts, validates LLM JSON output, and writes clean .md reports.

The whole system works offline using Ollama + llama3.

🧠 How the System Works (Technical Summary)
 User Input (.txt / .csv)
          ↓
 Python Module (Numerical / Policy / Transfer)
          ↓
 Prompt Builder → LLM Query (Ollama REST API)
          ↓
 JSON Validation (strict)
          ↓
 Markdown Report Generator
          ↓
 outputs/*.md


✔ Each module is completely independent
✔ All outputs are deterministic Markdown files
✔ LLM errors are caught and handled

📂 Project Structure (Beautiful Tree View)
LLM-scientific-experiment-assistant/
│
├── data/
│   ├── numerical_input.txt
│   ├── numerical_sample.csv
│   ├── policy_input.txt
│   ├── policy_sample.csv
│   └── transfer_input.txt
│
├── outputs/
│   ├── numerical_result.md
│   ├── numerical_output_raw.txt
│   ├── policy_result.md
│   └── transfer_result.md
│
├── src/
│   ├── main.py
│   ├── ollama_client.py
│   ├── numerical_module.py
│   ├── policy_module.py
│   └── transfer_module.py
│
├── requirements.txt
└── README.md


✔ Clean
✔ Indented
✔ Professional

⚙️ Installation
1️⃣ Install Ollama

Download for Windows/macOS/Linux:
👉 https://ollama.com/download

Pull a model:

ollama pull llama3

2️⃣ Create Virtual Environment
python -m venv .venv


Activate (PowerShell):

. .venv/Scripts/activate

3️⃣ Install Python Dependencies
pip install -r requirements.txt

▶️ How to Run the Modules
🔢 Numerical Solver Analysis

Euler vs RK4 stability, convergence, and error reasoning.

python src/main.py --mode numerical --input data/numerical_input.txt


Output → outputs/numerical_result.md

🚦 Traffic Policy Evaluation

Evaluates synthetic traffic-signal experiment data.

python src/main.py --mode policy --input data/policy_input.txt


Output → outputs/policy_result.md

🤖 Transfer-Learning Reasoning

Analyzes domain shift + transfer-strategy proposals.

python src/main.py --mode transfer --input data/transfer_input.txt


Output → outputs/transfer_result.md

🔬 Module Descriptions
🔢 Numerical Module

Loads CSV of solver outputs

Computes error trends

Sends structured query to LLM

Validates JSON

Produces a Markdown research report

The LLM provides:

best numerical method

reasoning

convergence comments

LaTeX-formatted insights

🚦 Policy Module

Loads a synthetic experiment table

LLM selects best-performing traffic policy

Produces markdown explanation of congestion, delay, and throughput

Useful for:

traffic engineering

simulation-based optimization

digital twins

🤖 Transfer Learning Module

LLM analyzes domain shift

Recommends transfer learning techniques

Explains how the shift impacts autonomous driving

Outputs include:

domain-shift description

recommended methods

relevance explanation

📊 Example Output Preview
Markdown Report Example
# Transfer Learning Analysis
Model: llama3

## JSON Output
{ ... }

## Structured Summary
field | value
------|-------
domain_shift_description | ...
transfer_strategy | ...
relevance | ...

🧩 Technical Highlights

Fully modular Python architecture

Strict JSON validation to avoid hallucinations

Local LLM inference (no API keys or cloud required)

Reproducible scientific experiments

Clean Markdown reporting pipeline

🏁 Conclusion

This project shows how LLMs can be embedded inside real computational pipelines, not as chatbots but as structured scientific reasoning engines.

It is a clean, modular, reproducible system designed for:

numerical analysis

traffic optimization studies

transfer learning research

Everything runs locally and outputs well-formatted analytical reports.
