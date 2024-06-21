# User Input for financial Details
monthly_income = int(input("Enter your monthly income: "))
Total_monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = Total_monthly_expenses - monthly_income
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")       
