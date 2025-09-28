# ============================================================================
# FinWise AI - MAIN APPLICATION WITH BUILT-IN PREREQUISITES
# ============================================================================

import sys
import subprocess
import os
import importlib.util

# ============================================================================
# PREREQUISITE CHECKER - Smart Dependency Management
# ============================================================================

def check_and_install_dependencies():
    """Smart dependency checker and installer"""
    print("🔧 Checking dependencies...")
    
    required_packages = {
        'gradio': 'gradio',
        'langchain_openai': 'langchain-openai',
        'langchain.prompts': 'langchain',
        'pandas': 'pandas',
        'plotly': 'plotly',
        'PyPDF2': 'PyPDF2',
        'docx': 'python-docx',
        'openpyxl': 'openpyxl'
    }
    
    missing_packages = []
    
    for import_name, install_name in required_packages.items():
        try:
            if '.' in import_name:
                main_module = import_name.split('.')[0]
                importlib.import_module(main_module)
            else:
                importlib.import_module(import_name)
            print(f"✅ {install_name} - already installed")
        except ImportError:
            print(f"⚠️ {install_name} - missing")
            missing_packages.append(install_name)
    
    if missing_packages:
        print(f"\n🔧 Installing {len(missing_packages)} missing packages...")
        for package in missing_packages:
            try:
                print(f"📦 Installing {package}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"✅ {package} installed successfully!")
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to install {package}: {e}")
                return False
    
    print("✅ All dependencies are ready!")
    return True

def validate_environment():
    """Environment validation with helpful guidance"""
    print("\n🔍 Validating environment...")
    
    openai_key = os.getenv("OPENAI_API_KEY")
    
    if not openai_key or openai_key == "your-api-key-here":
        print("⚠️  OpenAI API key not found!")
        print("\n🔑 For full AI analysis, you need an OpenAI API key:")
        print("   1. Visit: https://platform.openai.com/api-keys")
        print("   2. Sign up/login and create a new API key")
        print("   3. Copy the key (starts with 'sk-')")
        print("   4. Set it in your terminal:")
        print("      export OPENAI_API_KEY='your-key-here'")
        print("   5. Restart this application")
        print("\n💡 Don't worry - the app still works with sample analysis!")
        return False
    else:
        if openai_key.startswith('sk-') and len(openai_key) > 20:
            print("✅ OpenAI API key found and looks valid!")
            return True
        else:
            print("⚠️  OpenAI API key found but format looks incorrect")
            return False

def system_diagnostics():
    """System diagnostics and health check"""
    print("\n🩺 Running system diagnostics...")
    
    python_version = sys.version_info
    print(f"🐍 Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("⚠️  Python 3.8+ recommended for best compatibility")
    else:
        print("✅ Python version is compatible")
    
    venv_path = os.environ.get('VIRTUAL_ENV')
    if venv_path:
        print(f"✅ Virtual environment active: {os.path.basename(venv_path)}")
    else:
        print("⚠️  No virtual environment detected (recommended but not required)")
    
    try:
        import psutil
        memory = psutil.virtual_memory()
        print(f"💾 Available RAM: {memory.available // (1024**3):.1f} GB")
    except ImportError:
        print("💾 Memory check skipped (psutil not available)")
    
    print("✅ System diagnostics complete!")

# ============================================================================
# SMART IMPORTS WITH FALLBACKS
# ============================================================================

try:
    import gradio as gr
    GRADIO_AVAILABLE = True
except ImportError:
    print("⚠️ Gradio not found - will attempt to install automatically")
    GRADIO_AVAILABLE = False

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    print("⚠️ Pandas not found - will attempt to install automatically")
    PANDAS_AVAILABLE = False

try:
    from agents import (
        DebtAnalyzerAgent,
        SavingsStrategyAgent,
        BudgetAdvisorAgent,
        OptimizedPayoffAgent,
        FinancialReportAgent
    )
    AGENTS_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ AI Agents import issue: {e}")
    AGENTS_AVAILABLE = False

try:
    from data_processor import FinancialDataProcessor, create_sample_data
    DATA_PROCESSOR_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Data Processor import issue: {e}")
    DATA_PROCESSOR_AVAILABLE = False

try:
    from visualizer import FinancialVisualizer
    VISUALIZER_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Visualizer import issue: {e}")
    VISUALIZER_AVAILABLE = False

# ============================================================================
# MAIN APPLICATION CLASS
# ============================================================================

class AIFinancialCoach:
    """Main AI Financial Coach application class"""
    
    def __init__(self):
        """Initialize all AI agents and supporting modules"""
        print("🚀 Initializing FinWise AI...")
        
        try:
            if AGENTS_AVAILABLE:
                self.debt_analyzer = DebtAnalyzerAgent()
                self.savings_strategist = SavingsStrategyAgent()
                self.budget_advisor = BudgetAdvisorAgent()
                self.payoff_optimizer = OptimizedPayoffAgent()
                self.report_generator = FinancialReportAgent()
                print("✅ All AI agents initialized successfully!")
            else:
                print("⚠️ AI agents not available - using fallback mode")
        except Exception as e:
            print(f"⚠️ Warning: AI agents initialization issue: {e}")
        
        try:
            if DATA_PROCESSOR_AVAILABLE and VISUALIZER_AVAILABLE:
                self.data_processor = FinancialDataProcessor()
                self.visualizer = FinancialVisualizer()
                print("✅ Supporting modules initialized successfully!")
            else:
                print("⚠️ Some supporting modules not available")
        except Exception as e:
            print(f"⚠️ Warning: Supporting modules initialization issue: {e}")
        
        print("🎉 FinWise AI ready for action!")
    
    def analyze_finances(self, file_upload, financial_goals, extra_payment):
        """Main financial analysis function"""
        print("📄 Starting financial analysis workflow...")
        
        try:
            # Process financial data
            if file_upload is not None and DATA_PROCESSOR_AVAILABLE:
                print(f"📤 Processing uploaded file: {file_upload.name}")
                financial_data = self.data_processor.process_document(file_upload.name)
                if "error" in financial_data:
                    financial_data = create_sample_data()
                    report_note = "⚠️ Using sample data due to file processing error. "
                else:
                    report_note = "✅ Successfully processed your financial document. "
            else:
                if DATA_PROCESSOR_AVAILABLE:
                    financial_data = create_sample_data()
                else:
                    # Fallback sample data
                    financial_data = {
                        'total_income': 5000,
                        'total_expenses': 3500,
                        'categories': {'Rent': 1200, 'Food': 400, 'Transport': 300, 'Utilities': 200}
                    }
                report_note = "📊 Using sample financial data for demonstration. "
            
            # Run AI analysis if available
            if AGENTS_AVAILABLE and hasattr(self, 'report_generator'):
                print("🤖 Running AI financial analysis agents...")
                
                debt_analysis = self.debt_analyzer.analyze_debt(financial_data)
                savings_strategy = self.savings_strategist.create_savings_plan(financial_data, financial_goals)
                budget_advice = self.budget_advisor.analyze_budget(financial_data)
                
                extra_payment_amount = float(extra_payment) if extra_payment else 0
                payoff_plan = self.payoff_optimizer.create_payoff_plan(financial_data, extra_payment_amount)
                
                comprehensive_report = self.report_generator.generate_report(
                    debt_analysis, savings_strategy, budget_advice, payoff_plan, financial_data
                )
            else:
                # Fallback analysis
                print("📊 Generating fallback financial analysis...")
                income = financial_data.get('total_income', 0)
                expenses = financial_data.get('total_expenses', 0)
                net_savings = income - expenses
                savings_rate = (net_savings / income * 100) if income > 0 else 0
                
                comprehensive_report = f"""
                ## 📊 Financial Analysis Summary
                
                **Monthly Overview:**
                - Income: ${income:,.2f}
                - Expenses: ${expenses:,.2f}
                - Net Savings: ${net_savings:,.2f}
                - Savings Rate: {savings_rate:.1f}%
                
                **Key Recommendations:**
                - Emergency Fund: Aim for 3-6 months of expenses (${expenses * 3:,.2f} - ${expenses * 6:,.2f})
                - Budget Rule: Follow 50/30/20 (needs/wants/savings)
                - Debt Strategy: Pay high-interest debt first
                
                💡 **Note:** Full AI analysis requires OpenAI API key setup.
                """
            
            # Create dashboard
            if VISUALIZER_AVAILABLE and hasattr(self, 'visualizer'):
                financial_dashboard = self.visualizer.create_financial_dashboard(financial_data)
            else:
                financial_dashboard = """
                <div style="text-align: center; padding: 50px; background: #f8f9fa; border-radius: 10px;">
                    <h3>📊 Dashboard</h3>
                    <p>Interactive dashboard requires full setup completion.</p>
                </div>
                """
            
            return report_note + comprehensive_report, financial_dashboard
            
        except Exception as e:
            print(f"❌ Error during financial analysis: {e}")
            
            error_message = f"""
            ❌ **Error Processing Your Financial Analysis**
            
            **What happened:** {str(e)}
            
            **Possible causes:**
            - Missing OpenAI API key
            - Missing required modules
            - File format issues
            
            **Solutions:**
            1. Set OPENAI_API_KEY environment variable
            2. Check all required files are present
            3. Try with sample data (no file upload)
            """
            
            error_dashboard = """
            <div style="text-align: center; padding: 50px; background: #f8f9fa; border-radius: 10px;">
                <h2 style="color: #dc3545;">📊 Dashboard Temporarily Unavailable</h2>
                <p>Please resolve the error above to access dashboard.</p>
            </div>
            """
            
            return error_message, error_dashboard

# ============================================================================
# HELPER FUNCTIONS FOR PLOTS
# ============================================================================

def analyze_finances_with_plots(file_upload, financial_goals, extra_payment):
    """Enhanced analysis function that returns separate plot components"""
    try:
        coach = AIFinancialCoach()
        report, _ = coach.analyze_finances(file_upload, financial_goals, extra_payment)
        
        # Get financial data for plots
        if file_upload is not None and DATA_PROCESSOR_AVAILABLE:
            financial_data = coach.data_processor.process_document(file_upload.name)
            if "error" in financial_data:
                financial_data = create_sample_data() if DATA_PROCESSOR_AVAILABLE else {
                    'total_income': 5000, 'total_expenses': 3500,
                    'categories': {'Rent': 1200, 'Food': 400, 'Transport': 300}
                }
        else:
            financial_data = create_sample_data() if DATA_PROCESSOR_AVAILABLE else {
                'total_income': 5000, 'total_expenses': 3500,
                'categories': {'Rent': 1200, 'Food': 400, 'Transport': 300}
            }
        
        expense_fig = create_expense_plot(financial_data)
        cashflow_fig = create_cashflow_plot(financial_data)
        metrics_html = create_metrics_summary(financial_data)
        
        return report, expense_fig, cashflow_fig, metrics_html
        
    except Exception as e:
        print(f"Error in enhanced analysis: {e}")
        error_fig = create_error_plot(str(e))
        error_html = f"<div style='color: red; padding: 20px;'>Error: {str(e)}</div>"
        return f"Analysis Error: {str(e)}", error_fig, error_fig, error_html

def create_expense_plot(financial_data):
    """Create expense pie chart"""
    try:
        import plotly.graph_objects as go
        
        categories = financial_data.get('categories', {})
        expense_categories = {
            category: amount for category, amount in categories.items() 
            if category.lower() not in ['salary', 'income', 'deposit', 'bonus', 'refund']
        }
        
        if not expense_categories:
            expense_categories = {'No Data': 1}
        
        fig = go.Figure(data=[go.Pie(
            labels=list(expense_categories.keys()),
            values=list(expense_categories.values()),
            hole=0.3,
            textinfo='label+percent'
        )])
        
        fig.update_layout(title="Monthly Expense Breakdown", height=400)
        return fig
        
    except Exception as e:
        return create_error_plot("Expense chart error")

def create_cashflow_plot(financial_data):
    """Create cash flow bar chart"""
    try:
        import plotly.graph_objects as go
        
        income = financial_data.get('total_income', 0)
        expenses = financial_data.get('total_expenses', 0)
        net_savings = income - expenses
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=['Income', 'Expenses', 'Net Savings'],
            y=[income, expenses, net_savings],
            marker_color=['green', 'red', 'blue' if net_savings >= 0 else 'red']
        ))
        
        fig.update_layout(title="Monthly Cash Flow Overview", height=400)
        return fig
        
    except Exception as e:
        return create_error_plot("Cash flow chart error")

