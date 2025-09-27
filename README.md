🏦 FinWise – AI Financial Coach Agent

A personalized multi-agent financial advisor that analyzes income, expenses, debt, and savings to deliver actionable strategies through AI + data-driven insights.

🚀 Hackathon Highlights

This project demonstrates how GenAI can simplify financial planning by combining:

✅ Agent Orchestration

Specialized agents for Debt Analysis, Savings Strategy, Budgeting, Payoff Optimization, and Reporting.

Orchestrated together by the AI Financial Coach to provide a complete financial plan.

✅ Tabular RAG (Retrieval-Augmented Generation for Tables)

Upload your financial documents (CSV, Excel, PDF, Word).

The system extracts structured data (income, expenses, categories, transactions).

LLMs reason over this tabular context to generate tailored insights.

✅ User Data Integration

Accepts real user files (bank statements, expense sheets).

Automatically adapts recommendations to your personal finances.

✅ LLM Workflow

Uses LangChain + OpenAI for personalized financial insights.

Includes rule-based fallbacks to ensure the app works even without an API key.

✅ Live Dashboarding

Interactive dashboards with Plotly + Streamlit/Gradio.

Real-time cash flow, category breakdown, health score, and savings analysis.

🧠 Key Features
🏦 Financial Agents

Debt Analyzer Agent → debt ratios, payoff strategies (snowball vs avalanche).

Savings Strategy Agent → emergency funds, automation plans, investment guidance.

Budget Advisor Agent → 50/30/20 rule, overspending detection, optimization tips.

Optimized Payoff Agent → compares debt payoff strategies with extra payments.

Financial Report Agent → combines outputs into a structured report.

⚙️ Technical Capabilities

Tabular data ingestion + transaction processing.

Rule-based fallback when API not available.

AI-enhanced personalization when API is active.

Interactive visualizations (Plotly + Gradio).

Modular architecture with robust error handling.

📦 Installation & Setup
Prerequisites

Python 3.8+

Virtual environment recommended

Quick Start
# 1. Clone the project
git clone <your_repo_url>
cd ai_financial_coach

# 2. Create and activate virtual environment
python -m venv finwise_env
source finwise_env/bin/activate   # Windows: finwise_env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run app.py

▶️ Running the Project

Option 1: Command Line Test

python agents.py


Runs all agents with sample data.

Option 2: Web Interface (Recommended)

streamlit run app.py


Open browser at http://localhost:7860

Upload your CSV/Excel/PDF, or use built-in sample data.

Option 3: Component Testing

python data_processor.py   # Test document processing
python visualizer.py       # Test dashboards

📊 Sample Data

Example CSV format (included in /sample_data):

Date,Amount,Category
2025-01-01,5200,Salary
2025-01-01,-1200,Housing
2025-01-01,-350,Food
2025-01-01,-200,Entertainment
2025-01-01,-250,Debt Payment
2025-01-01,-300,Savings


Positive = income

Negative = expense

More 2024–2025 datasets are included for testing.

✅ Expected Output

Debt Analysis → debt-to-income ratio, payoff strategies, action plan

Savings Strategy → emergency fund, automation plan, investment goals

Budget Analysis → 50/30/20 allocation, overspending alerts

Debt Payoff Plan → snowball vs avalanche with extra payments

Comprehensive Report → combined agent insights

Dashboard → expense breakdown, health score, cash flow trends

🔑 AI Features

Enable AI analysis by setting your key:

export OPENAI_API_KEY="sk-your-key-here"


Without key → Rule-based analysis (always works).

With key → Full AI-powered recommendations.

📂 Project Structure
ai_financial_coach/
├── agents.py            # Core financial agents
├── app.py               # Main web interface (Gradio + Streamlit)
├── data_processor.py    # Document ingestion and processing
├── visualizer.py        # Charts and dashboards
├── requirements.txt     # Dependencies
├── sample_data/         # Sample files for testing
└── README.md            # Documentation

🛠️ Key Technologies

LangChain + OpenAI → AI orchestration & insights

Pandas → data processing

Streamlit + Gradio → interactive UI

Plotly → visualizations

PyPDF2, python-docx, openpyxl → multi-format document parsing

🎯 Hackathon Learning Outcomes

Build multi-agent AI systems with modular orchestration

Apply RAG + LLMs to financial decision support

Design resilient apps with fallbacks (AI or rule-based)

Show how GenAI can automate financial advisory

👩‍🏫 Demo Instructions (for Evaluators)

Run the app:

streamlit run app.py


Upload a sample CSV (or use built-in data).

Walk through outputs:

Debt → Savings → Budget → Payoff → Report → Dashboard

Highlight: multi-agent orchestration + live dashboarding + AI enhancement

✨ FinWise AI – turning complex finances into clear, actionable advice.