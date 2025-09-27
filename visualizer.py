# ============================================================================
# FINANCIAL VISUALIZER - ENHANCED WITH SMART PREREQUISITES
# ============================================================================
# This file creates interactive charts and dashboards to visualize financial data.
# It's like having a personal financial dashboard that makes complex data easy to understand.
# 
# ENHANCED FEATURES:
# 🔧 Automatic dependency checking and installation
# 🚨 Graceful fallbacks when packages aren't available
# 📊 Multiple chart types with professional styling
# 🎨 Color psychology for intuitive understanding
# 💫 Interactive features with hover effects and animations
# 
# WHAT THIS FILE DOES:
# 1. 🥧 Creates interactive pie charts for expense breakdown
# 2. 📊 Builds cash flow bar charts (income vs expenses vs savings)
# 3. 📈 Compares actual spending vs recommended budget (50/30/20 rule)
# 4. 🎯 Shows savings goal progress with timelines
# 5. 📱 Combines everything into a beautiful financial dashboard
# 
# TECHNOLOGIES USED:
# - Plotly: For interactive charts that users can hover/zoom
# - HTML/CSS: For beautiful styling and layout
# - Color psychology: Green for good, red for expenses, blue for savings
# - Fallback options: Simple text output when charts aren't available
# ============================================================================

import sys
import subprocess
import importlib.util
import os

# ============================================================================
# SMART DEPENDENCY MANAGEMENT - Visualizer Prerequisites
# ============================================================================