def create_metrics_summary(financial_data):
    """Create HTML summary of key metrics"""
    income = financial_data.get('total_income', 0)
    expenses = financial_data.get('total_expenses', 0)
    net_cash_flow = income - expenses
    savings_rate = ((net_cash_flow / income) * 100) if income > 0 else 0
    
    return f"""
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
        <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid green;">
            <h4>Monthly Income</h4>
            <p style="font-size: 20px; font-weight: bold;">${income:,.2f}</p>
        </div>
        <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid red;">
            <h4>Monthly Expenses</h4>
            <p style="font-size: 20px; font-weight: bold;">${expenses:,.2f}</p>
        </div>
        <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid blue;">
            <h4>Net Cash Flow</h4>
            <p style="font-size: 20px; font-weight: bold;">${net_cash_flow:,.2f}</p>
            <p>({savings_rate:.1f}% savings rate)</p>
        </div>
    </div>
    """

def create_error_plot(error_message):
    """Create error plot when something goes wrong"""
    try:
        import plotly.graph_objects as go
        fig = go.Figure()
        fig.add_annotation(text=f"Chart Error: {error_message}", showarrow=False, x=0.5, y=0.5)
        fig.update_layout(title="Chart Unavailable", height=300)
        return fig
    except:
        return None

# ============================================================================
# GRADIO INTERFACE CREATION - THIS FUNCTION MUST BE AT MODULE LEVEL
# ============================================================================

