🚀 LLM Scientific Experiment Assistant

A modular, research-oriented system for numerical analysis, traffic policy evaluation, and transfer-learning interpretation using a locally-run LLM (Ollama).

Author: Sara Momen

🧭 1. Introduction

This project demonstrates how a locally-hosted Large Language Model (LLM), executed via Ollama, can be integrated into scientific workflows as a structured reasoning engine, rather than a chatbot.

The system performs three research-relevant tasks:

🔢 Numerical Method Analysis

Evaluates ODE solvers (Euler vs RK4) with respect to:

stability

convergence

accuracy

🚦 Traffic Policy Evaluation

Performs digital-twin–style reasoning on experimental traffic signal data:

congestion interpretation

delay comparison

optimal policy selection

🤖 Transfer Learning Interpretation

Analyzes domain shifts for autonomous-driving sensor data and proposes:

adaptation strategies

robustness techniques

transfer-learning methodologies

🎯 Why This Project Matters (PhD Relevance)

This system directly aligns with research areas in:

Autonomous driving & ADAS

Traffic simulation and digital twins

Optimization & numerical analysis

Domain adaptation / transfer learning

LLMs as scientific assistants

Sensor robustness & computer vision

It showcases skills required for top doctoral programs, including:

scientific reasoning with LLMs

modular tool-building

numerical computing

structured analysis & reproducibility

🧠 2. System Architecture
+-----------------------------+
|        User Input (.txt)    |
+--------------+--------------+
               |
               v
+-----------------------------+
|  Preprocessing + Prompting  |
+--------------+--------------+
               |
               v
+-----------------------------+
|  Local LLM via Ollama       |
|  (llama3 or compatible)     |
+--------------+--------------+
               |
               v
+-----------------------------+
| JSON Parsing + Validation   |
+--------------+--------------+
               |
               v
+-----------------------------+
|   Numerical / Policy /      |
|   Transfer Modules          |
+--------------+--------------+
               |
               v
+-----------------------------+
|  Markdown Research Reports  |
+-----------------------------+


Each module is independent, reusable, and research-oriented.

📂 3. Repository Structure
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

🔧 4. Installation
1️⃣ Install Ollama

Download:
https://ollama.com/download

Pull a model:

ollama pull llama3

2️⃣ Create & Activate a Virtual Environment
python -m venv .venv


PowerShell:

. .venv/Scripts/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ 5. Usage
Transfer Learning Module
python src/main.py --mode transfer --input data/transfer_input.txt

Numerical Method Analysis
python src/main.py --mode numerical --input data/numerical_input.txt

Traffic Policy Evaluation
python src/main.py --mode policy --input data/policy_input.txt


All reports are saved in:

outputs/

📊 6. Module Overviews
🔢 A. Numerical Module — Stability & Convergence Analysis

The module:

loads numerical experiment CSVs

prompts the LLM to analyze errors

extracts structured JSON fields

outputs LaTeX-ready formulas

generates Markdown summaries

Research Relevance

Numerical optimization

Convergence analysis (Euler vs RK4)

PDE solver reasoning

Foundational methods for scientific computing

🚦 B. Policy Evaluation Module — Traffic Signal Optimization

The module:

samples synthetic traffic data

compares policies (cycle times, delay, congestion)

interprets performance via the LLM

outputs recommendations

Research Relevance

Traffic flow optimization

Digital twins / SUMO-style reasoning

Infrastructure-aware autonomous driving

Policy evaluation & reinforcement strategy design

🤖 C. Transfer Learning Module — Domain Shift in AV Perception

The module:

interprets sensor observations

reasons about domain shifts

proposes actionable transfer-learning strategies

Research Relevance

Robustness in autonomous vision systems

Domain adaptation

Cross-sensor policy evaluation

Vision-based mobility optimization

📘 7. Example Research Output (Abridged)
Transfer Learning (LLM-Assisted)
{
  "domain_shift_description": "...",
  "transfer_strategy": ["fine-tuning", "augmentation"],
  "autonomous_driving_relevance": "..."
}


Markdown report includes:

raw JSON

structured table

interpretive commentary

This format matches the expectations of:

research notebooks

lab documentation

reproducible science workflows

🔬 8. Research Competency Demonstrated

This project showcases five high-value PhD skills:

✔ Numerical Methods & Scientific Computing

Euler/RK4 analysis, error quantification, convergence.

✔ Optimization & Policy Reasoning

Traffic flow experiments, digital-twin methodology.

✔ Autonomous-Driving Perception

Domain shift, transfer-learning, sensor adaptation.

✔ LLM-Based Scientific Tool Building

Research automation, structured reasoning, reproducibility.

✔ Systems Engineering

Modular architecture, local inference, experiment pipelines.

🏁 9. Conclusion

This project demonstrates how local LLMs can be transformed into scientific reasoning engines supporting:

ODE numerical analysis

Traffic policy evaluation

Transfer learning for autonomous driving
