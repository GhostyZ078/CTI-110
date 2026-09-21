# Nicolas Posso
# 09/20/2026
# P1HW2 - Travel Expenses
# This code calculates and shows travel expenses.

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter Budget: "))

destination = input("Enter your travel destination: ")
print()

gas = int(input("How much do you think you will spend on gas? "))

accommodation = int(input("Approximately, how much will you need for accomodation/hotel? "))

food = int(input("Last, how much do you need for food? "))
print()

total_expenses = gas + accommodation + food

remaining_balance = budget - total_expenses

print("------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print()
print("Remaining Balance:", remaining_balance)