# Student Monthly Budget Analyzer

print("Welcome to My Monthly Budget Analyzer")
name = input("Enter student name = ")
monthly_income = float(input("Enter monthly income:- "))
food = float(input("Enter food expenses:- "))
travel = float(input("Enter travel expenses:- "))
study_material = float(input("Enter study materials expenses:- "))
mobile = float(input("Enter mobile/internet expenses:- "))
other = float(input("Enter other expenses:- "))

total_expenses = food + travel + study_material + mobile  + other

balance = monthly_income - total_expenses

if monthly_income > 0:
   savings_rate = (balance / monthly_income) * 100
else:
   savings_rate = 0

print("\n----- MONTHLY BUDGET REPORT -----")
print("Student:", name)
print("Monthly income: ₹", format(monthly_income, ".2f"))
print("Food expenses: ₹", format(food, ".2f"))
print("Travel expenses: ₹", format(travel, ".2f"))
print("Study materials: ₹", format(study_material, ".2f"))
print("Mobile/internet expenses: ₹", format(mobile, ".2f"))
print("Other expenses: ₹", format(other, ".2f"))

print("Total expenses: ₹", format(total_expenses, ".2f"))
print("Remaining balance: ₹", format(balance, ".2f"))
print("Savings rate:", format(savings_rate, ".2f"), "%")

if total_expenses > 0:
   print("\nExpenses Category Percentages:")
   print("Food:", format(food / total_expenses * 100, ".2f"), "%")
   print("Travel:", format(travel / total_expenses * 100, ".2f"), "%")
   print("Study materials:", format(study_material / total_expenses * 100, ".2f"), "%")
   print("Mobile/internet:", format(mobile/ total_expenses * 100, ".2f"), "%")
   print("Other:", format(other / total_expenses * 100, ".2f"), "%")
else:
   print("No expenses were entered.")

print("\n------THE END------")

print("\n------THANK YOU------")