def create_gradio_interface():
    """Create the Gradio web interface"""
    print("🎨 Creating Gradio web interface...")
    
    # Initialize our FinWise AI
    coach = AIFinancialCoach()
    
    with gr.Blocks(
        theme=gr.themes.Soft(),
        title="FinWise AI",
        css="""
        .gradio-container {
            max-width: 1200px !important;
            margin: auto;
        }
        .main-header {
            text-align: center;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            margin: 1rem 0;
        }
        """
    ) as app:
        
        # Header
        gr.HTML("""
        <div class="main-header">
            <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem;">
                🏦 FinWise AI Agent
            </h1>
            <p style="font-size: 1.2rem; margin: 0;">
                Get personalized financial advice powered by multiple AI agents
            </p>
        </div>
        """)
        
        # Feature description
        gr.Markdown("""
        ### 🚀 **What This App Does:**
        
        **🤖 Multi-Agent AI Analysis:**
        - 🏦 **Debt Analyzer**: Identifies debt patterns and suggests payoff strategies
        - 💰 **Savings Strategist**: Creates emergency funds and investment plans  
        - 📋 **Budget Advisor**: Analyzes spending with proven 50/30/20 rule
        - 🎯 **Payoff Optimizer**: Compares avalanche vs snowball debt methods
        - 📊 **Report Compiler**: Generates comprehensive financial health reports
        """)
        
        # Input section
        gr.Markdown("### 📤 **Upload Your Financial Data**")
        
        with gr.Row():
            with gr.Column(scale=2):
                file_upload = gr.File(
                    label="📄 Upload Financial Document",
                    file_count="single",
                    file_types=[".csv", ".xlsx", ".xls", ".pdf"]
                )
                
                gr.Markdown("""
                **💡 Sample CSV Format:**
                ```
                Date,Amount,Category,Description
                2024-01-01,3000,Salary,Monthly Salary
                2024-01-02,-150,Groceries,Whole Foods
                2024-01-03,-1200,Rent,Apartment Rent
                ```
                """)
            
            with gr.Column(scale=1):
                financial_goals = gr.Textbox(
                    label="🎯 Your Financial Goals",
                    placeholder="e.g., Save for emergency fund, pay off credit card debt...",
                    lines=4
                )
                
                extra_payment = gr.Number(
                    label="💵 Extra Monthly Payment for Debts",
                    value=0,
                    minimum=0
                )
        
        # Analysis button
        analyze_button = gr.Button(
            "🚀 Analyze My Finances",
            variant="primary",
            size="lg"
        )
        
        # Output section
        gr.Markdown("### 📊 **Your Personalized Financial Analysis**")
        
        with gr.Row():
            with gr.Column(scale=2):
                financial_report = gr.Markdown(
                    label="📋 Comprehensive Financial Report",
                    value="Click 'Analyze My Finances' to get your personalized report..."
                )

        with gr.Row():
            with gr.Column():
                expense_chart = gr.Plot(label="📊 Expense Breakdown")
            with gr.Column():
                cashflow_chart = gr.Plot(label="💰 Cash Flow Overview")

        with gr.Row():
            with gr.Column():
                metrics_summary = gr.HTML(
                    label="📈 Financial Health Metrics",
                    value="<div style='text-align: center; padding: 20px;'>Metrics will appear after analysis...</div>"
                )
        
        # Footer
        gr.Markdown("""
        ---
        ### 🔒 **Privacy & Security**
        - Your financial data is processed locally and not stored
        - AI analysis uses OpenAI's secure API
        - No data is shared with third parties
        """)
        
        # Connect button to analysis function
        analyze_button.click(
            fn=analyze_finances_with_plots,
            inputs=[file_upload, financial_goals, extra_payment],
            outputs=[financial_report, expense_chart, cashflow_chart, metrics_summary],
            show_progress=True
        )
    
    print("✅ Gradio interface created successfully!")
    return app

