🚀 LLM Scientific Experiment Assistant
A modular, research-oriented system for numerical analysis, traffic policy evaluation, and transfer-learning reasoning using a local LLM (Ollama).
📌 1. Introduction

This project demonstrates how a locally-run Large Language Model (LLM) (via Ollama) can be used as a structured scientific reasoning engine—not as a chatbot, but as an integrated component inside a computational workflow.

The system performs three research-relevant tasks:

Numerical Method Analysis — Evaluate stability, convergence, and accuracy of ODE solvers (Euler vs RK4).

Traffic Policy Evaluation — Analyze traffic signal control experiments (digital-twin style) using structured LLM reasoning.

Transfer Learning Interpretation — Analyze domain shifts in autonomous-driving perception and propose transfer-learning strategies.

The project satisfies class requirements while also acting as a research-quality demonstration aligned with PhD topics in:

Autonomous driving

Traffic simulation and digital twins

Optimization & numerical analysis

Transfer learning & computer vision

LLMs as scientific assistants

🧠 2. System Architecture
           +------------------------+
           |   User Input (.txt)    |
           +-----------+------------+
                       |
                       v
       +---------------+------------------+
       |   Preprocessing & Prompt Builder |
       +---------------+------------------+
                       |
                       v
           +-----------+-----------+
           |  Local LLM via Ollama |
           | (llama3 or others)    |
           +-----------+-----------+
                       |
        JSON Validation & Error Handling
                       |
                       v
           +-----------+-----------+
           |  Module-Specific Logic |
           +-----------+-----------+
                       |
                       v
           +------------------------+
           | Markdown Reports (.md) |
           +------------------------+


Each module is independent and designed for research workflows.

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

Download Ollama:
https://ollama.com/download

Then pull a model:

ollama pull llama3

2️⃣ Create a virtual environment
python -m venv .venv


Activate (PowerShell):

. .venv/Scripts/activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ 5. Usage
Run Transfer Learning Analysis
python src/main.py --mode transfer --input data/transfer_input.txt

Run Numerical Stability/Accuracy Analysis
python src/main.py --mode numerical --input data/numerical_input.txt

Run Traffic Policy Evaluation
python src/main.py --mode policy --input data/policy_input.txt


All results are saved into:

outputs/

📊 6. Module Summaries
🔢 A. Numerical Module — Euler vs RK4 Analysis

This module:

loads a CSV of solver outputs

sends them to the LLM for interpretation

extracts structured fields (best method, convergence, stability, LaTeX bullets)

produces a Markdown research summary

Research Relevance:

✔ Numerical analysis
✔ Optimization & PDE reasoning
✔ Interpretable scientific workflow

🚦 B. Policy Evaluation Module — Traffic Signal Optimization

This module:

loads experiment data for multiple traffic signal policies

LLM interprets congestion, delay trends, throughput

outputs a research-style analysis

identifies the best-performing traffic policy

Research Relevance:

✔ Traffic simulation
✔ Autonomous driving
✔ Digital twin analytics
✔ Policy evaluation / optimization

🤖 C. Transfer Learning Module — Autonomous Driving Sensor Shift

This module:

analyzes domain shift between sensor modalities

proposes transfer learning strategies (fine-tuning, augmentation, DA)

explains relevance to self-driving systems

Research Relevance:

✔ Computer vision
✔ Sensor fusion
✔ Transfer learning
✔ Robust autonomous perception

📘 7. Example Output

Example (abridged):

# Transfer Learning Analysis (LLM-Assisted)

Model used: llama3

## Raw JSON Output
{
  "domain_shift_description": "...",
  "transfer_strategy": ["fine-tuning", "augmentation"],
  "autonomous_driving_relevance": "..."
}

## Structured Summary
| field | value |
|-------|--------|
| domain_shift_description | ... |
| transfer_strategy | ... |
| autonomous_driving_relevance | ... |


All modules generate similar Markdown files suitable for a research logbook.

🔬 8. Research Relevance Summary

This project highlights five major competencies expected in top mobility research labs:

✔ Numerical Methods

(RK4/Euler accuracy, stability, convergence)

✔ Optimization & Policy Evaluation

(traffic-delay minimization, digital-twin style experiments)

✔ Computer Vision & Transfer Learning

(domain shift, sensor robustness — key in ADAS/AV labs)

✔ Scientific Tool Building

Modular, reproducible, automatable experiment assistant.

✔ Local LLM Integration

Shows ability to work with constrained offline environments (important for research compute clusters).

🏁 9. Conclusion

This project demonstrates how LLMs can be integrated into scientific computing workflows to produce structured, reproducible analyses across:

numerical ODE solving

traffic simulation and optimization

autonomous-driving perception

It is both a class project and a research portfolio artifact suitable for PhD applications in:

Autonomous driving

Optimization

Game theory

Digital twins

Computer vision

Transportation systems