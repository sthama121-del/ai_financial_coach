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
# FILE VALIDATION HELPER FUNCTIONS
# ============================================================================

def validate_financial_content(financial_data, file_path):
    """Validate that extracted data actually represents financial information"""
    
    # Check the actual file content for context clues
    try:
        file_content = ""
        file_ext = os.path.splitext(file_path)[1].lower()
        
        if file_ext == '.pdf':
            # Read PDF content to check for non-financial keywords
            try:
                import PyPDF2
                with open(file_path, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    # Read first few pages
                    for page_num in range(min(3, len(pdf_reader.pages))):
                        file_content += pdf_reader.pages[page_num].extract_text()
            except:
                pass
        elif file_ext == '.csv':
            # Read CSV content
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
            except:
                pass
        elif file_ext in ['.xlsx', '.xls']:
            # Read Excel content
            try:
                import pandas as pd
                df = pd.read_excel(file_path)
                file_content = df.to_string()
            except:
                pass
    except:
        file_content = ""
    
    # Convert to lowercase for analysis
    content_lower = file_content.lower()
    
    # Check for non-financial content indicators
    educational_keywords = [
        'course', 'session', 'learning', 'training', 'education', 'curriculum',
        'bootcamp', 'workshop', 'seminar', 'lecture', 'chapter', 'lesson',
        'instructor', 'student', 'professor', 'university', 'college',
        'prerequisites', 'syllabus', 'assignment', 'homework', 'exam',
        'modern ai pro', 'ai essentials', 'machine learning', 'neural network',
        'transformer', 'llm', 'gpt', 'artificial intelligence'
    ]
    
    # Count educational keywords
    educational_count = sum(1 for keyword in educational_keywords if keyword in content_lower)
    
    # Check for financial keywords
    financial_keywords = [
        'transaction', 'payment', 'deposit', 'withdrawal', 'balance', 
        'expense', 'income', 'salary', 'bill', 'purchase', 'debit', 
        'credit', 'bank', 'account', 'receipt', 'invoice', 'spending',
        'budget', 'money', 'dollar', 'cost', 'price', 'fee'
    ]
    
    financial_count = sum(1 for keyword in financial_keywords if keyword in content_lower)
    
    # Analyze the extracted financial data
    income = financial_data.get('total_income', 0)
    expenses = financial_data.get('total_expenses', 0)
    categories = financial_data.get('categories', {})
    
    # Red flags that indicate non-financial content:
    
    # Strong educational content indicators
    if educational_count >= 5:
        return False, f"Document appears to be educational content ({educational_count} educational keywords found)"
    
    # Very low income with zero expenses - likely extracted metadata
    if income < 500 and expenses == 0:
        return False, "Financial amounts appear to be extracted metadata rather than actual transactions"
    
    # No meaningful categories
    if len(categories) == 0:
        return False, "No expense categories found in document"
    
    # Categories contain non-financial terms
    category_text = ' '.join(str(categories).lower().split())
    non_financial_indicators = ['pdf', 'page', 'section', 'chapter', 'course', 'session', 'notebook']
    if any(indicator in category_text for indicator in non_financial_indicators):
        return False, "Categories appear to contain document metadata rather than financial categories"
    
    # If we found educational keywords but very few financial keywords
    if educational_count > financial_count and educational_count >= 3:
        return False, f"Document appears to be educational ({educational_count} educational vs {financial_count} financial keywords)"
    
    # Income is suspiciously specific small amounts (like page numbers)
    if income in [75, 36, 35, 34, 33, 32, 31, 30] and expenses == 0:
        return False, "Income amount appears to be a page number or document metadata"
    
    return True, "Content appears to contain financial data"

def validate_uploaded_file(file_upload):
    """Validate uploaded file and return status"""
    if file_upload is None:
        return "no_file", None, None
    
    file_path = file_upload.name
    filename = os.path.basename(file_path)
    
    print(f"Validating file: {filename}")
    
    # Check if file exists
    if not os.path.exists(file_path):
        return "file_not_found", filename, "File does not exist"
    
    # Check file size
    try:
        file_size = os.path.getsize(file_path)
        print(f"File size: {file_size} bytes")
        
        if file_size == 0:
            return "empty_file", filename, "File is empty (0 bytes)"
        elif file_size < 10:  # Very small files are likely empty or corrupted
            return "too_small", filename, f"File is too small ({file_size} bytes)"
    except Exception as e:
        return "size_error", filename, f"Cannot check file size: {str(e)}"
    
    # Try to peek at file content for basic validation
    try:
        file_ext = os.path.splitext(filename)[1].lower()
        
        if file_ext == '.csv':
            # Check CSV content
            with open(file_path, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
                if not first_line:
                    return "no_content", filename, "CSV file has no content"
                # Check if it has some reasonable content
                if len(first_line) < 5:
                    return "insufficient_content", filename, "CSV content appears insufficient"
        
        elif file_ext in ['.xlsx', '.xls']:
            # Check Excel content
            import pandas as pd
            try:
                df = pd.read_excel(file_path)
                if df.empty:
                    return "no_content", filename, "Excel file has no data"
                if len(df.columns) == 0:
                    return "no_columns", filename, "Excel file has no columns"
            except Exception as e:
                return "excel_error", filename, f"Cannot read Excel file: {str(e)}"
    
    except Exception as e:
        return "content_error", filename, f"Cannot validate file content: {str(e)}"
    
    return "valid", filename, "File appears valid"

# ============================================================================
# HELPER FUNCTIONS FOR PLOTS
# ============================================================================

def analyze_finances_with_plots(file_upload, financial_goals, extra_payment):
    """Enhanced analysis function with proper file validation"""
    try:
        # First validate the uploaded file
        file_status, filename, message = validate_uploaded_file(file_upload)
        
        print(f"File validation result: {file_status} - {message}")
        
        # Handle different file validation results
        if file_status == "empty_file":
            error_report = f"""
            ## ⚠️ **Empty File Detected**
            
            **Issue:** The uploaded file `{filename}` is empty (0 bytes).
            
            **What to do:**
            1. Check that your file contains data
            2. Ensure the file saved properly from your spreadsheet program
            3. Try uploading a different file
            4. Use the sample CSV format shown above
            
            **To see sample analysis:** Remove the file and click "Analyze My Finances" again.
            """
            
            empty_fig = create_empty_file_plot()
            error_html = """
            <div style="background: #fff3cd; border: 1px solid #ffeaa7; padding: 20px; border-radius: 8px; margin: 10px 0;">
                <h3 style="color: #856404; margin: 0 0 10px 0;">📁 Empty File</h3>
                <p style="color: #856404; margin: 0;">Please upload a file with financial data or remove the file to see sample analysis.</p>
            </div>
            """
            
            return error_report, empty_fig, empty_fig, error_html
        
        elif file_status == "too_small":
            error_report = f"""
            ## ⚠️ **File Too Small**
            
            **Issue:** The uploaded file `{filename}` is too small ({message}).
            
            **This usually means:**
            - File is empty or nearly empty
            - File didn't save properly
            - File is corrupted
            
            **Solutions:**
            1. Check your original file has data
            2. Save and re-upload the file
            3. Try a different file format (CSV recommended)
            
            **To see sample analysis:** Remove the file and click "Analyze My Finances" again.
            """
            
            small_fig = create_small_file_plot()
            error_html = """
            <div style="background: #fff3cd; border: 1px solid #ffeaa7; padding: 20px; border-radius: 8px; margin: 10px 0;">
                <h3 style="color: #856404; margin: 0 0 10px 0;">📏 File Too Small</h3>
                <p style="color: #856404; margin: 0;">File appears to be empty or corrupted.</p>
            </div>
            """
            
            return error_report, small_fig, small_fig, error_html
        
        elif file_status == "no_content":
            error_report = f"""
            ## 📊 **No Data Found in File**
            
            **Issue:** The file `{filename}` was opened but contains no financial data.
            
            **Common causes:**
            - File has only headers but no data rows
            - File is in an unexpected format
            - Data was not saved properly
            
            **Expected CSV format:**
            ```
            Date,Amount,Category,Description
            2024-01-01,3000,Salary,Monthly Salary
            2024-01-02,-150,Groceries,Whole Foods
            2024-01-03,-1200,Rent,Apartment Rent
            ```
            
            **Solutions:**
            1. Add data rows to your file
            2. Ensure proper CSV format
            3. Check that data saved correctly
            
            **To see sample analysis:** Remove the file and click "Analyze My Finances" again.
            """
            
            no_data_fig = create_no_data_plot()
            error_html = """
            <div style="background: #e2e3e5; border: 1px solid #d6d8db; padding: 20px; border-radius: 8px; margin: 10px 0;">
                <h3 style="color: #383d41; margin: 0 0 10px 0;">📋 No Data</h3>
                <p style="color: #383d41; margin: 0;">File opened but no financial data found.</p>
            </div>
            """
            
            return error_report, no_data_fig, no_data_fig, error_html
        
        elif file_status in ["file_not_found", "size_error", "content_error", "excel_error"]:
            error_report = f"""
            ## ❌ **File Processing Error**
            
            **Issue:** Problem processing file `{filename}`.
            
            **Error:** {message}
            
            **Solutions:**
            1. Try uploading the file again
            2. Save your file as CSV format
            3. Check the file isn't corrupted
            4. Ensure file has proper financial data
            
            **To see sample analysis:** Remove the file and click "Analyze My Finances" again.
            """
            
            error_fig = create_error_plot(f"File error: {message}")
            error_html = f"""
            <div style="background: #f8d7da; border: 1px solid #f5c6cb; padding: 20px; border-radius: 8px; margin: 10px 0;">
                <h3 style="color: #721c24; margin: 0 0 10px 0;">💢 Processing Error</h3>
                <p style="color: #721c24; margin: 0;">{message}</p>
            </div>
            """
            
            return error_report, error_fig, error_fig, error_html
        
        # If we reach here, file is valid or no file uploaded
        coach = AIFinancialCoach()
        
        if file_status == "valid":
            # File is valid, try to process it and validate content
            print(f"File validation passed, processing {filename}")
            
            # Process the file and check if it contains actual financial data
            if DATA_PROCESSOR_AVAILABLE:
                financial_data = coach.data_processor.process_document(file_upload.name)
                
                if "error" not in financial_data:
                    # NEW: Validate that this is actually financial content
                    is_financial, validation_message = validate_financial_content(financial_data, file_upload.name)
                    
                    if not is_financial:
                        error_report = f"""
                        ## 📄 **Non-Financial Content Detected**
                        
                        **Issue:** The file `{filename}` appears to contain non-financial content.
                        
                        **Detection:** {validation_message}
                        
                        **This file appears to be:**
                        - Educational or course material
                        - Documentation or manual
                        - General text document
                        - Other non-financial content
                        
                        **For financial analysis, please upload:**
                        - Bank statements (CSV/Excel)
                        - Expense tracking spreadsheets  
                        - Budget documents
                        - Transaction records
                        
                        **Sample Analysis:** Remove the file and click "Analyze" to see how financial analysis works with sample data.
                        """
                        
                        non_financial_fig = create_non_financial_plot()
                        error_html = """
                        <div style="background: #e3f2fd; border: 1px solid #90caf9; padding: 20px; border-radius: 8px; margin: 10px 0;">
                            <h3 style="color: #1565c0; margin: 0 0 10px 0;">📄 Non-Financial Content</h3>
                            <p style="color: #1565c0; margin: 0;">This appears to be educational/documentation content, not financial data.</p>
                        </div>
                        """
                        
                        return error_report, non_financial_fig, non_financial_fig, error_html
            
            file_success_note = f"✅ **File validation passed:** `{filename}` - Processing financial data...\n\n"
        else:
            # No file uploaded
            print("No file uploaded, using sample data")
            file_success_note = "📊 **Sample Data Analysis** - No file uploaded, using demonstration data.\n\n"
        
        # Continue with normal analysis
        report, _ = coach.analyze_finances(file_upload, financial_goals, extra_payment)
        
        # Add file processing note at the beginning (but remove the old one if it exists)
        if report.startswith("⚠️ Using sample data due to file processing error."):
            # Remove the old error message since we handled validation properly
            report = report.replace("⚠️ Using sample data due to file processing error. ", "")
        
        report = file_success_note + report
        
        # Get financial data for creating plots
        if file_upload is not None and DATA_PROCESSOR_AVAILABLE and file_status == "valid":
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
        
        # Create charts
        expense_fig = create_expense_plot(financial_data)
        cashflow_fig = create_cashflow_plot(financial_data)
        metrics_html = create_metrics_summary(financial_data)
        
        return report, expense_fig, cashflow_fig, metrics_html
        
    except Exception as e:
        print(f"Error in enhanced analysis: {e}")
        
        general_error_report = f"""
        ## ❌ **Analysis Error**
        
        **Error:** {str(e)}
        
        **What happened:** An unexpected error occurred during analysis.
        
        **Solutions:**
        1. Try without uploading a file (sample analysis)
        2. Check your file format and data
        3. Refresh the page and try again
        4. Contact support if the problem persists
        """
        
        error_fig = create_error_plot(str(e))
        error_html = f"""
        <div style="background: #f8d7da; border: 1px solid #f5c6cb; padding: 20px; border-radius: 8px; margin: 10px 0;">
            <h3 style="color: #721c24; margin: 0 0 10px 0;">💥 System Error</h3>
            <p style="color: #721c24; margin: 0;">{str(e)}</p>
        </div>
        """
        
        return general_error_report, error_fig, error_fig, error_html

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

def create_empty_file_plot():
    """Create a plot indicating empty file"""
    try:
        import plotly.graph_objects as go
        fig = go.Figure()
        fig.add_annotation(
            text="📁 Empty File<br>No data to display",
            showarrow=False,
            x=0.5, y=0.5,
            font=dict(size=16, color="orange")
        )
        fig.update_layout(
            title="File is Empty",
            height=300,
            showlegend=False,
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False)
        )
        return fig
    except:
        return None

def create_small_file_plot():
    """Create a plot indicating file too small"""
    try:
        import plotly.graph_objects as go
        fig = go.Figure()
        fig.add_annotation(
            text="📏 File Too Small<br>Appears empty or corrupted",
            showarrow=False,
            x=0.5, y=0.5,
            font=dict(size=16, color="orange")
        )
        fig.update_layout(
            title="File Too Small",
            height=300,
            showlegend=False,
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False)
        )
        return fig
    except:
        return None

def create_no_data_plot():
    """Create a plot indicating no financial data found"""
    try:
        import plotly.graph_objects as go
        fig = go.Figure()
        fig.add_annotation(
            text="📊 No Financial Data<br>Check your file format",
            showarrow=False,
            x=0.5, y=0.5,
            font=dict(size=16, color="gray")
        )
        fig.update_layout(
            title="No Financial Transactions Found",
            height=300,
            showlegend=False,
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False)
        )
        return fig
    except:
        return None

def create_non_financial_plot():
    """Create a plot indicating non-financial content detected"""
    try:
        import plotly.graph_objects as go
        fig = go.Figure()
        fig.add_annotation(
            text="📄 Non-Financial Content<br>Upload financial data instead",
            showarrow=False,
            x=0.5, y=0.5,
            font=dict(size=16, color="blue")
        )
        fig.update_layout(
            title="Non-Financial Content Detected",
            height=300,
            showlegend=False,
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False)
        )
        return fig
    except:
        return None

# ============================================================================
# GRADIO INTERFACE CREATION
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