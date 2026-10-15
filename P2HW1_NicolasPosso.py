# Nicolas Posso
# October 14, 2026
# P2HW1
# This code calculates and displays travel expenses

# Pseudocode:
# Get the budget from the user
# Get the travel destination
# Get the expenses for gas, accommodation, and food
# Calculate the remaining balance
# Display the travel expenses

print("This program calculates and displays travel expenses")

budget = float(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

remaining = budget - gas - accommodation - food

print("\n------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print(f"{'Fuel:':<20}${gas:,.2f}")
print(f"{'Accommodation:':<20}${accommodation:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")
print("---------------------------------------")
print(f"{'Remaining Balance:':<20}${remaining:,.2f}")
