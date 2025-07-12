import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import calendar
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def plot_spending_trends(df):
    """Plot spending trends over time"""
    plt.style.use('seaborn')
    fig, axes = plt.subplots(3, 1, figsize=(12, 15))
    fig.suptitle('Monthly Financial Dashboard', fontsize=16, y=0.95)
    
    # Spending Plot
    spending_data = df[['date', 'money_spent_on_eating_out', 'money_spent_on_groceries', 
                       'money_spent_entertainment_alcohol']]
    spending_data.plot(x='date', y=['money_spent_on_eating_out', 'money_spent_on_groceries', 
                                   'money_spent_entertainment_alcohol'],
                      ax=axes[0], marker='o')
    axes[0].set_title('Monthly Spending')
    axes[0].set_ylabel('Amount ($)')
    axes[0].legend(['Eating Out', 'Groceries', 'Entertainment/Alcohol'])
    
    # Savings Contributions Plot
    contributions_data = df[['date', 'money_put_towards_retirement', 
                           'money_put_towards_house', 'money_put_towards_portfolio']]
    contributions_data.plot(x='date', y=['money_put_towards_retirement', 
                                       'money_put_towards_house', 
                                       'money_put_towards_portfolio'],
                          ax=axes[1], marker='o')
    axes[1].set_title('Monthly Contributions')
    axes[1].set_ylabel('Amount ($)')
    axes[1].legend(['Retirement', 'Housing', 'Investment Portfolio'])
    
    # Total Savings Plot
    savings_data = df[['date', 'money_saved_for_retirement', 
                      'money_saved_for_house', 'money_saved_in_portfolio']]
    savings_data.plot(x='date', y=['money_saved_for_retirement', 
                                  'money_saved_for_house', 
                                  'money_saved_in_portfolio'],
                     ax=axes[2], marker='o')
    axes[2].set_title('Total Savings Over Time')
    axes[2].set_ylabel('Amount ($)')
    axes[2].legend(['Retirement', 'Housing', 'Investment Portfolio'])
    
    # Adjust layout and display
    plt.tight_layout()
    plt.show()

def calculate_monthly_stats(df):
    """Calculate and display monthly statistics"""
    if len(df) >= 2:
        current = df.iloc[-1]
        previous = df.iloc[-2]

        print("\n=== Monthly Summary ===")
        print(f"\nTotal Spending This Month: ${current['money_spent_on_eating_out'] + current['money_spent_on_groceries'] + current['money_spent_entertainment_alcohol']:,.2f}")
        
        # Calculate month-over-month changes
        retirement_change = current['money_saved_for_retirement'] - previous['money_saved_for_retirement']
        house_change = current['money_saved_for_house'] - previous['money_saved_for_house']
        portfolio_change = current['money_saved_in_portfolio'] - previous['money_saved_in_portfolio']
        
        print("\nMonth-over-Month Changes:")
        print(f"Retirement: ${retirement_change:+,.2f}")
        print(f"Housing Fund: ${house_change:+,.2f}")
        print(f"Investment Portfolio: ${portfolio_change:+,.2f}")

if __name__ == "__main__":
    # First, run the monthly expense tracker to get new data
    from monthly_expense_tracker import new_month
    
    # Get new monthly data
    print("Let's record this month's financial data...")
    # new_month()
    
    # Read the updated CSV and create visualizations
    try:
        df = pd.read_csv("data.csv")
        print(df.head())
        # Convert date strings to datetime objects
        df['date'] = pd.to_datetime(df['date'])
        
        # Generate and show plots
        plot_spending_trends(df)
        
        # Show monthly statistics
        calculate_monthly_stats(df)
        
    except FileNotFoundError:
        print("No existing data found. Please run the script again next month to see trends.") 