# ============================================================================
# MAIN EXECUTION FUNCTIONS
# ============================================================================

def main():
    """Main application entry point"""
    print("=" * 60)
    print("🏦 FinWise AI - STARTING UP")
    print("=" * 60)
    
    # Check for OpenAI API key
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key or openai_key == "your-api-key-here":
        print("⚠️  WARNING: OPENAI_API_KEY not found!")
        print("🔑 To get full AI analysis, you need an OpenAI API key:")
        print("   1. Go to https://platform.openai.com/api-keys")
        print("   2. Create a new API key")
        print("   3. Set it: export OPENAI_API_KEY='your-key-here'")
        print("📊 App will still work with sample analysis!")
    else:
        print("✅ OpenAI API key found - full AI analysis available!")
    
    try:
        print("🔧 Running pre-flight checks...")
        
        if not check_and_install_dependencies():
            print("❌ Dependency installation failed!")
            return
        
        api_key_valid = validate_environment()
        system_diagnostics()
        
        print("🎨 Creating web interface...")
        app = create_gradio_interface()
        
        print("\n" + "=" * 60)
        print("🎉 FinWise AI IS READY!")
        print("=" * 60)
        print("📱 Open: http://localhost:7860")
        print("📊 Upload financial data or try sample analysis")
        if not api_key_valid:
            print("💡 Demo mode - add API key for full analysis")
        print("=" * 60)
        
        in_colab = "COLAB_RELEASE_TAG" in os.environ or "COLAB_GPU" in os.environ
        
        app.launch(
            server_name="0.0.0.0",
            server_port=7860,
            share=in_colab,
            show_error=True,
            quiet=False,
            inbrowser=not in_colab
        )
        
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        print("\n🔧 Troubleshooting:")
        print("   1. Check error message above")
        print("   2. Ensure correct directory")
        print("   3. Try: pip install --upgrade gradio")
        print("   4. Check port 7860 availability")

def startup_sequence():
    """Enhanced startup sequence"""
    print("=" * 60)
    print("🏦 FinWise AI - ENHANCED STARTUP")
    print("=" * 60)
    print("🔧 Built-in dependency management")
    print("🔍 Automatic environment validation")
    print("🩺 Complete system diagnostics")
    print("🚀 Smart application launch")
    print("=" * 60)
    main()

# ============================================================================
# APPLICATION ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    startup_sequence()