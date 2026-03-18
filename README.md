# AI Financial Coach — Multi-Agent Financial Advisor

> A personalized multi-agent financial advisor that analyzes income, expenses, debt, and savings to deliver actionable strategies using GenAI and data-driven insights.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.2.16-orange)](https://langchain.com/)
[![Gradio](https://img.shields.io/badge/Gradio-4.x-green)](https://gradio.app/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-purple)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Problem Statement

Personal financial planning is complex, fragmented, and inaccessible. Most people lack the expertise to simultaneously analyze their debt structure, optimize savings strategies, and build realistic budgets. Generic financial tools apply one-size-fits-all rules that ignore individual financial profiles.

This system implements a multi-agent architecture where five specialized AI agents collaborate to deliver a complete, personalized financial plan from any uploaded financial document — CSV, Excel, PDF, or Word.

---

## Architecture

Document Upload (CSV, Excel, PDF, Word)
          |
          v
Data Processor
  - Tabular ingestion and transaction parsing
  - Content validation (rejects non-financial documents)
  - Structured financial profile extraction
          |
          v
Multi-Agent Orchestration (LangChain)
  |
  |-- DebtAnalyzerAgent      -> Debt ratios, payoff strategies
  |-- SavingsStrategyAgent   -> Emergency funds, automation plans
  |-- BudgetAdvisorAgent     -> 50/30/20 rule, overspending alerts
  |-- OptimizedPayoffAgent   -> Snowball vs avalanche comparison
  |-- FinancialReportAgent   -> Full summary and action plan
          |
          v
AI Layer
  Primary:  OpenAI GPT-4o-mini (when API key present)
  Fallback: Rule-based analysis (works fully offline)
          |
          v
Web Interface + Dashboards
  Gradio web app + Plotly interactive charts
  Cash flow, category breakdown, savings progress, financial health score

---

## Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Agent Orchestration | LangChain | Multi-agent coordination |
| LLM | OpenAI GPT-4o-mini | AI-powered financial insights |
| Web Interface | Gradio | Interactive web application |
| Visualizations | Plotly | Interactive dashboards |
| Data Processing | Pandas | Transaction analysis |
| Document Parsing | PyPDF2, python-docx, openpyxl | Multi-format ingestion |
| Fallback Engine | Rule-based analysis | Works without API key |
| Language | Python 3.8+ | Core runtime |

---

## Agents

### DebtAnalyzerAgent
Calculates debt-to-income ratios, identifies high-interest liabilities, and recommends payoff sequencing using snowball and avalanche strategies.

### SavingsStrategyAgent
Evaluates current savings rate against income, recommends emergency fund targets, and suggests automation strategies based on cash flow patterns.

### BudgetAdvisorAgent
Applies the 50/30/20 framework to categorize spending, identifies overspending patterns, and generates optimization recommendations.

### OptimizedPayoffAgent
Runs scenario analysis comparing extra payment strategies — quantifies interest savings and time-to-payoff across different approaches.

### FinancialReportAgent
Aggregates outputs from all agents into a cohesive financial health report with a prioritized action plan.

---

## Getting Started

### Prerequisites
- Python 3.8+
- OpenAI API key (optional — app works without it in rule-based mode)

### Installation

Clone the repository:
  git clone https://github.com/sthama121-del/ai_financial_coach.git
  cd ai_financial_coach

Create virtual environment:
  python -m venv .venv

Activate on Windows:
  .venv\Scripts\activate

Activate on macOS/Linux:
  source .venv/bin/activate

Install dependencies:
  pip install -r requirements.txt

### Running the Application

  python app.py

Navigate to http://localhost:7860 in your browser.

### Optional — Enable AI Mode

  export OPENAI_API_KEY="sk-your-key-here"

Without key: rule-based analysis (always works)
With key: full GPT-4o-mini powered insights

---

## Usage

1. Launch the app and open http://localhost:7860
2. Upload a financial file (CSV, Excel, PDF, or Word)
3. The system validates the document and extracts transactions
4. All five agents run in sequence and generate their analysis
5. View the interactive dashboard and download the full report

### Sample CSV Format

Date,Amount,Category,Description
2025-01-01,5200,Salary,Monthly Salary
2025-01-01,-1200,Housing,Rent Payment
2025-01-01,-350,Food,Groceries
2025-01-01,-250,Debt Payment,Credit Card Minimum
2025-01-01,-300,Savings,Emergency Fund

Positive amounts = income, negative amounts = expenses.
Sample files are available in the sample_data/ folder.

---

## Key Capabilities

- Multi-format document ingestion — CSV, Excel, PDF, Word
- Intelligent content validation — rejects non-financial documents with clear error messages
- Five specialized agents working in coordination via LangChain
- Graceful degradation — full functionality without an API key
- Interactive Plotly dashboards — cash flow, spending breakdown, savings trajectory
- Modular architecture — each agent can be tested and extended independently

---

## Business Value

| Dimension | Impact |
|-----------|--------|
| Accessibility | Democratizes financial planning for non-experts |
| Flexibility | Works with any financial document format |
| Reliability | Rule-based fallback ensures 100% uptime without API dependency |
| Extensibility | Modular agent design — new agents can be added without refactoring |
| Cost efficiency | GPT-4o-mini minimizes inference costs vs GPT-4 |

---

## Future Enhancements

- Bank API integration — connect directly to financial accounts via Plaid
- Goal tracking — set and monitor savings/debt payoff milestones over time
- Multi-currency support — handle international financial documents
- Scheduled reports — automated monthly financial health summaries
- RAG over historical data — query past transactions in natural language
- Azure deployment — containerized deployment on Azure Container Apps

---

## Project Structure

ai_financial_coach/
  agents.py           Five specialized AI financial agents
  app.py              Main Gradio web application
  data_processor.py   Document ingestion and validation
  visualizer.py       Plotly dashboards and charts
  requirements.txt    Python dependencies
  sample_data/        Example CSV files for testing
  README.md           This file

---

## Author

Srikanth — Senior Data Engineer / AI Engineer
Specializing in agentic AI systems, GenAI pipelines, and data engineering.

---

## License

MIT License — free to use, modify, and distribute.