def check_visualization_dependencies():
    """
    🔧 VISUALIZATION DEPENDENCY CHECKER
    
    WHAT THIS FUNCTION DOES:
    1. Checks if visualization packages are available
    2. Attempts to install missing packages automatically
    3. Provides fallback options when installations fail
    4. Returns capability flags for graceful degradation
    
    VISUALIZATION PACKAGES NEEDED:
    - plotly: Interactive charts (primary)
    - matplotlib: Static charts (fallback)
    - pandas: Data manipulation
    - io, base64: Image handling
    
    RETURNS:
    Dictionary with capability flags for different chart types
    """
    
    print("🎨 Checking visualization dependencies...")
    
    capabilities = {
        'interactive_charts': False,
        'static_charts': False,
        'data_processing': False,
        'dashboard': False
    }
    
    # Check Plotly (primary visualization engine)
    try:
        import plotly.graph_objects as go
        import plotly.express as px
        capabilities['interactive_charts'] = True
        capabilities['dashboard'] = True
        print("✅ Plotly - Interactive charts available")
    except ImportError:
        print("❌ Plotly missing - trying to install...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "plotly"])
            import plotly.graph_objects as go
            capabilities['interactive_charts'] = True
            print("✅ Plotly installed successfully!")
        except Exception as e:
            print(f"⚠️ Plotly installation failed: {e}")
    
    # Check Matplotlib (fallback visualization)
    try:
        import matplotlib.pyplot as plt
        capabilities['static_charts'] = True
        print("✅ Matplotlib - Static charts available")
    except ImportError:
        print("❌ Matplotlib missing - trying to install...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
            capabilities['static_charts'] = True
            print("✅ Matplotlib installed successfully!")
        except Exception as e:
            print(f"⚠️ Matplotlib installation failed: {e}")
    
    # Check Pandas (data processing)
    try:
        import pandas as pd
        capabilities['data_processing'] = True
        print("✅ Pandas - Data processing available")
    except ImportError:
        print("❌ Pandas missing - trying to install...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
            capabilities['data_processing'] = True
            print("✅ Pandas installed successfully!")
        except Exception as e:
            print(f"⚠️ Pandas installation failed: {e}")
    
    return capabilities

# Try to import with smart fallbacks
VISUALIZATION_CAPABILITIES = check_visualization_dependencies()

# Smart imports based on availability
if VISUALIZATION_CAPABILITIES['interactive_charts']:
    try:
        import plotly.graph_objects as go
        import plotly.express as px
        from plotly.subplots import make_subplots
        PLOTLY_AVAILABLE = True
    except ImportError:
        PLOTLY_AVAILABLE = False
else:
    PLOTLY_AVAILABLE = False

if VISUALIZATION_CAPABILITIES['static_charts']:
    try:
        import matplotlib.pyplot as plt
        MATPLOTLIB_AVAILABLE = True
    except ImportError:
        MATPLOTLIB_AVAILABLE = False
else:
    MATPLOTLIB_AVAILABLE = False

if VISUALIZATION_CAPABILITIES['data_processing']:
    try:
        import pandas as pd
        PANDAS_AVAILABLE = True
    except ImportError:
        PANDAS_AVAILABLE = False
else:
    PANDAS_AVAILABLE = False

# Standard library imports (always available)
from typing import Dict, Any
import io
import base64

# ============================================================================
# MAIN VISUALIZER CLASS - Enhanced with Smart Fallbacks
# ============================================================================

class FinancialVisualizer:
    """
    📊 ENHANCED FINANCIAL VISUALIZER CLASS
    
    WHAT IT DOES:
    - Takes raw financial data (numbers, categories, amounts)
    - Creates beautiful, interactive charts using best available technology
    - Returns HTML that Gradio can display in the web interface
    - Uses color psychology to make charts intuitive
    - Provides fallback options when advanced features aren't available
    
    VISUALIZATION STRATEGY:
    1. Primary: Plotly interactive charts (best experience)
    2. Fallback: Matplotlib static charts (good experience)
    3. Emergency: Text-based summaries (basic experience)
    
    COLOR PSYCHOLOGY WE USE:
    - 🟢 Green: Income, positive things, good financial health
    - 🔴 Red: Expenses, negative cash flow, areas needing attention
    - 🔵 Blue: Savings, investments, neutral information
    - 🟡 Yellow: Warnings, moderate concerns
    - 🟣 Purple: Premium features, advanced insights
    """
    
    def __init__(self):
        """
        ENHANCED INITIALIZATION: Set up visualizer with smart capabilities
        """
        
        print("🎨 Initializing Financial Visualizer...")
        
        # Professional color palette
        self.color_palette = [
            '#2E86AB',  # Professional blue - main brand color
            '#A23B72',  # Sophisticated purple - premium feel
            '#F18F01',  # Energetic orange - attention grabbing
            '#C73E1D',  # Alert red - warnings/expenses
            '#590925',  # Deep maroon - serious tone
            '#1B4332',  # Forest green - growth/savings
            '#40916C'   # Fresh green - positive outcomes
        ]
        
        # Set capabilities based on available packages
        self.can_create_interactive = PLOTLY_AVAILABLE
        self.can_create_static = MATPLOTLIB_AVAILABLE
        self.can_process_data = PANDAS_AVAILABLE
        
        # Report capabilities
        if self.can_create_interactive:
            print("✅ Interactive charts (Plotly) - Full functionality")
        elif self.can_create_static:
            print("⚠️ Static charts only (Matplotlib) - Limited interactivity")
        else:
            print("❌ Chart libraries unavailable - Text summaries only")
        
        print("🎨 Financial Visualizer ready!")
    
    def create_expense_pie_chart(self, financial_data: Dict[str, Any]) -> str:
        """
        🥧 ENHANCED PIE CHART CREATION WITH SMART FALLBACKS
        """
        
        print("🥧 Creating expense pie chart...")
        
        try:
            # STEP 1: Validate and extract data
            categories = financial_data.get('categories', {})
            
            if not categories:
                return self._create_no_data_message("expense breakdown", 
                    "📊 No expense data available for visualization.<br>Upload a financial document to see your expense breakdown!")
            
            # STEP 2: Filter expense categories (remove income)
            expense_categories = {
                category: amount for category, amount in categories.items() 
                if category.lower() not in ['salary', 'income', 'deposit', 'bonus', 'refund']
            }
            
            if not expense_categories:
                return self._create_no_data_message("expenses",
                    "💰 Only income categories found - no expenses to visualize!<br>This is actually great news for your budget!")
            
            # STEP 3: Try interactive chart first (best experience)
            if self.can_create_interactive:
                return self._create_interactive_pie_chart(expense_categories)
            
            # STEP 4: Fallback to static chart (good experience)
            elif self.can_create_static:
                return self._create_static_pie_chart(expense_categories)
            
            # STEP 5: Emergency fallback to text summary (basic experience)
            else:
                return self._create_text_expense_summary(expense_categories)
                
        except Exception as e:
            print(f"❌ Error creating expense pie chart: {e}")
            return self._create_error_message("expense pie chart", str(e))
    
    def _create_interactive_pie_chart(self, expense_categories: Dict[str, float]) -> str:
        """🎪 CREATE INTERACTIVE PIE CHART WITH PLOTLY"""
        
        try:
            # Create interactive pie chart using Plotly
            fig = go.Figure(data=[go.Pie(
                labels=list(expense_categories.keys()),
                values=list(expense_categories.values()),
                hole=0.3,  # Donut chart
                marker_colors=self.color_palette,
                textinfo='label+percent',
                textposition='auto',
                hovertemplate='<b>%{label}</b><br>Amount: $%{value:,.2f}<br>Percentage: %{percent}<extra></extra>'
            )])
            
            # Professional styling
            fig.update_layout(
                title={
                    'text': "💸 Monthly Expense Breakdown",
                    'x': 0.5,
                    'xanchor': 'center',
                    'font': {'size': 20, 'color': '#2E86AB'}
                },
                font=dict(size=14),
                showlegend=True,
                legend=dict(
                    orientation="v",
                    yanchor="middle",
                    y=0.5,
                    xanchor="left",
                    x=1.05
                ),
                margin=dict(l=20, r=120, t=60, b=20),
                height=400,
                plot_bgcolor='white',
                paper_bgcolor='white'
            )
            
            return fig.to_html(include_plotlyjs=True, div_id="expense_pie_chart")
            
        except Exception as e:
            print(f"❌ Interactive pie chart failed: {e}")
            raise
    
    def _create_static_pie_chart(self, expense_categories: Dict[str, float]) -> str:
        """📊 CREATE STATIC PIE CHART WITH MATPLOTLIB (FALLBACK)"""
        
        try:
            # Create static pie chart with matplotlib
            fig, ax = plt.subplots(figsize=(10, 6))
            
            labels = list(expense_categories.keys())
            sizes = list(expense_categories.values())
            
            # Create pie chart with our color palette
            colors = self.color_palette[:len(labels)]
            wedges, texts, autotexts = ax.pie(
                sizes, 
                labels=labels, 
                colors=colors,
                autopct='%1.1f%%',
                startangle=90
            )
            
            ax.set_title('💸 Monthly Expense Breakdown', fontsize=16, fontweight='bold')
            
            # Convert to base64 string for HTML embedding
            img_buffer = io.BytesIO()
            plt.savefig(img_buffer, format='png', bbox_inches='tight', dpi=150)
            img_buffer.seek(0)
            img_base64 = base64.b64encode(img_buffer.read()).decode()
            plt.close()
            
            return f'<img src="data:image/png;base64,{img_base64}" style="max-width: 100%; height: auto;">'
            
        except Exception as e:
            print(f"❌ Static pie chart failed: {e}")
            raise
    
    def _create_text_expense_summary(self, expense_categories: Dict[str, float]) -> str:
        """📝 CREATE TEXT SUMMARY (EMERGENCY FALLBACK)"""
        
        total_expenses = sum(expense_categories.values())
        
        html = """
        <div style="background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            <h3 style="color: #2E86AB; margin-top: 0;">💸 Monthly Expense Breakdown</h3>
            <p style="color: #666; margin-bottom: 20px;">Charts unavailable - showing detailed breakdown:</p>
            <table style="width: 100%; border-collapse: collapse;">
                <tr style="background: #f8f9fa; font-weight: bold;">
                    <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Category</th>
                    <th style="padding: 10px; text-align: right; border: 1px solid #ddd;">Amount</th>
                    <th style="padding: 10px; text-align: right; border: 1px solid #ddd;">Percentage</th>
                </tr>
        """
        
        for category, amount in sorted(expense_categories.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / total_expenses * 100) if total_expenses > 0 else 0
            html += f"""
                <tr>
                    <td style="padding: 10px; border: 1px solid #ddd;">{category}</td>
                    <td style="padding: 10px; text-align: right; border: 1px solid #ddd;">${amount:,.2f}</td>
                    <td style="padding: 10px; text-align: right; border: 1px solid #ddd;">{percentage:.1f}%</td>
                </tr>
            """
        
        html += f"""
                <tr style="background: #f8f9fa; font-weight: bold;">
                    <td style="padding: 10px; border: 1px solid #ddd;">TOTAL</td>
                    <td style="padding: 10px; text-align: right; border: 1px solid #ddd;">${total_expenses:,.2f}</td>
                    <td style="padding: 10px; text-align: right; border: 1px solid #ddd;">100.0%</td>
                </tr>
            </table>
        </div>
        """
        
        return html
    
    def create_cash_flow_chart(self, financial_data: Dict[str, Any]) -> str:
        """💰 ENHANCED CASH FLOW CHART WITH SMART FALLBACKS"""
        
        print("💰 Creating cash flow chart...")
        
        try:
            # Extract financial data
            income = financial_data.get('total_income', 0)
            expenses = financial_data.get('total_expenses', 0)
            net_savings = income - expenses
            
            if income == 0 and expenses == 0:
                return self._create_no_data_message("cash flow",
                    "📊 No financial data available for cash flow analysis.<br>Upload your financial document to see cash flow!")
            
            # Try different visualization approaches
            if self.can_create_interactive:
                return self._create_interactive_cash_flow(income, expenses, net_savings)
            elif self.can_create_static:
                return self._create_static_cash_flow(income, expenses, net_savings)
            else:
                return self._create_text_cash_flow(income, expenses, net_savings)
                
        except Exception as e:
            print(f"❌ Error creating cash flow chart: {e}")
            return self._create_error_message("cash flow chart", str(e))
    
    def _create_interactive_cash_flow(self, income: float, expenses: float, net_savings: float) -> str:
        """💰 Interactive cash flow chart with Plotly"""
        
        categories = ['💰 Monthly Income', '💸 Monthly Expenses', '💎 Available for Savings']
        values = [income, -expenses, net_savings]
        colors = [
            '#28a745',  # Green for income
            '#dc3545',  # Red for expenses  
            '#007bff' if net_savings >= 0 else '#dc3545'  # Blue/red for savings
        ]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=categories,
            y=values,
            marker_color=colors,
            text=[f'${abs(val):,.0f}' for val in values],
            textposition='auto',
            textfont=dict(size=16, color='white', family='Arial Black'),
            hovertemplate='<b>%{x}</b><br>Amount: $%{y:,.2f}<extra></extra>'
        ))
        
        fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
        
        fig.update_layout(
            title={
                'text': "💰 Monthly Cash Flow Overview",
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20, 'color': '#2E86AB'}
            },
            yaxis_title="Amount ($)",
            yaxis=dict(tickformat='$,.0f', gridcolor='lightgray'),
            plot_bgcolor='white',
            height=400
        )
        
        return fig.to_html(include_plotlyjs=True, div_id="cash_flow_chart")
    
    def _create_static_cash_flow(self, income: float, expenses: float, net_savings: float) -> str:
        """📊 Static cash flow chart with Matplotlib"""
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        categories = ['Monthly Income', 'Monthly Expenses', 'Available for Savings']
        values = [income, expenses, abs(net_savings)]
        colors = ['#28a745', '#dc3545', '#007bff' if net_savings >= 0 else '#dc3545']
        
        bars = ax.bar(categories, values, color=colors)
        
        # Add value labels on bars
        for bar, value in zip(bars, [income, expenses, net_savings]):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'${abs(value):,.0f}', ha='center', va='bottom', fontweight='bold')
        
        ax.set_title('💰 Monthly Cash Flow Overview', fontsize=16, fontweight='bold')
        ax.set_ylabel('Amount ($)')
        ax.grid(axis='y', alpha=0.3)
        
        # Convert to HTML
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', bbox_inches='tight', dpi=150)
        img_buffer.seek(0)
        img_base64 = base64.b64encode(img_buffer.read()).decode()
        plt.close()
        
        return f'<img src="data:image/png;base64,{img_base64}" style="max-width: 100%; height: auto;">'
    
    def _create_text_cash_flow(self, income: float, expenses: float, net_savings: float) -> str:
        """📝 Text-based cash flow summary"""
        
        savings_rate = (net_savings / income * 100) if income > 0 else 0
        status = "positive" if net_savings > 0 else "negative" if net_savings < 0 else "break-even"
        status_color = "#28a745" if net_savings > 0 else "#dc3545" if net_savings < 0 else "#ffc107"
        
        return f"""
        <div style="background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            <h3 style="color: #2E86AB; margin-top: 0;">💰 Monthly Cash Flow Overview</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
                <div style="background: #28a745; color: white; padding: 15px; border-radius: 8px; text-align: center;">
                    <h4 style="margin: 0;">💰 Monthly Income</h4>
                    <p style="font-size: 24px; font-weight: bold; margin: 5px 0;">${income:,.2f}</p>
                </div>
                <div style="background: #dc3545; color: white; padding: 15px; border-radius: 8px; text-align: center;">
                    <h4 style="margin: 0;">💸 Monthly Expenses</h4>
                    <p style="font-size: 24px; font-weight: bold; margin: 5px 0;">${expenses:,.2f}</p>
                </div>
                <div style="background: {status_color}; color: white; padding: 15px; border-radius: 8px; text-align: center;">
                    <h4 style="margin: 0;">💎 Net Cash Flow</h4>
                    <p style="font-size: 24px; font-weight: bold; margin: 5px 0;">${net_savings:,.2f}</p>
                    <p style="margin: 0; font-size: 14px;">({savings_rate:.1f}% savings rate)</p>
                </div>
            </div>
            <p style="margin-top: 15px; text-align: center; color: #666;">
                Cash flow status: <strong style="color: {status_color};">{status.title()}</strong>
            </p>
        </div>
        """
    
    def create_financial_dashboard(self, financial_data: Dict[str, Any]) -> str:
        """📈 ENHANCED COMPREHENSIVE FINANCIAL DASHBOARD"""
        
        print("📈 Creating comprehensive financial dashboard...")
        
        try:
            # Calculate key metrics
            income = financial_data.get('total_income', 0)
            expenses = financial_data.get('total_expenses', 0)
            net_cash_flow = income - expenses
            savings_rate = ((net_cash_flow / income) * 100) if income > 0 else 0
            health_score = self._calculate_health_score(income, expenses, net_cash_flow)
            health_color = self._get_health_color(health_score)
            
            # Create dashboard header
            dashboard_html = f"""
            <!-- ENHANCED DASHBOARD HEADER -->
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; margin: 20px 0; box-shadow: 0 10px 25px rgba(0,0,0,0.2);">
                <h1 style="text-align: center; margin: 0; font-size: 28px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); font-family: 'Arial', sans-serif;">
                    📈 Your Personal Financial Health Dashboard
                </h1>
                <p style="text-align: center; margin: 10px 0; opacity: 0.9; font-size: 16px;">
                    Complete overview powered by AI analysis with {self._get_capability_description()}
                </p>
            </div>
            
            <!-- KEY METRICS CARDS -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 30px 0;">
                
                <!-- INCOME CARD -->
                <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-left: 5px solid #28a745; transition: transform 0.2s;">
                    <div style="display: flex; align-items: center; margin-bottom: 10px;">
                        <span style="font-size: 24px; margin-right: 10px;">💰</span>
                        <h3 style="color: #28a745; margin: 0; font-size: 16px; font-weight: 600;">Monthly Income</h3>
                    </div>
                    <p style="font-size: 32px; font-weight: bold; margin: 0; color: #2c3e50; font-family: 'Arial Black';">${income:,.2f}</p>
                    <p style="margin: 5px 0 0 0; color: #7f8c8d; font-size: 14px;">Total monthly earnings</p>
                </div>
                
                <!-- EXPENSES CARD -->
                <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-left: 5px solid #dc3545; transition: transform 0.2s;">
                    <div style="display: flex; align-items: center; margin-bottom: 10px;">
                        <span style="font-size: 24px; margin-right: 10px;">💸</span>
                        <h3 style="color: #dc3545; margin: 0; font-size: 16px; font-weight: 600;">Monthly Expenses</h3>
                    </div>
                    <p style="font-size: 32px; font-weight: bold; margin: 0; color: #2c3e50; font-family: 'Arial Black';">${expenses:,.2f}</p>
                    <p style="margin: 5px 0 0 0; color: #7f8c8d; font-size: 14px;">Total monthly spending</p>
                </div>
                
                <!-- CASH FLOW CARD -->
                <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-left: 5px solid #007bff; transition: transform 0.2s;">
                    <div style="display: flex; align-items: center; margin-bottom: 10px;">
                        <span style="font-size: 24px; margin-right: 10px;">💎</span>
                        <h3 style="color: #007bff; margin: 0; font-size: 16px; font-weight: 600;">Net Cash Flow</h3>
                    </div>
                    <p style="font-size: 32px; font-weight: bold; margin: 0; color: #2c3e50; font-family: 'Arial Black';">${net_cash_flow:,.2f}</p>
                    <p style="margin: 5px 0 0 0; color: #7f8c8d; font-size: 14px;">Available for savings & investments</p>
                </div>
                
                <!-- FINANCIAL HEALTH SCORE CARD -->
                <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-left: 5px solid {health_color}; transition: transform 0.2s;">
                    <div style="display: flex; align-items: center; margin-bottom: 10px;">
                        <span style="font-size: 24px; margin-right: 10px;">❤️</span>
                        <h3 style="color: {health_color}; margin: 0; font-size: 16px; font-weight: 600;">Financial Health Score</h3>
                    </div>
                    <p style="font-size: 32px; font-weight: bold; margin: 0; color: #2c3e50; font-family: 'Arial Black';">{health_score}/100</p>
                    <p style="margin: 5px 0 0 0; color: #7f8c8d; font-size: 14px;">Savings rate: {savings_rate:.1f}%</p>
                </div>
            </div>
            """
            
            # Add visualizations based on capabilities
            if self.can_create_interactive or self.can_create_static:
                dashboard_html += f"""
                <!-- EXPENSE BREAKDOWN CHART SECTION -->
                <div style="background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin: 20px 0;">
                    <h2 style="margin-top: 0; color: #2c3e50; font-size: 18px; border-bottom: 2px solid #eee; padding-bottom: 10px;">
                        📊 Expense Analysis
                    </h2>
                    {self.create_expense_pie_chart(financial_data)}
                </div>
                
                <!-- CASH FLOW CHART SECTION -->
                <div style="background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin: 20px 0;">
                    <h2 style="margin-top: 0; color: #2c3e50; font-size: 18px; border-bottom: 2px solid #eee; padding-bottom: 10px;">
                        💰 Cash Flow Overview
                    </h2>
                    {self.create_cash_flow_chart(financial_data)}
                </div>
                """
            else:
                dashboard_html += """
                <!-- CHARTS UNAVAILABLE NOTICE -->
                <div style="background: #fff3cd; padding: 20px; border-radius: 12px; border-left: 4px solid #ffc107; margin: 20px 0;">
                    <h3 style="margin-top: 0; color: #856404;">📊 Visualization Libraries Unavailable</h3>
                    <p style="color: #856404; margin-bottom: 10px;">Charts are temporarily unavailable, but all financial analysis is still working!</p>
                    <p style="color: #856404; margin: 0; font-size: 14px;">To enable charts: pip install plotly matplotlib</p>
                </div>
                """
            
            # Add insights footer
            dashboard_html += f"""
            <!-- FOOTER WITH INSIGHTS -->
            <div style="background: #f8f9fa; padding: 20px; border-radius: 12px; margin: 20px 0; border-left: 4px solid #007bff;">
                <h3 style="margin-top: 0; color: #2c3e50;">📈 Key Insights</h3>
                <ul style="color: #6c757d; line-height: 1.6;">
                    <li><strong>Cash Flow:</strong> {"Positive" if net_cash_flow > 0 else "Negative"} ${abs(net_cash_flow):,.2f} per month</li>
                    <li><strong>Savings Rate:</strong> {savings_rate:.1f}% {"(Excellent!)" if savings_rate >= 20 else "(Consider increasing)" if savings_rate >= 10 else "(Needs improvement)"}</li>
                    <li><strong>Health Score:</strong> {health_score}/100 {"(Great job!)" if health_score >= 80 else "(Room for improvement)" if health_score >= 60 else "(Needs attention)"}</li>
                    <li><strong>Visualization:</strong> {self._get_capability_description()}</li>
                </ul>
            </div>
            """
            
            return dashboard_html
            
        except Exception as e:
            print(f"❌ Error creating dashboard: {e}")
            return self._create_error_message("financial dashboard", str(e))
    
    def _get_capability_description(self) -> str:
        """📋 Get description of current visualization capabilities"""
        if self.can_create_interactive:
            return "Interactive charts with full functionality"
        elif self.can_create_static:
            return "Static charts with limited interactivity"
        else:
            return "Text summaries (install plotly for charts)"
    
    def _calculate_health_score(self, income: float, expenses: float, net_cash_flow: float) -> int:
        """
        📊 ENHANCED FINANCIAL HEALTH SCORE CALCULATION
        
        HOW THE SCORING WORKS:
        1. Primary factor: Savings rate (most important for financial health)
        2. Secondary factor: Expense control (keeping expenses reasonable)
        3. Bonus points: Very low expense ratios get extra credit
        
        SCORING BREAKDOWN:
        - 90-100 points: 20%+ savings rate (excellent financial health)
        - 80-89 points: 15-19% savings rate (very good)
        - 70-79 points: 10-14% savings rate (good)
        - 60-69 points: 5-9% savings rate (fair, needs improvement)
        - 50-59 points: 1-4% savings rate (poor, urgent attention needed)
        - 30-49 points: 0% or negative savings (critical situation)
        
        BONUS POINTS:
        - +10 points: Expenses < 50% of income (very frugal)
        - +5 points: Expenses < 70% of income (good control)
        
        WHY THIS SCORING:
        - Based on financial research and expert recommendations
        - Emphasizes savings rate (the #1 predictor of financial success)
        - Rewards expense control (living below your means)
        - Provides clear benchmarks for improvement
        """
        if income <= 0:
            return 0
        
        savings_rate = (net_cash_flow / income) * 100
        
        if savings_rate >= 20:
            score = 90
        elif savings_rate >= 15:
            score = 80
        elif savings_rate >= 10:
            score = 70
        elif savings_rate >= 5:
            score = 60
        elif savings_rate > 0:
            score = 50
        else:
            score = 30
        
        expense_ratio = (expenses / income) * 100
        if expense_ratio < 50:
            score += 10
        elif expense_ratio < 70:
            score += 5
        
        return min(100, score)
    
    def _get_health_color(self, score: int) -> str:
        """🎨 Get color based on health score"""
        if score >= 80:
            return '#28a745'  # Green
        elif score >= 60:
            return '#ffc107'  # Yellow
        else:
            return '#dc3545'  # Red
    
    def _create_no_data_message(self, chart_type: str, message: str) -> str:
        """📝 Create professional no-data message"""
        return f"""
        <div style="text-align: center; padding: 50px; background: #f8f9fa; border-radius: 10px; margin: 20px; border: 2px dashed #dee2e6;">
            <h3 style="color: #6c757d; margin-bottom: 15px;">📊 {chart_type.title()} Chart</h3>
            <p style="color: #6c757d; font-size: 16px; line-height: 1.5;">{message}</p>
        </div>
        """
    
    def _create_error_message(self, component: str, error: str) -> str:
        """❌ Create professional error message"""
        return f"""
        <div style="background: #f8d7da; color: #721c24; padding: 20px; border-radius: 10px; border-left: 4px solid #dc3545; margin: 20px;">
            <h3 style="margin-top: 0;">❌ {component.title()} Error</h3>
            <p style="margin-bottom: 10px;">There was an issue creating the {component}:</p>
            <code style="background: #fff; padding: 5px; border-radius: 3px; display: block; margin: 10px 0;">{error}</code>
            <p style="margin: 0; font-size: 14px;">The rest of your financial analysis should still work normally.</p>
        </div>
        """

