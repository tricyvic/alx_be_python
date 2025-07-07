monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expense: "))

# monthly_savings\s*=\s*(monthly_income\s*-\s*monthly_expenses|float\s*\(\s*monthly_income\s*\)\s*-\s*float\s*\(\s*monthly_expenses\s*\))


monthly_savings = monthly_income - monthly_expenses
annual_interest = 5/100

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")