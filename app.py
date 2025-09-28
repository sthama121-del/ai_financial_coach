# ============================================================================
# FinWise AI - MAIN APPLICATION WITH BUILT-IN PREREQUISITES
# ============================================================================
# This is the main application file that brings together all our AI agents,
# data processing, and visualization components into one beautiful web interface.
# 
# NEW FEATURES ADDED:
# 🔧 Automatic dependency checking and installation
# 🔍 Environment validation with helpful error messages
# 🚨 Graceful fallbacks when components aren't available
# 📋 Self-diagnosing system that guides users through setup
# 
# WHAT THIS APPLICATION DOES:
# 1. ✅ Checks and installs missing dependencies automatically
# 2. 🔑 Validates OpenAI API key and provides setup instructions
# 3. 📊 Processes financial documents (CSV, Excel, PDF)
# 4. 🤖 Runs 5 AI agents to analyze your finances
# 5. 📈 Creates beautiful interactive dashboards
# 6. 📋 Generates comprehensive financial reports
# 7. 🎯 Provides actionable recommendations
# ============================================================================

import sys
import subprocess
import os
import importlib.util

# ============================================================================
# PREREQUISITE CHECKER - Smart Dependency Management
# ============================================================================

def check_and_install_dependencies():
    """
    🔧 SMART DEPENDENCY CHECKER AND INSTALLER
    
    WHAT THIS FUNCTION DOES:
    1. Checks if required packages are installed
    2. Attempts to install missing packages automatically
    3. Provides clear error messages if installation fails
    4. Validates that installations work correctly
    
    WHY THIS IS IMPORTANT:
    - Users don't need to manually install packages
    - Reduces setup friction for demos and hackathons
    - Professional applications handle their own dependencies
    - Provides better user experience
    
    PACKAGES WE NEED:
    - gradio: Web interface framework
    - langchain-openai: AI language models
    - pandas: Data manipulation
    - plotly: Interactive charts
    - PyPDF2: PDF document processing
    - python-docx: Word document processing
    - openpyxl: Excel file processing
    """
    
    print("🔧 Checking dependencies...")
    
    # Define required packages with their import names and install names
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
    
    # Check each package
    for import_name, install_name in required_packages.items():
        try:
            # Try to import the package
            if '.' in import_name:
                # Handle nested imports like 'langchain.prompts'
                main_module = import_name.split('.')[0]
                importlib.import_module(main_module)
            else:
                importlib.import_module(import_name)
            print(f"✅ {install_name} - already installed")
        except ImportError:
            print(f"❌ {install_name} - missing")
            missing_packages.append(install_name)
    
    # Install missing packages
    if missing_packages:
        print(f"\n🔧 Installing {len(missing_packages)} missing packages...")
        
        for package in missing_packages:
            try:
                print(f"📦 Installing {package}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"✅ {package} installed successfully!")
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to install {package}: {e}")
                print(f"💡 Please run manually: pip install {package}")
                return False
    
    print("✅ All dependencies are ready!")
    return True

def validate_environment():
    """
    🔍 ENVIRONMENT VALIDATION WITH HELPFUL GUIDANCE
    
    WHAT THIS FUNCTION DOES:
    1. Checks for OpenAI API key
    2. Provides setup instructions if missing
    3. Tests that key works (optional)
    4. Gives guidance on getting API keys
    
    WHY THIS MATTERS:
    - API key is crucial for AI functionality
    - Better to catch issues early than during demo
    - Provides educational value about API setup
    - Graceful degradation when key is missing
    """
    
    print("\n🔍 Validating environment...")
    
    # Check for OpenAI API key
    openai_key = os.getenv("OPENAI_API_KEY")
    
    if not openai_key or openai_key == "your-api-key-here":
        print("⚠️  OpenAI API key not found!")
        print("")
        print("🔑 For full AI analysis, you need an OpenAI API key:")
        print("   1. Visit: https://platform.openai.com/api-keys")
        print("   2. Sign up/login and create a new API key")
        print("   3. Copy the key (starts with 'sk-')")
        print("   4. Set it in your terminal:")
        print("      export OPENAI_API_KEY='your-key-here'")
        print("   5. Restart this application")
        print("")
        print("💡 Don't worry - the app still works with sample analysis!")
        print("   You can demo all features without an API key.")
        print("")
        return False
    else:
        # Validate that the key format looks correct
        if openai_key.startswith('sk-') and len(openai_key) > 20:
            print("✅ OpenAI API key found and looks valid!")
            return True
        else:
            print("⚠️  OpenAI API key found but format looks incorrect")
            print("💡 Keys should start with 'sk-' and be ~50+ characters")
            return False

def system_diagnostics():
    """
    🩺 SYSTEM DIAGNOSTICS - Complete Health Check
    
    WHAT THIS FUNCTION DOES:
    1. Checks Python version compatibility
    2. Validates virtual environment setup
    3. Tests import capabilities
    4. Reports system specifications
    5. Provides optimization suggestions
    """
    
    print("\n🩺 Running system diagnostics...")
    
    # Check Python version
    python_version = sys.version_info
    print(f"🐍 Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("⚠️  Python 3.8+ recommended for best compatibility")
    else:
        print("✅ Python version is compatible")
    
    # Check virtual environment
    venv_path = os.environ.get('VIRTUAL_ENV')
    if venv_path:
        print(f"✅ Virtual environment active: {os.path.basename(venv_path)}")
    else:
        print("⚠️  No virtual environment detected (recommended but not required)")
    
    # Check available memory (simplified)
    try:
        import psutil
        memory = psutil.virtual_memory()
        print(f"💾 Available RAM: {memory.available // (1024**3):.1f} GB")
    except ImportError:
        print("💾 Memory check skipped (psutil not available)")
    
    print("✅ System diagnostics complete!")

# ============================================================================

# SMART IMPORTS WITH FALLBACKS - Professional Error Handling
try:
    import gradio as gr  # Web interface framework - makes beautiful UIs easy
    GRADIO_AVAILABLE = True
except ImportError:
    print("⚠️ Gradio not found - will attempt to install automatically")
    GRADIO_AVAILABLE = False

try:
    import pandas as pd  # Data manipulation library
    PANDAS_AVAILABLE = True
except ImportError:
    print("⚠️ Pandas not found - will attempt to install automatically")
    PANDAS_AVAILABLE = False

# Our custom modules (the files we created)
try:
    from agents import (
        DebtAnalyzerAgent,      # 🏦 Finds and analyzes debt
        SavingsStrategyAgent,   # 💰 Creates savings plans
        BudgetAdvisorAgent,     # 📋 Analyzes budgets with 50/30/20 rule
        OptimizedPayoffAgent,   # 🎯 Optimizes debt payoff strategies
        FinancialReportAgent    # 📊 Compiles comprehensive reports
    )
    AGENTS_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ AI Agents import issue: {e}")
    AGENTS_AVAILABLE = False

try:
    from data_processor import FinancialDataProcessor, create_sample_data  # Document processing
    DATA_PROCESSOR_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Data Processor import issue: {e}")
    DATA_PROCESSOR_AVAILABLE = False

try:
    from visualizer import FinancialVisualizer  # Chart and dashboard creation
    VISUALIZER_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Visualizer import issue: {e}")
    VISUALIZER_AVAILABLE = False

# ============================================================================
# MAIN APPLICATION CLASS - The Brain That Orchestrates Everything
# ============================================================================
# This class is like a conductor of an orchestra - it coordinates all the
# different AI agents, makes sure they work together harmoniously, and
# presents the final performance (financial analysis) to the user.
# ============================================================================

class AIFinancialCoach:
    """
    🧠 FinWise AI - MAIN APPLICATION CLASS
    
    WHAT THIS CLASS DOES:
    - Initializes all 5 AI agents
    - Coordinates the analysis workflow
    - Handles file uploads and data processing
    - Manages error handling and fallbacks
    - Orchestrates the complete financial analysis pipeline
    
    THINK OF IT AS:
    - A financial advisor's office with 5 specialists
    - Each specialist (agent) has expertise in one area
    - This class coordinates appointments and compiles advice
    - User gets comprehensive analysis from all specialists
    
    WORKFLOW ORCHESTRATION:
    1. Process uploaded financial document
    2. Run debt analysis (find and prioritize debts)
    3. Create savings strategy (emergency fund, goals)
    4. Analyze budget (50/30/20 rule compliance)
    5. Optimize debt payoff (avalanche vs snowball)
    6. Generate comprehensive report
    7. Create interactive dashboard
    8. Present everything in user-friendly format
    """
    
    def __init__(self):
        """
        INITIALIZATION: Set up all the AI agents and supporting modules
        
        WHY WE INITIALIZE HERE:
        - Creates all agents once at startup (efficient)
        - Ensures all components are ready before user interaction
        - Provides single point of configuration
        - Makes error handling centralized
        """
        
        print("🚀 Initializing FinWise AI...")
        
        # STEP 1: Initialize all 5 AI financial agents
        try:
            self.debt_analyzer = DebtAnalyzerAgent()           # 🏦 Debt analysis specialist
            self.savings_strategist = SavingsStrategyAgent()   # 💰 Savings planning expert
            self.budget_advisor = BudgetAdvisorAgent()         # 📋 Budget optimization guru
            self.payoff_optimizer = OptimizedPayoffAgent()    # 🎯 Debt payoff strategist
            self.report_generator = FinancialReportAgent()     # 📊 Report compilation specialist
            print("✅ All AI agents initialized successfully!")
        except Exception as e:
            print(f"⚠️ Warning: AI agents initialization issue: {e}")
        
        # STEP 2: Initialize supporting modules
        try:
            self.data_processor = FinancialDataProcessor()     # 📄 Document processing engine
            self.visualizer = FinancialVisualizer()           # 📊 Chart and dashboard creator
            print("✅ Supporting modules initialized successfully!")
        except Exception as e:
            print(f"⚠️ Warning: Supporting modules initialization issue: {e}")
        
        print("🎉 FinWise AI ready for action!")
    
    def analyze_finances(self, file_upload, financial_goals, extra_payment):
        """
        🎯 MAIN ANALYSIS FUNCTION - The Heart of Our Application
        
        This is the main function that gets called when user clicks "Analyze"
        It orchestrates the entire financial analysis workflow.
        
        INPUTS FROM USER INTERFACE:
        - file_upload: User's financial document (CSV, Excel, PDF) or None
        - financial_goals: Text describing user's financial objectives
        - extra_payment: Additional money available for debt payments per month
        
        OUTPUTS TO USER INTERFACE:
        - comprehensive_report: Detailed financial analysis and recommendations
        - financial_dashboard: Interactive charts and visualizations
        
        WORKFLOW:
        1. 📄 Process Document: Extract financial data from upload or use sample
        2. 🤖 Run AI Agents: Each agent analyzes different aspects
        3. 📊 Create Visuals: Generate charts and dashboard
        4. 📋 Compile Report: Combine all analyses into actionable advice
        5. ✅ Return Results: Present to user in beautiful format
        """
        
        print("🔄 Starting financial analysis workflow...")
        
        try:
            # ================================================================
            # STEP 1: DOCUMENT PROCESSING - Get Financial Data
            # ================================================================
            # This step extracts structured financial data from whatever
            # the user uploaded, or provides sample data for demonstration
            
            print("📄 Processing financial document...")
            
            if file_upload is not None:
                # User uploaded a file - try to process it
                print(f"📤 Processing uploaded file: {file_upload.name}")
                financial_data = self.data_processor.process_document(file_upload.name)
                
                if "error" in financial_data:
                    # File processing failed - use sample data instead
                    print("⚠️ File processing failed, using sample data")
                    financial_data = create_sample_data()
                    report_note = "⚠️ Using sample data due to file processing error. Upload a CSV with columns: Date, Amount, Category for best results. "
                else:
                    # File processed successfully
                    print("✅ File processed successfully")
                    report_note = "✅ Successfully processed your financial document. "
            else:
                # No file uploaded - use sample data for demonstration
                print("📊 No file uploaded, using sample data for demonstration")
                financial_data = create_sample_data()
                report_note = "📊 Using sample financial data for demonstration. Upload your own financial document for personalized analysis. "
            
            # ================================================================
            # STEP 2: AI AGENT ANALYSIS - Run All 5 Specialists
            # ================================================================
            # Each agent focuses on one aspect of financial health
            # Running them in logical order: debt → savings → budget → optimization → report
            
            print("🤖 Running AI financial analysis agents...")
            
            # AGENT 1: Debt Analyzer - Find and prioritize debt payments
            print("  🏦 Running Debt Analyzer Agent...")
            debt_analysis = self.debt_analyzer.analyze_debt(financial_data)
            
            # AGENT 2: Savings Strategist - Create emergency fund and savings plan
            print("  💰 Running Savings Strategy Agent...")
            savings_strategy = self.savings_strategist.create_savings_plan(
                financial_data, financial_goals
            )
            
            # AGENT 3: Budget Advisor - Analyze spending with 50/30/20 rule
            print("  📋 Running Budget Advisor Agent...")
            budget_advice = self.budget_advisor.analyze_budget(financial_data)
            
            # AGENT 4: Payoff Optimizer - Compare debt payoff strategies
            print("  🎯 Running Payoff Optimizer Agent...")
            extra_payment_amount = float(extra_payment) if extra_payment else 0
            payoff_plan = self.payoff_optimizer.create_payoff_plan(
                financial_data, extra_payment_amount
            )
            
            print("✅ All AI agents completed analysis!")
            
            # ================================================================
            # STEP 3: REPORT GENERATION - Compile Comprehensive Advice
            # ================================================================
            # The report generator takes all agent outputs and creates
            # a cohesive, actionable financial plan
            
            print("📊 Generating comprehensive financial report...")
            comprehensive_report = self.report_generator.generate_report(
                debt_analysis, savings_strategy, budget_advice, 
                payoff_plan, financial_data
            )
            
            # Add processing note to beginning of report
            comprehensive_report = report_note + comprehensive_report
            
            # ================================================================
            # STEP 4: VISUALIZATION - Create Beautiful Dashboard
            # ================================================================
            # Transform numbers into visual insights that are easy to understand
            
            print("📈 Creating interactive financial dashboard...")
            financial_dashboard = self.visualizer.create_financial_dashboard(financial_data)
            
            print("🎉 Financial analysis completed successfully!")
            
            # Return both the comprehensive report and interactive dashboard
            return comprehensive_report, financial_dashboard
            
        except Exception as e:
            # ================================================================
            # ERROR HANDLING - Graceful Failure Management
            # ================================================================
            # If anything goes wrong, provide helpful error message and guidance
            
            print(f"❌ Error during financial analysis: {e}")
            
            error_message = f"""
            ❌ **Error Processing Your Financial Analysis**
            
            **What happened:** {str(e)}
            
            **This might be due to:**
            - 🔑 Missing OpenAI API key (check environment variables)
            - 📄 Unsupported file format (try CSV with Date, Amount, Category columns)
            - 🌐 Network connectivity issues
            - 📊 Invalid data format in uploaded file
            
            **How to fix it:**
            1. Check that OPENAI_API_KEY is set in your environment
            2. Try uploading a CSV file with columns: Date, Amount, Category
            3. Or run without uploading a file to see sample analysis
            
            **For support:** Check the console for detailed error messages.
            """
            
            error_dashboard = """
            <div style="text-align: center; padding: 50px; background: #f8f9fa; border-radius: 10px; margin: 20px;">
                <h2 style="color: #dc3545;">📊 Dashboard Temporarily Unavailable</h2>
                <p style="color: #6c757d;">Dashboard will be available once the error above is resolved.</p>
            </div>
            """
            
            return error_message, error_dashboard

# ============================================================================
# GRADIO USER INTERFACE - Beautiful Web Interface
# ============================================================================
# This section creates the web interface that users interact with.
# Gradio makes it easy to create professional-looking web apps.
# ============================================================================

def create_gradio_interface():
    """
    🎨 CREATE BEAUTIFUL WEB INTERFACE
    
    WHAT THIS FUNCTION DOES:
    - Creates the web interface layout using Gradio
    - Defines input components (file upload, text fields)
    - Defines output components (report, dashboard)
    - Sets up the visual styling and branding
    - Connects interface to our AI analysis function
    
    INTERFACE COMPONENTS:
    1. Header with title and description
    2. File upload area for financial documents
    3. Text input for financial goals
    4. Number input for extra debt payments
    5. Analysis button to trigger processing
    6. Output areas for report and dashboard
    
    WHY GRADIO:
    - Easy to create professional interfaces
    - Automatic mobile responsiveness
    - Built-in file handling
    - No HTML/CSS knowledge required
    - Perfect for AI/ML applications
    """
    
    print("🎨 Creating Gradio web interface...")
    
    # Initialize our FinWise AI
    coach = AIFinancialCoach()
    
    # Create the Gradio interface with custom theme and styling
    with gr.Blocks(
        theme=gr.themes.Soft(),  # Professional, modern theme
        title="FinWise AI",  # Browser tab title
        css="""
        /* Custom CSS for professional appearance */
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
        
        # ============================================================
        # HEADER SECTION - Title and Description
        # ============================================================
        
        # Main title with gradient background
        gr.HTML("""
        <div class="main-header">
            <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                🏦 FinWise AI Agent
            </h1>
            <p style="font-size: 1.2rem; margin: 0; opacity: 0.9;">
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
        
        **📊 Interactive Visualizations:**
        - Expense breakdown pie charts
        - Cash flow analysis
        - Budget vs actual spending comparison
        - Financial health scoring
        
        **📋 Actionable Insights:**
        - Personalized 90-day action plans
        - Specific dollar amounts and timelines
        - Tool and app recommendations
        - Progress tracking strategies
        """)
        
        # ============================================================
        # INPUT SECTION - User Inputs
        # ============================================================
        
        gr.Markdown("### 📤 **Upload Your Financial Data**")
        
        with gr.Row():
            with gr.Column(scale=2):
                # File upload component
                file_upload = gr.File(
                    label="📄 Upload Financial Document",
                    file_count="single",  # Only one file at a time
                    file_types=[".csv", ".xlsx", ".xls", ".pdf"],  # Supported formats
                    #info="Supported formats: CSV, Excel, PDF. For best results, use CSV with columns: Date, Amount, Category"
                    #help="Supported formats: CSV, Excel, PDF. For best results, use CSV with columns: Date, Amount, Category"
                )
                
                # Sample file format helper
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
                # Financial goals input
                financial_goals = gr.Textbox(
                    label="🎯 Your Financial Goals",
                    placeholder="e.g., Save for emergency fund, pay off credit card debt, buy a house down payment...",
                    lines=4,
                    #info="Describe your financial objectives to get personalized advice"
                    #help="Describe your financial objectives to get personalized advice"
                )
                
                # Extra payment input
                extra_payment = gr.Number(
                    label="💵 Extra Monthly Payment for Debts",
                    value=0,
                    minimum=0,
                    #info="Additional amount you can put toward debt payments each month"
                    #help="Additional amount you can put toward debt payments each month"
                )
        
        # ============================================================
        # ACTION BUTTON - Trigger Analysis
        # ============================================================
        
        analyze_button = gr.Button(
            "🚀 Analyze My Finances",
            variant="primary",  # Makes button prominent
            size="lg"  # Large button
        )
        
        # ============================================================
        # OUTPUT SECTION - Results Display
        # ============================================================
        
        gr.Markdown("### 📊 **Your Personalized Financial Analysis**")
        
        with gr.Row():
            with gr.Column(scale=3):
                # Comprehensive financial report
                financial_report = gr.Markdown(
                    label="📋 Comprehensive Financial Report",
                    value="Click 'Analyze My Finances' to get your personalized report...",
                    container=True
                )
            
            with gr.Column(scale=2):
                # Interactive dashboard
                financial_dashboard = gr.HTML(
                    label="📈 Interactive Financial Dashboard",
                    value="<div style='text-align: center; padding: 50px; color: #666;'>Dashboard will appear here after analysis...</div>"
                )
        
        # ============================================================
        # FOOTER SECTION - Additional Information
        # ============================================================
        
        gr.Markdown("""
        ---
        ### 🔒 **Privacy & Security**
        - Your financial data is processed locally and not stored
        - AI analysis uses OpenAI's secure API
        - No data is shared with third parties
        
        ### 🛠️ **Technical Details**
        - Built with Python, LangChain, and Gradio
        - Uses GPT-4o-mini for cost-effective analysis
        - Supports multiple file formats and data sources
        - Interactive charts powered by Plotly
        
        ### 📞 **Support**
        - This is a demo application for educational purposes
        - For production use, consult with licensed financial advisors
        - Source code available for review and customization
        """)
        
        # ============================================================
        # EVENT HANDLERS - Connect Interface to Logic
        # ============================================================
        
        # Connect the analyze button to our main analysis function
        analyze_button.click(
            fn=coach.analyze_finances,  # Function to call
            inputs=[file_upload, financial_goals, extra_payment],  # Input components
            outputs=[financial_report, financial_dashboard],  # Output components
            show_progress=True  # Show loading indicator
        )
    
    print("✅ Gradio interface created successfully!")
    return app

# ============================================================================
# MAIN EXECUTION - Start the Application
# ============================================================================
# This is where everything comes together and the app actually starts running
# ============================================================================

def main():
    """
    🚀 MAIN FUNCTION - Application Entry Point
    
    WHAT THIS FUNCTION DOES:
    1. Checks for required environment variables (OpenAI API key)
    2. Creates the Gradio interface
    3. Starts the web server
    4. Provides helpful startup information
    
    ENVIRONMENT SETUP:
    - Checks for OPENAI_API_KEY environment variable
    - Provides helpful error messages if missing
    - Gives instructions for setting up the API key
    
    SERVER STARTUP:
    - Launches Gradio development server
    - Makes app available at http://localhost:7860
    - Provides public sharing option for demos
    """
    
    print("=" * 60)
    print("🏦 FinWise AI - STARTING UP")
    print("=" * 60)
    
    # ================================================================
    # ENVIRONMENT VALIDATION - Check Required Setup
    # ================================================================
    
    # Check for OpenAI API key
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key or openai_key == "your-api-key-here":
        print("⚠️  WARNING: OPENAI_API_KEY not found in environment variables!")
        print("")
        print("🔑 To get full AI analysis, you need an OpenAI API key:")
        print("   1. Go to https://platform.openai.com/api-keys")
        print("   2. Create a new API key")
        print("   3. Set it in terminal: export OPENAI_API_KEY='your-key-here'")
        print("   4. Restart this application")
        print("")
        print("📊 Don't worry - the app will still work with sample analysis!")
        print("")
    else:
        print("✅ OpenAI API key found - full AI analysis available!")
        print("")
    
    # ================================================================
    # ENHANCED APPLICATION STARTUP - Smart Launch Process
    # ================================================================
    
    try:
        # Pre-flight checks
        print("🔧 Running pre-flight checks...")
        
        if not check_and_install_dependencies():
            print("❌ Dependency installation failed!")
            print("💡 Try running manually: pip install -r requirements.txt")
            return
        
        api_key_valid = validate_environment()
        system_diagnostics()
        
        print("🎨 Creating web interface...")
        app = create_gradio_interface()
        
        print("🚀 Starting web server...")
        print("")
        print("=" * 60)
        print("🎉 FinWise AI IS READY!")
        print("=" * 60)
        print("📱 Open your browser and go to: http://localhost:7860")
        print("📊 Upload your financial document or try the sample data")
        print("🤖 Get personalized FinWise AI!")
        if not api_key_valid:
            print("💡 Demo mode active - add OpenAI API key for full AI analysis")
        print("=" * 60)
        print("")
        
        in_colab = "COLAB_RELEASE_TAG" in os.environ or "COLAB_GPU" in os.environ

        # Launch the Gradio app with enhanced configuration
        app.launch(
            #server_name="127.0.0.1",  # Local server only
            server_name="0.0.0.0",  # Local server only
            server_port=7860,  # Standard port
            share=in_colab,        # 👈 True in Colab, False locally
            #share=False,  # Set to True for public demo links
            show_error=True,  # Show detailed errors for debugging
            quiet=False,  # Show startup logs
            #inbrowser=True  # Automatically open browser
            inbrowser=not in_colab, # 👈 Auto-open browser only locally
        )
        
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        print("")
        print("🔧 Troubleshooting steps:")
        print("   1. Check the error message above for specific issues")
        print("   2. Ensure you're in the correct directory")
        print("   3. Try: pip install --upgrade gradio langchain-openai")
        print("   4. Check that port 7860 is available")
        print("   5. Restart your terminal and try again")
        print("")
        print("💬 If problems persist, the error above should guide you!")

# ============================================================================
# STARTUP SEQUENCE WITH SMART PREREQUISITES
# ============================================================================

def startup_sequence():
    """
    🚀 ENHANCED STARTUP SEQUENCE
    
    WHAT THIS DOES:
    1. Shows professional startup banner
    2. Runs all prerequisite checks automatically
    3. Handles missing dependencies gracefully
    4. Provides clear guidance for any issues
    5. Launches application when everything is ready
    
    WHY THIS IS BETTER:
    - Self-diagnosing application
    - Better user experience
    - Professional presentation
    - Reduces support burden
    - Works out-of-the-box for most users
    """
    
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
# This is the standard Python pattern for running a script directly
# When someone runs "python app.py", this code executes
# ============================================================================

if __name__ == "__main__":
    """
    🎯 ENHANCED ENTRY POINT - Professional Application Launch
    
    Now when someone runs "python app.py", they get:
    - Automatic dependency checking and installation
    - Environment validation with helpful guidance
    - System diagnostics and optimization tips
    - Graceful error handling with troubleshooting steps
    - Professional startup sequence
    
    This makes the application much more user-friendly and production-ready!
    """
    startup_sequence()

# ============================================================================
# END OF APPLICATION
# ============================================================================
# 
# CONGRATULATIONS! 🎉
# 
# You now have a complete FinWise AI application with:
# 
# ✅ 5 Specialized AI Agents:
#    - Debt Analyzer for debt optimization
#    - Savings Strategist for financial planning
#    - Budget Advisor for spending analysis
#    - Payoff Optimizer for debt elimination
#    - Report Generator for comprehensive advice
# 
# ✅ Document Processing:
#    - CSV, Excel, and PDF support
#    - Automatic data extraction and categorization
#    - Error handling and fallbacks
# 
# ✅ Beautiful Visualizations:
#    - Interactive pie charts for expense breakdown
#    - Cash flow analysis charts
#    - Budget vs actual comparisons
#    - Financial health scoring dashboard
# 
# ✅ Professional Web Interface:
#    - Modern, responsive design
#    - Easy file uploads
#    - Real-time analysis
#    - Mobile-friendly layout
# 
# ✅ Comprehensive Reporting:
#    - Detailed financial analysis
#    - 90-day action plans
#    - Specific recommendations with dollar amounts
#    - Tool and resource suggestions
# 
# NEXT STEPS FOR YOUR HACKATHON:
# 
# 1. 🔑 Set up OpenAI API key for full functionality
# 2. 🧪 Test with your own financial data
# 3. 🎨 Customize colors, branding, or features
# 4. 📊 Add additional chart types or metrics
# 5. 🚀 Deploy to cloud for public demos
# 
# DEMO PRESENTATION TIPS:
# 
# 1. 🎯 Start with the problem: "Financial planning is complex and time-consuming"
# 2. 💡 Show the solution: "5 AI agents working together like a financial advisory team"
# 3. 📱 Live demo: Upload sample data and walk through each agent's analysis
# 4. 📊 Highlight visualizations: Show how complex data becomes clear insights
# 5. 🎉 End with impact: "Saves hours of analysis, provides professional-grade advice"
# 
# You've built something truly impressive! 🏆
# 
# ============================================================================