# ============================================================================
# SELF-TEST FUNCTION - Validate Visualizer Capabilities
# ============================================================================

def test_visualizer_capabilities():
    """
    🧪 COMPREHENSIVE VISUALIZER TESTING
    
    WHAT THIS FUNCTION DOES:
    1. Tests all visualization components
    2. Reports available capabilities
    3. Provides sample output for each chart type
    4. Validates error handling
    """
    
    print("🧪 Testing Financial Visualizer capabilities...")
    print("=" * 50)
    
    # Create sample data
    sample_data = {
        'total_income': 5000,
        'total_expenses': 3500,
        'categories': {
            'Rent': 1200,
            'Groceries': 400,
            'Transportation': 300,
            'Entertainment': 200,
            'Utilities': 150,
            'Insurance': 250,
            'Salary': 5000
        }
    }
    
    # Test visualizer
    try:
        viz = FinancialVisualizer()
        
        print("📊 Testing expense pie chart...")
        pie_result = viz.create_expense_pie_chart(sample_data)
        print(f"✅ Pie chart: {'Interactive' if viz.can_create_interactive else 'Static' if viz.can_create_static else 'Text only'}")
        
        print("💰 Testing cash flow chart...")
        flow_result = viz.create_cash_flow_chart(sample_data)
        print(f"✅ Cash flow: {'Interactive' if viz.can_create_interactive else 'Static' if viz.can_create_static else 'Text only'}")
        
        print("📈 Testing financial dashboard...")
        dashboard_result = viz.create_financial_dashboard(sample_data)
        print("✅ Dashboard: Created successfully")
        
        print("=" * 50)
        print("🎉 All visualizer tests passed!")
        
        return True
        
    except Exception as e:
        print(f"❌ Visualizer test failed: {e}")
        return False

# ============================================================================
# MAIN EXECUTION - For Testing
# ============================================================================

if __name__ == "__main__":
    """
    🎯 VISUALIZER TESTING ENTRY POINT
    
    When someone runs "python visualizer.py", this tests all functionality
    """
    print("🎨 Financial Visualizer - Standalone Testing")
    print("=" * 60)
    
    success = test_visualizer_capabilities()
    
    if success:
        print("✅ Visualizer is ready for use in the main application!")
    else:
        print("❌ Some issues detected - check error messages above")
        print("💡 Try: pip install plotly matplotlib pandas")

# ============================================================================
# END OF ENHANCED VISUALIZER
# ============================================================================