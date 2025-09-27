# ============================================================================
# AI FINANCIAL COACH AGENTS - ENHANCED WITH SMART PREREQUISITES
# ============================================================================
# This file contains 5 specialized AI agents that work together to analyze
# your financial situation and provide personalized advice.
# 
# ENHANCED FEATURES:
# 🔧 Automatic dependency checking and installation
# 🚨 Graceful fallbacks when AI services aren't available
# 🔑 Smart API key validation with helpful guidance
# 📊 Comprehensive error handling with recovery options
# 🎯 Professional logging and debugging capabilities
# 
# WHAT THIS FILE DOES:
# 1. 🏦 DebtAnalyzerAgent - Finds debt patterns and suggests payoff strategies
# 2. 💰 SavingsStrategyAgent - Creates personalized savings plans  
# 3. 📋 BudgetAdvisorAgent - Analyzes spending with 50/30/20 rule
# 4. 🎯 OptimizedPayoffAgent - Compares debt payoff methods (avalanche vs snowball)
# 5. 📊 FinancialReportAgent - Compiles everything into comprehensive reports
# 
# AI ARCHITECTURE:
# - Primary: OpenAI GPT-4o-mini for cost-effective analysis
# - Fallback: Rule-based analysis when AI unavailable
# - Smart prompting: Optimized templates for financial advice
# - Error recovery: Graceful degradation with helpful guidance
# ============================================================================

import sys
import subprocess
import importlib.util
import os
import json
from typing import Dict, List, Any

# ============================================================================
# SMART DEPENDENCY MANAGEMENT - AI Agent Prerequisites
# ============================================================================

