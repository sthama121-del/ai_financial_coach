🏦 FinWise – AI Financial Coach Agent

A personalized multi-agent financial advisor that analyzes income, expenses, debt, and savings to deliver actionable strategies using GenAI + data-driven insights.

🚀 Hackathon Highlights

This project demonstrates how GenAI can simplify financial planning by combining:

✅ Agent Orchestration
Specialized agents (Debt, Savings, Budget, Payoff, Report) orchestrated together to provide a complete financial plan.

✅ Tabular RAG (Retrieval-Augmented Generation for Tables)
Upload CSV/Excel/PDF/Word → structured data is extracted → LLMs reason over this context.

✅ User Data Integration
Works with real financial documents (bank statements, expense sheets).

✅ LLM Workflow
LangChain + OpenAI for personalized insights, with rule-based fallbacks if no API key is available.

✅ Live Dashboarding
Interactive dashboards (Plotly + Streamlit/Gradio) for cash flow, category breakdown, savings, and health scores.

🧠 Key Features

🏦 Debt Analyzer → Ratios, payoff strategies (snowball vs avalanche).

💰 Savings Strategist → Emergency funds, automation, investments.

📋 Budget Advisor → 50/30/20 rule, overspending alerts, optimization tips.

🎯 Payoff Optimizer → Compare extra payment scenarios.

📊 Report Generator → Full financial summary & action plan.

⚙️ Technical Capabilities

Tabular ingestion & transaction processing.

AI-enhanced insights (when API key set).

Rule-based fallback (works even offline).

Live dashboards with Plotly + Gradio.

Modular architecture with error handling.

📦 Installation & Setup
Prerequisites

Python 3.8+

Virtual environment recommended

Quick Start
# 1. Clone the repo
git clone https://github.com/sthama121-del/ai_financial_coach.git
cd ai_financial_coach

# 2. Create & activate environment
python -m venv finwise_env
source finwise_env/bin/activate   # Windows: finwise_env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py

▶️ Running the Project

Option 1 – Command Line Test

python agents.py


Option 2 – Web App (Recommended)

streamlit run app.py


Opens at: http://localhost:7860

Option 3 – Component Tests

python data_processor.py   # Document ingestion
python visualizer.py       # Dashboards

📊 Sample Data

Example CSV (in /sample_data):

Date,Amount,Category
2025-01-01,5200,Salary
2025-01-01,-1200,Housing
2025-01-01,-350,Food
2025-01-01,-200,Entertainment
2025-01-01,-250,Debt Payment
2025-01-01,-300,Savings


Positive = Income

Negative = Expense

More 2024–2025 datasets included.

🔑 AI Features

Enable full AI analysis by adding your key:

export OPENAI_API_KEY="sk-your-key-here"


Without key → Rule-based mode (always works).

With key → Full AI-powered insights.

📂 Project Structure
ai_financial_coach/
├── agents.py          # Core AI financial agents
├── app.py             # Main app (Gradio + Streamlit)
├── data_processor.py  # Data ingestion
├── visualizer.py      # Dashboards & charts
├── requirements.txt   # Dependencies
├── sample_data/       # Example CSVs
└── README.md          # Documentation

🛠️ Tech Stack

LangChain + OpenAI → AI orchestration

Pandas → Data processing

Streamlit + Gradio → Web interface

Plotly → Visualizations

PyPDF2, python-docx, openpyxl → File parsing

👩‍🏫 Demo Instructions (for Hackathon Evaluators)

Run:

streamlit run app.py


Upload sample CSV (or your own financial file).

Walk through results:
Debt → Savings → Budget → Payoff → Report → Dashboard

Highlight:

Multi-agent orchestration

Live dashboarding

AI personalization

✨ FinWise AI – Turning complex finances into clear, actionable advice.