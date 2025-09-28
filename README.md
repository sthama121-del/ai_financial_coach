# FinWise AI - Multi-Agent Financial Coach

A personalized multi-agent financial advisor that analyzes income, expenses, debt, and savings to deliver actionable strategies using GenAI + data-driven insights.

## Hackathon Highlights

This project demonstrates how GenAI can simplify financial planning by combining:

**Agent Orchestration**  
Specialized agents (Debt, Savings, Budget, Payoff, Report) orchestrated together to provide a complete financial plan.

**Tabular RAG (Retrieval-Augmented Generation for Tables)**  
Upload CSV/Excel/PDF/Word → structured data is extracted → LLMs reason over this context.

**User Data Integration**  
Works with real financial documents (bank statements, expense sheets) with intelligent content validation.

**LLM Workflow**  
LangChain + OpenAI for personalized insights, with rule-based fallbacks if no API key is available.

**Live Dashboarding**  
Interactive dashboards (Plotly + Gradio) for cash flow, category breakdown, savings, and health scores.

## Key Features

**Debt Analyzer** → Ratios, payoff strategies (snowball vs avalanche)

**Savings Strategist** → Emergency funds, automation, investments

**Budget Advisor** → 50/30/20 rule, overspending alerts, optimization tips

**Payoff Optimizer** → Compare extra payment scenarios

**Report Generator** → Full financial summary & action plan

**Smart File Validation** → Detects and rejects non-financial content (educational docs, manuals, etc.)

## Technical Capabilities

- Tabular ingestion & transaction processing
- AI-enhanced insights (when API key set)
- Rule-based fallback (works even offline)
- Live dashboards with Plotly + Gradio
- Modular architecture with comprehensive error handling
- Content validation to prevent misanalysis of non-financial documents

## Installation & Setup

### Prerequisites
- Python 3.8+
- Virtual environment recommended

### Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/sthama121-del/ai_financial_coach.git
cd ai_financial_coach

# 2. Create & activate environment
python -m venv finwise_env
source finwise_env/bin/activate   # Windows: finwise_env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

## Running the Project

**Option 1 – Web App (Recommended)**
```bash
python app.py
```
Opens at: http://localhost:7860

**Option 2 – Command Line Test**
```bash
python agents.py
```

**Option 3 – Component Tests**
```bash
python data_processor.py   # Document ingestion
python visualizer.py       # Dashboards
```

## Sample Data

Example CSV format (samples in `/sample_data`):

```csv
Date,Amount,Category,Description
2025-01-01,5200,Salary,Monthly Salary
2025-01-01,-1200,Housing,Rent Payment
2025-01-01,-350,Food,Groceries
2025-01-01,-200,Entertainment,Movies & Dining
2025-01-01,-250,Debt Payment,Credit Card
2025-01-01,-300,Savings,Emergency Fund
```

**Format Rules:**
- Positive amounts = Income
- Negative amounts = Expenses
- Additional 2024–2025 datasets included

## AI Features

Enable full AI analysis by adding your OpenAI API key:

```bash
export OPENAI_API_KEY="sk-your-key-here"
```

**Without key** → Rule-based mode (always works)  
**With key** → Full AI-powered insights

## Project Structure

```
ai_financial_coach/
├── agents.py          # Core AI financial agents
├── app.py             # Main Gradio web application
├── data_processor.py  # Data ingestion & validation
├── visualizer.py      # Dashboards & charts
├── requirements.txt   # Dependencies
├── sample_data/       # Example CSV files
└── README.md          # Documentation
```

## Tech Stack

- **LangChain + OpenAI** → AI orchestration
- **Pandas** → Data processing
- **Gradio** → Web interface
- **Plotly** → Interactive visualizations
- **PyPDF2, python-docx, openpyxl** → File parsing

## Demo Instructions (for Hackathon Evaluators)

1. **Start the application:**
   ```bash
   python app.py
   ```

2. **Upload sample data:**
   - Use provided CSV from `/sample_data/` folder
   - Or upload your own financial file

3. **Walk through results:**
   - Debt Analysis → Savings Strategy → Budget Advice → Payoff Plan → Comprehensive Report → Interactive Dashboard

4. **Test file validation:**
   - Try uploading a non-financial document (PDF, Word doc)
   - Observe intelligent rejection with clear error messages

5. **Highlight key features:**
   - Multi-agent orchestration
   - Live interactive dashboarding
   - AI personalization with fallback modes
   - Smart content validation

## Key Differentiators

- **Multi-Agent Architecture:** Five specialized AI agents working together
- **Intelligent File Validation:** Detects and rejects educational content, manuals, and other non-financial documents
- **Graceful Degradation:** Works with or without API keys
- **Real Document Processing:** Handles CSV, Excel, PDF, and Word formats
- **Interactive Visualizations:** Live charts that update with your data

FinWise AI - Turning complex finances into clear, actionable advice through intelligent multi-agent analysis.