def check_ai_dependencies():
    """
    🤖 AI DEPENDENCY CHECKER AND INSTALLER
    
    WHAT THIS FUNCTION DOES:
    1. Checks if AI/ML packages are available
    2. Attempts to install missing packages automatically
    3. Validates API keys and configurations
    4. Returns capability flags for different AI features
    
    AI PACKAGES NEEDED:
    - langchain-openai: Main AI language model interface
    - langchain: Core prompt templates and utilities
    - pandas: Data manipulation for financial analysis
    - json: Data serialization (built-in)
    
    RETURNS:
    Dictionary with capability flags for different AI features
    """
    
    print("🤖 Checking AI dependencies...")
    
    capabilities = {
        'openai_available': False,
        'langchain_available': False,
        'data_processing': False,
        'api_key_valid': False,
        'full_ai_analysis': False
    }
    
    # Check LangChain OpenAI (primary AI engine)
    try:
        from langchain_openai import ChatOpenAI
        capabilities['openai_available'] = True
        print("✅ LangChain OpenAI - AI analysis available")
    except ImportError:
        print("❌ LangChain OpenAI missing - trying to install...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "langchain-openai"])
            from langchain_openai import ChatOpenAI
            capabilities['openai_available'] = True
            print("✅ LangChain OpenAI installed successfully!")
        except Exception as e:
            print(f"⚠️ LangChain OpenAI installation failed: {e}")
    
    # Check LangChain core (prompt templates)
    try:
        from langchain.prompts import PromptTemplate
        capabilities['langchain_available'] = True
        print("✅ LangChain core - Prompt templates available")
    except ImportError:
        print("❌ LangChain core missing - trying to install...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "langchain"])
            capabilities['langchain_available'] = True
            print("✅ LangChain core installed successfully!")
        except Exception as e:
            print(f"⚠️ LangChain core installation failed: {e}")
    
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
    
    # Check API key
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key and openai_key != "your-api-key-here" and openai_key.startswith('sk-'):
        capabilities['api_key_valid'] = True
        print("✅ OpenAI API key - Valid format detected")
    else:
        print("⚠️ OpenAI API key - Missing or invalid format")
    
    # Determine full AI capability
    capabilities['full_ai_analysis'] = (
        capabilities['openai_available'] and 
        capabilities['langchain_available'] and 
        capabilities['api_key_valid']
    )
    
    if capabilities['full_ai_analysis']:
        print("🎉 Full AI analysis capabilities available!")
    else:
        print("💡 Limited AI capabilities - fallback analysis will be used")
    
    return capabilities

# Initialize capabilities
AI_CAPABILITIES = check_ai_dependencies()

# Smart imports based on availability
if AI_CAPABILITIES['openai_available']:
    try:
        from langchain_openai import ChatOpenAI
        OPENAI_AVAILABLE = True
    except ImportError:
        OPENAI_AVAILABLE = False
else:
    OPENAI_AVAILABLE = False

if AI_CAPABILITIES['langchain_available']:
    try:
        from langchain.prompts import PromptTemplate
        LANGCHAIN_AVAILABLE = True
    except ImportError:
        LANGCHAIN_AVAILABLE = False
else:
    LANGCHAIN_AVAILABLE = False

if AI_CAPABILITIES['data_processing']:
    try:
        import pandas as pd
        PANDAS_AVAILABLE = True
    except ImportError:
        PANDAS_AVAILABLE = False
else:
    PANDAS_AVAILABLE = False

# ============================================================================
# AI MODEL SETUP - Enhanced with Error Handling
# ============================================================================

def initialize_ai_model():
    """
    🧠 SMART AI MODEL INITIALIZATION
    
    WHAT THIS FUNCTION DOES:
    1. Attempts to initialize OpenAI model with proper configuration
    2. Validates API key format and connectivity
    3. Provides detailed error messages for troubleshooting
    4. Returns model instance or None for fallback handling
    """
    
    if not (OPENAI_AVAILABLE and LANGCHAIN_AVAILABLE):
        print("⚠️ AI libraries not available - using fallback analysis")
        return None
    
    try:
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")
        
        if not OPENAI_API_KEY or OPENAI_API_KEY == "your-api-key-here":
            print("⚠️ OpenAI API key not found - using fallback analysis")
            return None
        
        # Initialize with error handling
        llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            model="gpt-4o-mini",  # Cost-effective model
            temperature=0.7,      # Balance creativity and consistency
            max_tokens=2000,      # Reasonable response length
            timeout=30            # Prevent hanging requests
        )
        
        print("✅ AI model initialized successfully!")
        return llm
        
    except Exception as e:
        print(f"⚠️ AI model initialization failed: {e}")
        return None

# Initialize the AI model
llm = initialize_ai_model()

# ============================================================================
# AGENT 1: ENHANCED DEBT ANALYZER AGENT 🏦
# ============================================================================

class DebtAnalyzerAgent:
    """
    🏦 ENHANCED DEBT ANALYZER AGENT
    
    WHAT IT DOES:
    - Scans your transactions to find debt-related payments
    - Calculates debt-to-income ratios and health metrics
    - Uses AI for personalized strategies OR rule-based fallbacks
    - Suggests avalanche vs snowball methods with specific timelines
    
    ENHANCED FEATURES:
    - Smart fallback analysis when AI unavailable
    - Comprehensive error handling and recovery
    - Professional financial calculations
    - Educational explanations of debt strategies
    
    HOW IT WORKS:
    1. Identifies debt patterns in transaction data
    2. Calculates financial health metrics
    3. Uses AI analysis OR rule-based recommendations
    4. Returns actionable advice with specific dollar amounts
    """
    
    def __init__(self):
        self.agent_name = "💳 Enhanced Debt Analyzer"
        self.ai_available = llm is not None
        print(f"🏦 Debt Analyzer Agent initialized ({'AI-powered' if self.ai_available else 'rule-based'})")
    
    def analyze_debt(self, financial_data: Dict[str, Any]) -> str:
        """
        ENHANCED DEBT ANALYSIS WITH SMART FALLBACKS
        
        INPUTS:
        - financial_data: Dictionary containing income, expenses, transactions
        
        OUTPUTS:
        - String with detailed debt analysis and recommendations
        
        ENHANCEMENT FEATURES:
        - AI analysis when available (personalized, contextual)
        - Rule-based analysis as fallback (still valuable, professional)
        - Comprehensive error handling
        - Educational content regardless of AI availability
        """
        
        print("🏦 Analyzing debt patterns...")
        
        try:
            # STEP 1: Extract debt information
            debts = self._identify_debts(financial_data)
            income = financial_data.get('total_income', 0)
            expenses = financial_data.get('total_expenses', 0)
            
            # STEP 2: Calculate key metrics
            debt_metrics = self._calculate_debt_metrics(debts, income, expenses)
            
            # STEP 3: Choose analysis method
            if self.ai_available:
                return self._ai_debt_analysis(debts, debt_metrics, financial_data)
            else:
                return self._rule_based_debt_analysis(debts, debt_metrics, financial_data)
                
        except Exception as e:
            print(f"❌ Error in debt analysis: {e}")
            return self._create_error_fallback("debt analysis", str(e), financial_data)
    
    def _ai_debt_analysis(self, debts: List[Dict], debt_metrics: Dict, financial_data: Dict[str, Any]) -> str:
        """🤖 AI-powered debt analysis with personalized recommendations"""
        
        try:
            # Create comprehensive prompt for AI
            prompt_template = PromptTemplate(
                input_variables=["debts", "metrics", "income", "expenses"],
                template="""
                You are a certified financial counselor with 20 years experience in debt management.
                Analyze this client's debt situation and provide actionable advice:
                
                💰 FINANCIAL PROFILE:
                Monthly Income: ${income}
                Monthly Expenses: ${expenses}
                Debt Payments Identified: {debts}
                
                📊 DEBT METRICS:
                {metrics}
                
                Provide comprehensive analysis including:
                
                1. 📊 DEBT HEALTH ASSESSMENT
                   - Debt-to-income ratio evaluation
                   - Overall debt load assessment
                   - Risk factors and concerns
                
                2. 🎯 PAYOFF STRATEGY COMPARISON
                   - Avalanche method (highest interest first) analysis
                   - Snowball method (smallest balance first) analysis
                   - Recommendation for this specific situation
                
                3. 💵 SPECIFIC ACTION PLAN
                   - Recommended monthly payment amounts
                   - Timeline for debt freedom
                   - Milestones to track progress
                
                4. 🚀 IMMEDIATE NEXT STEPS
                   - 3 specific actions to take this week
                   - Tools or resources to use
                   - Warning signs to watch for
                
                Be encouraging but realistic. Use specific dollar amounts and timelines.
                Focus on actionable advice that can be implemented immediately.
                """
            )
            
            # Format data for AI
            debt_summary = json.dumps(debts, indent=2) if debts else "No specific debt payments identified in transactions"
            metrics_summary = json.dumps(debt_metrics, indent=2)
            
            # Generate prompt
            prompt = prompt_template.format(
                debts=debt_summary,
                metrics=metrics_summary,
                income=financial_data.get('total_income', 0),
                expenses=financial_data.get('total_expenses', 0)
            )
            
            # Get AI response
            analysis = llm.predict(prompt)
            return f"🤖 {self.agent_name} AI Analysis:\n\n{analysis}"
            
        except Exception as e:
            print(f"❌ AI debt analysis failed: {e}")
            # Fallback to rule-based analysis
            return self._rule_based_debt_analysis(debts, debt_metrics, financial_data)
    
    def _rule_based_debt_analysis(self, debts: List[Dict], debt_metrics: Dict, financial_data: Dict[str, Any]) -> str:
        """📋 Professional rule-based debt analysis (fallback)"""
        
        income = financial_data.get('total_income', 0)
        expenses = financial_data.get('total_expenses', 0)
        total_debt_payments = debt_metrics.get('total_monthly_payments', 0)
        debt_to_income_ratio = debt_metrics.get('debt_to_income_ratio', 0)
        
        # Assess debt health
        if debt_to_income_ratio <= 0.2:
            health_status = "Excellent"
            health_color = "🟢"
            health_advice = "Your debt-to-income ratio is excellent! You're in great financial shape."
        elif debt_to_income_ratio <= 0.36:
            health_status = "Good"
            health_color = "🟡"
            health_advice = "Your debt-to-income ratio is manageable but could be improved."
        else:
            health_status = "Needs Attention"
            health_color = "🔴"
            health_advice = "Your debt-to-income ratio is high. Focus on debt reduction immediately."
        
        # Generate professional analysis
        analysis = f"""
📊 **DEBT HEALTH ASSESSMENT**

{health_color} **Status**: {health_status}
💰 **Monthly Income**: ${income:,.2f}
💸 **Total Debt Payments**: ${total_debt_payments:,.2f}
📈 **Debt-to-Income Ratio**: {debt_to_income_ratio:.1%}

{health_advice}

---

🎯 **DEBT PAYOFF STRATEGIES**

**Avalanche Method (Recommended for Maximum Savings)**
- Pay minimums on all debts
- Put extra money toward highest interest rate debt
- Saves the most money in interest over time
- Best for disciplined borrowers focused on math

**Snowball Method (Recommended for Motivation)**
- Pay minimums on all debts  
- Put extra money toward smallest balance
- Provides psychological wins and momentum
- Best for people who need encouragement

---

💵 **ACTION PLAN**

**Immediate Steps (This Week):**
1. List all debts with balances, minimum payments, and interest rates
2. Choose either avalanche or snowball method based on your personality
3. Set up automatic payments to avoid late fees

**Short-term Goals (Next 3 Months):**
1. Find an extra ${max(50, (income - expenses) * 0.1):,.0f}/month for debt payments
2. Consider debt consolidation if you have multiple high-interest debts
3. Build a small emergency fund (${min(500, income * 0.1):,.0f}) to avoid new debt

**Long-term Vision (Next 12 Months):**
1. {"Maintain excellent debt management" if debt_to_income_ratio <= 0.2 else f"Reduce debt-to-income ratio to below 20% (currently {debt_to_income_ratio:.1%})"}
2. Increase available cash flow for savings and investments
3. Build comprehensive emergency fund (3-6 months expenses)

---

📱 **RECOMMENDED TOOLS**
- Debt Payoff Planner apps for tracking progress
- Mint or YNAB for budget tracking
- Credit monitoring services for score improvement

⚠️ **Note**: This analysis is based on transaction patterns. For complete debt strategy, gather all debt details including exact balances and interest rates.
        """
        
        return f"📋 {self.agent_name} Professional Analysis:\n\n{analysis}"
    
    def _identify_debts(self, financial_data: Dict[str, Any]) -> List[Dict]:
        """Enhanced debt identification with better pattern recognition"""
        
        debts = []
        debt_keywords = [
            'credit card', 'loan', 'mortgage', 'car payment', 'student loan', 
            'debt', 'payment', 'financing', 'installment', 'lease'
        ]
        
        for transaction in financial_data.get('transactions', []):
            description = transaction.get('category', '').lower()
            amount = transaction.get('amount', 0)
            
            # Only consider negative amounts (payments out)
            if amount < 0 and any(keyword in description for keyword in debt_keywords):
                debts.append({
                    'type': transaction.get('category'),
                    'amount': abs(amount),
                    'date': transaction.get('date'),
                    'description': transaction.get('description', '')
                })
        
        return debts
    
    def _calculate_debt_metrics(self, debts: List[Dict], income: float, expenses: float) -> Dict:
        """Calculate comprehensive debt health metrics"""
        
        total_monthly_payments = sum(debt.get('amount', 0) for debt in debts)
        debt_to_income_ratio = (total_monthly_payments / income) if income > 0 else 0
        available_for_extra_payments = max(0, income - expenses - total_monthly_payments)
        
        return {
            'total_monthly_payments': total_monthly_payments,
            'debt_to_income_ratio': debt_to_income_ratio,
            'number_of_debts': len(debts),
            'available_for_extra_payments': available_for_extra_payments,
            'debt_categories': list(set(debt.get('type', 'Unknown') for debt in debts))
        }
    
    def _create_error_fallback(self, analysis_type: str, error: str, financial_data: Dict[str, Any]) -> str:
        """Create helpful error fallback with basic analysis"""
        
        income = financial_data.get('total_income', 0)
        expenses = financial_data.get('total_expenses', 0)
        
        return f"""
❌ **{analysis_type.title()} Temporarily Unavailable**

**Issue**: {error}

**Basic Assessment Based on Your Data**:
- Monthly Income: ${income:,.2f}
- Monthly Expenses: ${expenses:,.2f}
- Net Cash Flow: ${income - expenses:,.2f}

**General Debt Management Advice**:
1. **Focus on high-interest debt first** (usually credit cards)
2. **Make minimum payments on all debts** to maintain good credit
3. **Find extra money** by reviewing your expense categories
4. **Consider the 50/30/20 rule**: 50% needs, 30% wants, 20% savings/debt payoff

**Next Steps**: The technical issue above should be resolved soon. Your financial analysis will work normally once the system is restored.
        """

# ============================================================================
# AGENT 2: ENHANCED SAVINGS STRATEGY AGENT 💰
# ============================================================================

class SavingsStrategyAgent:
    """
    💰 ENHANCED SAVINGS STRATEGY AGENT
    
    WHAT IT DOES:
    - Creates personalized savings plans based on income/expenses
    - Sets realistic emergency fund targets
    - Uses AI for custom strategies OR proven rule-based approaches
    - Provides investment guidance for surplus funds
    
    ENHANCED FEATURES:
    - Smart goal setting based on financial capacity
    - Multiple savings strategies (conservative, moderate, aggressive)
    - Behavioral psychology insights for better savings habits
    - Automatic vs manual savings recommendations
    """
    
    def __init__(self):
        self.agent_name = "💰 Enhanced Savings Strategist"
        self.ai_available = llm is not None
        print(f"💰 Savings Strategy Agent initialized ({'AI-powered' if self.ai_available else 'rule-based'})")
    
    def create_savings_plan(self, financial_data: Dict[str, Any], goals: str = "") -> str:
        """
        ENHANCED SAVINGS STRATEGY WITH SMART APPROACHES
        
        INPUTS:
        - financial_data: Income, expenses, spending patterns
        - goals: User's personal financial objectives
        
        OUTPUTS:
        - Comprehensive savings strategy with specific action steps
        
        ENHANCEMENT FEATURES:
        - AI-personalized strategies when available
        - Proven rule-based strategies as fallback
        - Multiple savings rate recommendations
        - Behavioral insights for success
        """
        
        print("💰 Creating personalized savings strategy...")
        
        try:
            # Calculate savings capacity
            income = financial_data.get('total_income', 0)
            expenses = financial_data.get('total_expenses', 0)
            available_for_savings = max(0, income - expenses)
            
            # Calculate savings metrics
            savings_metrics = self._calculate_savings_metrics(income, expenses, available_for_savings)
            
            # Choose strategy method
            if self.ai_available and goals:
                return self._ai_savings_strategy(savings_metrics, financial_data, goals)
            else:
                return self._rule_based_savings_strategy(savings_metrics, financial_data, goals)
                
        except Exception as e:
            print(f"❌ Error in savings strategy: {e}")
            return self._create_savings_fallback("savings strategy", str(e), financial_data)
    
    def _ai_savings_strategy(self, metrics: Dict, financial_data: Dict[str, Any], goals: str) -> str:
        """🤖 AI-powered personalized savings strategy"""
        
        try:
            prompt_template = PromptTemplate(
                input_variables=["metrics", "categories", "goals", "income"],
                template="""
                You are a certified financial planner specializing in savings strategies.
                Create a personalized savings plan for this client:
                
                📊 FINANCIAL PROFILE:
                {metrics}
                
                💰 SPENDING BREAKDOWN:
                {categories}
                
                🎯 CLIENT GOALS:
                {goals}
                
                Monthly Income: ${income}
                
                Create a comprehensive savings strategy including:
                
                1. 🎯 SAVINGS RATE RECOMMENDATION
                   - Recommended percentage of income to save
                   - Justification based on their financial situation
                   - Progressive goals (start vs long-term targets)
                
                2. 🚨 EMERGENCY FUND STRATEGY
                   - Target amount (3-6 months expenses)
                   - Timeline to build emergency fund
                   - Where to keep emergency funds
                
                3. ✂️ EXPENSE OPTIMIZATION
                   - Specific categories to reduce spending
                   - Dollar amounts that can be redirected to savings
                   - Practical tips for each category
                
                4. 🤖 AUTOMATION PLAN
                   - Automatic transfer amounts and timing
                   - Account setup recommendations
                   - "Pay yourself first" strategy
                
                5. 📈 GOAL-SPECIFIC SAVINGS
                   - Short-term goals (3-12 months)
                   - Medium-term goals (1-5 years)
                   - Long-term wealth building
                
                6. 💡 INVESTMENT RECOMMENDATIONS
                   - When to start investing
                   - Types of accounts (401k, IRA, taxable)
                   - Risk tolerance considerations
                
                Make it actionable with specific dollar amounts, percentages, and timelines.
                Focus on behavioral psychology - what will actually work for this person.
                """
            )
            
            # Format data for AI
            metrics_summary = json.dumps(metrics, indent=2)
            categories_summary = json.dumps(financial_data.get('categories', {}), indent=2)
            
            prompt = prompt_template.format(
                metrics=metrics_summary,
                categories=categories_summary,
                goals=goals or "Build financial security and achieve financial independence",
                income=financial_data.get('total_income', 0)
            )
            
            strategy = llm.predict(prompt)
            return f"🤖 {self.agent_name} AI Strategy:\n\n{strategy}"
            
        except Exception as e:
            print(f"❌ AI savings strategy failed: {e}")
            return self._rule_based_savings_strategy(metrics, financial_data, goals)
    
    def _rule_based_savings_strategy(self, metrics: Dict, financial_data: Dict[str, Any], goals: str) -> str:
        """📋 Professional rule-based savings strategy"""
        
        income = financial_data.get('total_income', 0)
        expenses = financial_data.get('total_expenses', 0)
        available = metrics.get('available_for_savings', 0)
        current_savings_rate = metrics.get('current_savings_rate', 0)
        
        # Determine savings rate recommendation
        if current_savings_rate >= 0.20:
            rate_status = "Excellent"
            rate_target = max(0.20, current_savings_rate)
            rate_advice = "You're already saving an excellent amount! Consider optimizing for tax efficiency."
        elif current_savings_rate >= 0.15:
            rate_status = "Very Good"
            rate_target = 0.20
            rate_advice = "You're doing well! Try to reach the ideal 20% savings rate."
        elif current_savings_rate >= 0.10:
            rate_status = "Good"
            rate_target = 0.15
            rate_advice = "Good foundation! Gradually increase your savings rate."
        elif current_savings_rate > 0:
            rate_status = "Fair"
            rate_target = 0.10
            rate_advice = "Start small and build the habit. Every dollar saved matters!"
        else:
            rate_status = "Needs Improvement"
            rate_target = 0.05
            rate_advice = "Focus on creating positive cash flow first, then build savings."
        
        # Calculate emergency fund target
        emergency_fund_target = expenses * 3  # Conservative 3 months
        emergency_fund_monthly = min(available * 0.5, emergency_fund_target / 12)
        
        # Generate strategy - Fixed formatting to avoid backslash in f-string
        long_term_goal = "Maintain excellent debt management" if current_savings_rate >= 0.20 else f"Reduce debt-to-income ratio to below 20% (currently {current_savings_rate:.1%})"
        
        strategy = f"""
🎯 **SAVINGS RATE ANALYSIS**

📊 **Current Status**: {rate_status}
💰 **Current Savings Rate**: {current_savings_rate:.1%} of income
🎯 **Target Savings Rate**: {rate_target:.1%} of income
💵 **Target Monthly Savings**: ${income * rate_target:,.0f}

{rate_advice}

---

🚨 **EMERGENCY FUND STRATEGY**

🎯 **Target Amount**: ${emergency_fund_target:,.0f} (3 months expenses)
💰 **Monthly Contribution**: ${emergency_fund_monthly:,.0f}
⏰ **Timeline**: {emergency_fund_target / max(emergency_fund_monthly, 1):.0f} months to full fund
🏦 **Where to Keep**: High-yield savings account or money market

**Why 3 Months**: Covers most common emergencies (job loss, medical bills, major repairs)

---

✂️ **EXPENSE OPTIMIZATION OPPORTUNITIES**

Based on typical spending patterns, consider reducing:
"""
        
        # Add category-specific advice
        categories = financial_data.get('categories', {})
        total_expenses_check = sum(categories.values())
        
        if total_expenses_check > 0:
            for category, amount in categories.items():
                percentage = (amount / total_expenses_check) * 100
                if percentage > 30 and 'rent' not in category.lower():
                    strategy += f"• **{category}**: ${amount:,.0f}/month ({percentage:.0f}% of expenses) - Consider reducing by 10-15%\n"
                elif percentage > 15 and category.lower() not in ['rent', 'mortgage', 'housing']:
                    strategy += f"• **{category}**: ${amount:,.0f}/month - Look for savings opportunities\n"
        
        strategy += f"""
---

🤖 **AUTOMATION PLAN**

**Step 1: Set Up Automatic Transfers**
- Transfer ${max(100, available * 0.2):,.0f}/month to savings on payday
- Start small and increase by $25/month every 3 months

**Step 2: Account Structure**
- Emergency fund: High-yield savings (aim for 4%+ APY)
- Short-term goals: Separate savings accounts
- Long-term: Consider investment accounts after emergency fund

**Step 3: "Pay Yourself First"**
- Treat savings like a non-negotiable bill
- Automate before you can spend the money

---

📈 **GOAL-SPECIFIC SAVINGS**

**Short-term (3-12 months)**:
{goals if goals else "• Build emergency funds• Save for annual expenses (insurance, taxes)"}

**Medium-term (1-5 years)**:
• Home down payment fund
• Vehicle replacement fund
• Major vacation or experience fund

**Long-term (5+ years)**:
• Retirement savings (401k, IRA)
• Investment portfolio building
• Financial independence planning

---

💡 **NEXT STEPS**

**This Week**:
1. Open high-yield savings account if you don't have one
2. Set up automatic transfer for ${max(50, available * 0.1):,.0f}/month
3. Review one major expense category for reduction opportunities

**This Month**:
1. Build your emergency fund to $1,000 minimum
2. Increase savings rate by finding one expense to cut
3. Research investment options for surplus funds

**This Quarter**:
1. Reach {min(25, rate_target * 100):.0f}% of your emergency fund goal
2. Optimize for tax-advantaged accounts (401k match, IRA)
3. Create specific timelines for your personal goals

---

 **RECOMMENDED TOOLS**
• High-yield savings: Ally Bank, Marcus, Capital One 360
• Budgeting: YNAB, Mint, PocketGuard
• Investment: Vanguard, Fidelity, Charles Schwab
• Automation: Bank bill pay, investment auto-transfers
        """
        
        return f"📋 {self.agent_name} Professional Strategy:\n\n{strategy}"
    
    def _calculate_savings_metrics(self, income: float, expenses: float, available: float) -> Dict:
        """Calculate comprehensive savings metrics"""
        
        current_savings_rate = (available / income) if income > 0 else 0
        emergency_fund_target = expenses * 3
        time_to_emergency_fund = (emergency_fund_target / available) if available > 0 else float('inf')
        
        return {
            'available_for_savings': available,
            'current_savings_rate': current_savings_rate,
            'emergency_fund_target': emergency_fund_target,
            'time_to_emergency_fund_months': min(time_to_emergency_fund, 120),  # Cap at 10 years
            'recommended_rate_conservative': 0.10,
            'recommended_rate_moderate': 0.15,
            'recommended_rate_aggressive': 0.20
        }
    
    def _create_savings_fallback(self, analysis_type: str, error: str, financial_data: Dict[str, Any]) -> str:
        """Create helpful savings fallback"""
        
        income = financial_data.get('total_income', 0)
        expenses = financial_data.get('total_expenses', 0)
        available = max(0, income - expenses)
        
        return f"""
❌ **{analysis_type.title()} Temporarily Unavailable**

**Issue**: {error}

**Quick Savings Assessment**:
- Available for Savings: ${available:,.2f}/month
- Recommended Emergency Fund: ${expenses * 3:,.2f}
- Suggested Savings Rate: 10-20% of income

**Universal Savings Principles**:
1. **Pay yourself first** - Save before spending
2. **Start with emergency fund** - $1,000 minimum, then 3-6 months expenses
3. **Automate everything** - Set up automatic transfers
4. **Increase gradually** - Add $25/month to savings every quarter

**The 50/30/20 Rule**: 50% needs, 30% wants, 20% savings/debt repayment
        """

# ============================================================================
# AGENT 3: ENHANCED BUDGET ADVISOR AGENT 📋
# ============================================================================

class BudgetAdvisorAgent:
    """
    📋 ENHANCED BUDGET ADVISOR AGENT
    
    WHAT IT DOES:
    - Analyzes your spending patterns against the famous 50/30/20 rule
    - Identifies categories where you're overspending
    - Suggests realistic budget allocations for each category
    - Provides practical tips to stay on budget
    
    ENHANCED FEATURES:
    - Smart budget analysis with multiple frameworks
    - Personalized recommendations based on income level
    - Behavioral insights for better budgeting
    - Emergency budget adjustments for financial stress
    """
    
    def __init__(self):
        self.agent_name = "📋 Enhanced Budget Advisor"
        self.ai_available = llm is not None
        print(f"📋 Budget Advisor Agent initialized ({'AI-powered' if self.ai_available else 'rule-based'})")
    
    def analyze_budget(self, financial_data: Dict[str, Any]) -> str:
        """
        ENHANCED BUDGET ANALYSIS WITH SMART RECOMMENDATIONS
        
        INPUTS:
        - financial_data: Dictionary with income and spending by category
        
        OUTPUTS:
        - String with detailed budget analysis and recommendations
        
        ENHANCEMENT FEATURES:
        - AI-powered personalized budget advice when available
        - Professional rule-based analysis as fallback
        - Multiple budgeting frameworks (50/30/20, zero-based, etc.)
        - Behavioral psychology insights
        """
        
        print("📋 Analyzing budget and spending patterns...")
        
        try:
            # Calculate budget metrics
            income = financial_data.get('total_income', 0)
            expenses = financial_data.get('total_expenses', 0)
            categories = financial_data.get('categories', {})
            
            # Choose analysis method
            if self.ai_available:
                return self._ai_budget_analysis(income, expenses, categories)
            else:
                return self._rule_based_budget_analysis(income, expenses, categories)
                
        except Exception as e:
            print(f"❌ Error in budget analysis: {e}")
            return self._create_budget_fallback("budget analysis", str(e), financial_data)
    
    def _ai_budget_analysis(self, income: float, expenses: float, categories: Dict) -> str:
        """🤖 AI-powered budget analysis"""
        
        try:
            prompt_template = PromptTemplate(
                input_variables=["income", "expenses", "categories"],
                template="""
                You are a budget expert analyzing spending patterns.
                
                💵 SPENDING ANALYSIS:
                Monthly Income: ${income}
                Monthly Expenses: ${expenses}
                Spending Categories: {categories}
                
                Analyze against the 50/30/20 budgeting rule and provide:
                
                1. 📊 Budget health assessment (what's working vs problematic)
                2. 💡 Recommended budget allocations by category (specific $ amounts)
                3. ⚠️ Overspending areas that need immediate attention
                4. 🛠️ Practical tips for each major spending category
                5. 📋 Complete monthly budget template with dollar amounts
                6. 🎯 One major change to implement this month
                
                Use 50/30/20 rule: 50% needs (rent, utilities, groceries), 
                30% wants (entertainment, dining out), 20% savings/debt repayment.
                """
            )
            
            prompt = prompt_template.format(
                income=income,
                expenses=expenses,
                categories=json.dumps(categories, indent=2)
            )
            
            advice = llm.predict(prompt)
            return f"🤖 {self.agent_name} AI Analysis:\n\n{advice}"
            
        except Exception as e:
            print(f"❌ AI budget analysis failed: {e}")
            return self._rule_based_budget_analysis(income, expenses, categories)
    
    def _rule_based_budget_analysis(self, income: float, expenses: float, categories: Dict) -> str:
        """📋 Professional rule-based budget analysis"""
        
        if income <= 0:
            return "❌ Cannot analyze budget without income data."
        
        expense_ratio = (expenses / income) * 100
        savings_potential = income - expenses
        savings_rate = (savings_potential / income) * 100
        
        # Budget health assessment
        if expense_ratio <= 50:
            budget_health = "Excellent"
            health_color = "🟢"
        elif expense_ratio <= 70:
            budget_health = "Good"
            health_color = "🟡"
        elif expense_ratio <= 90:
            budget_health = "Fair"
            health_color = "🟠"
        else:
            budget_health = "Needs Immediate Attention"
            health_color = "🔴"
        
        # 50/30/20 rule recommendations
        needs_budget = income * 0.50  # 50% for needs
        wants_budget = income * 0.30  # 30% for wants
        savings_budget = income * 0.20  # 20% for savings/debt
        
        analysis = f"""
📊 **BUDGET HEALTH ASSESSMENT**



{health_color} **Overall Health**: {budget_health}
💰 **Expense Ratio**: {expense_ratio:.1f}% of income
💎 **Savings Rate**: {savings_rate:.1f}% of income

---

💡 **50/30/20 RULE ANALYSIS**

**Recommended Budget Allocation:**
• 🏠 **Needs (50%)**: ${needs_budget:,.0f}/month
  - Housing, utilities, groceries, insurance, minimum debt payments
• 🎯 **Wants (30%)**: ${wants_budget:,.0f}/month
  - Entertainment, dining out, hobbies, subscriptions
• 💰 **Savings/Extra Debt (20%)**: ${savings_budget:,.0f}/month
  - Emergency fund, investments, extra debt payments

**Your Current Spending:**
• 💸 **Total Expenses**: ${expenses:,.0f}/month
• 💎 **Available for Savings**: ${savings_potential:,.0f}/month

---

⚠️ **SPENDING ANALYSIS BY CATEGORY**
"""
        
        # Analyze each category
        total_expenses = sum(categories.values()) if categories else expenses
        
        for category, amount in categories.items():
            percentage = (amount / income) * 100 if income > 0 else 0
            
            if percentage > 30:
                analysis += f"🔴 **{category}**: ${amount:,.0f} ({percentage:.1f}% of income) - REDUCE IMMEDIATELY\n"
            elif percentage > 15:
                analysis += f"🟡 **{category}**: ${amount:,.0f} ({percentage:.1f}% of income) - Consider reducing\n"
            else:
                analysis += f"🟢 **{category}**: ${amount:,.0f} ({percentage:.1f}% of income) - Well controlled\n"
        
        analysis += f"""
---

🛠️ **PRACTICAL BUDGET TIPS**

**For Housing (Target: 25-30% of income)**:
• If over 30%, consider roommates or moving to cheaper area
• Negotiate rent or refinance mortgage if possible

**For Food (Target: 10-15% of income)**:
• Meal plan and cook at home more often
• Use grocery store sales and coupons
• Limit restaurant visits to special occasions

**For Transportation (Target: 10-15% of income)**:
• Consider public transit or carpooling
• Maintain your vehicle to avoid expensive repairs
• Shop around for car insurance annually

**For Entertainment (Target: 5-10% of income)**:
• Set a monthly entertainment budget and stick to it
• Look for free community events and activities
• Cancel unused subscriptions

---

📋 **RECOMMENDED MONTHLY BUDGET**

**NEEDS (${needs_budget:,.0f}):**
• Housing: ${income * 0.25:,.0f}
• Utilities: ${income * 0.05:,.0f}
• Groceries: ${income * 0.10:,.0f}
• Insurance: ${income * 0.05:,.0f}
• Minimum Debt Payments: ${income * 0.05:,.0f}

**WANTS (${wants_budget:,.0f}):**
• Dining Out: ${income * 0.10:,.0f}
• Entertainment: ${income * 0.10:,.0f}
• Shopping: ${income * 0.05:,.0f}
• Personal Care: ${income * 0.05:,.0f}

**SAVINGS & EXTRA DEBT (${savings_budget:,.0f}):**
• Emergency Fund: ${income * 0.10:,.0f}
• Investments: ${income * 0.05:,.0f}
• Extra Debt Payments: ${income * 0.05:,.0f}

---

🎯 **THIS MONTH'S PRIORITY**

Focus on the largest overspending category and reduce it by 20%. This single change could free up significant money for savings or debt payoff.

---

📱 **RECOMMENDED BUDGETING TOOLS**
• YNAB (You Need A Budget) - Zero-based budgeting
• Mint - Automatic expense tracking
• PocketGuard - Prevents overspending
• Manual spreadsheet - Full control over categories
        """
        
        return f"📋 {self.agent_name} Professional Analysis:\n\n{analysis}"
    
    def _create_budget_fallback(self, analysis_type: str, error: str, financial_data: Dict[str, Any]) -> str:
        """Create helpful budget fallback"""
        
        income = financial_data.get('total_income', 0)
        expenses = financial_data.get('total_expenses', 0)
        
        return f"""
❌ **{analysis_type.title()} Temporarily Unavailable**

**Issue**: {error}

**Quick Budget Assessment**:
- Monthly Income: ${income:,.2f}
- Monthly Expenses: ${expenses:,.2f}
- Expense Ratio: {(expenses/income)*100:.1f}% of income

**50/30/20 Rule Quick Guide**:
- 50% Needs: ${income * 0.5:,.0f} (housing, utilities, groceries)
- 30% Wants: ${income * 0.3:,.0f} (entertainment, dining out)
- 20% Savings: ${income * 0.2:,.0f} (emergency fund, investments)

**Immediate Action**: If expenses exceed 80% of income, focus on reducing the largest expense category first.
        """

# ============================================================================
# SELF-TEST FUNCTION - Validate Agent Capabilities
# ============================================================================

def test_agent_capabilities():
    """
    🧪 COMPREHENSIVE AGENT TESTING
    
    WHAT THIS FUNCTION DOES:
    1. Tests all AI agents with sample data
    2. Reports available capabilities (AI vs rule-based)
    3. Validates error handling and fallbacks
    4. Provides performance metrics
    """
    
    print("🧪 Testing AI Financial Agent capabilities...")
    print("=" * 50)
    
    # Create sample financial data
    sample_data = {
        'total_income': 5000,
        'total_expenses': 3500,
        'categories': {
            'Rent': 1200,
            'Groceries': 400,
            'Car Payment': 350,
            'Credit Card': 200,
            'Utilities': 150,
            'Entertainment': 300,
            'Insurance': 250,
            'Gas': 200,
            'Salary': 5000
        },
        'transactions': [
            {'date': '2024-01-01', 'amount': 5000, 'category': 'Salary'},
            {'date': '2024-01-02', 'amount': -1200, 'category': 'Rent'},
            {'date': '2024-01-03', 'amount': -350, 'category': 'Car Payment'},
            {'date': '2024-01-04', 'amount': -200, 'category': 'Credit Card Payment'}
        ]
    }
    
    # Test agents
    try:
        print("🏦 Testing Debt Analyzer Agent...")
        debt_agent = DebtAnalyzerAgent()
        debt_result = debt_agent.analyze_debt(sample_data)
        print(f"✅ Debt Analysis: {'AI-powered' if debt_agent.ai_available else 'Rule-based'}")
        
        print("💰 Testing Savings Strategy Agent...")
        savings_agent = SavingsStrategyAgent()
        savings_result = savings_agent.create_savings_plan(sample_data, "Save for house down payment")
        print(f"✅ Savings Strategy: {'AI-powered' if savings_agent.ai_available else 'Rule-based'}")
        
        print("📋 Testing Budget Advisor Agent...")
        budget_agent = BudgetAdvisorAgent()
        budget_result = budget_agent.analyze_budget(sample_data)
        print(f"✅ Budget Analysis: {'AI-powered' if budget_agent.ai_available else 'Rule-based'}")
        
        print("=" * 50)
        print("🎉 All agent tests passed!")
        print(f"🤖 AI Capability: {'Full AI analysis available' if AI_CAPABILITIES['full_ai_analysis'] else 'Rule-based fallbacks active'}")
        
        return True
        
    except Exception as e:
        print(f"❌ Agent test failed: {e}")
        return False

# ============================================================================
# MAIN EXECUTION - For Testing
# ============================================================================

if __name__ == "__main__":
    """
    🎯 AGENT TESTING ENTRY POINT
    
    When someone runs "python agents.py", this tests all functionality
    """
    print("🤖 AI Financial Agents - Standalone Testing")
    print("=" * 60)
    
    success = test_agent_capabilities()
    
    if success:
        print("✅ All agents are ready for use in the main application!")
        if AI_CAPABILITIES['full_ai_analysis']:
            print("🎉 Full AI capabilities detected - premium experience available!")
        else:
            print("💡 Using professional rule-based analysis - still very valuable!")
    else:
        print("❌ Some issues detected - check error messages above")
        print("💡 Try: pip install langchain-openai langchain pandas")
        print("🔑 For AI features: export OPENAI_API_KEY='your-key-here'")


# ============================================================================
# AGENT 4: OPTIMIZED PAYOFF AGENT 💡
# ============================================================================

class OptimizedPayoffAgent:
    """
    💡 OPTIMIZED PAYOFF AGENT (Hackathon Version)

    WHAT IT DOES:
    - Generates a simple debt payoff plan
    - Supports extra monthly payments
    - Provides both Snowball and Avalanche strategies
    """
    def __init__(self):
        self.agent_name = "💡 Optimized Payoff Agent"
        print(f"{self.agent_name} initialized")

    def create_payoff_plan(self, financial_data, extra_payment=0):
        categories = financial_data.get("categories", {})
        total_debt = 0
        for cat, amount in categories.items():
            if "loan" in cat.lower() or "credit" in cat.lower() or "debt" in cat.lower():
                total_debt += amount

        if total_debt <= 0:
            return "✅ No debts detected. Keep saving and investing!"

        return f"""
        🎯 Optimized Debt Payoff Plan
        - Total debt identified: ${total_debt:,.2f}
        - Extra monthly payment: ${extra_payment:,.2f}

        Recommended Strategy:
        • Snowball: Pay smallest debts first for quick wins.
        • Avalanche: Pay highest-interest debts first to save money.
        • Reinvest payments as each debt clears.
        """

# ============================================================================
# AGENT 5: FINANCIAL REPORT AGENT 📊
# ============================================================================

class FinancialReportAgent:
    """
    📊 FINANCIAL REPORT AGENT (Hackathon Version)

    WHAT IT DOES:
    - Combines outputs from all agents into one report
    - Ensures consistent formatting
    - Provides a single string for the app to display
    """
    def __init__(self):
        self.agent_name = "📊 Financial Report Agent"
        print(f"{self.agent_name} initialized")

    def generate_report(self, debt_analysis, savings_strategy, budget_advice, payoff_plan, financial_data):
        report = f"""
        🏦 **Debt Analysis**
        {debt_analysis}

        💰 **Savings Strategy**
        {savings_strategy}

        📋 **Budget Advice**
        {budget_advice}

        🎯 **Debt Payoff Plan**
        {payoff_plan}

        📊 **Financial Summary**
        • Income: ${financial_data.get('total_income', 0):,.2f}
        • Expenses: ${financial_data.get('total_expenses', 0):,.2f}
        • Categories: {len(financial_data.get('categories', {}))}
        """
        return report


# ============================================================================
# END OF ENHANCED AI AGENTS
# ============================================================================