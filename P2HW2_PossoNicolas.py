# Nicolas Posso
# October 14, 2026
# P2HW2
# This code calculates statistics for module grades

# Pseudocode:
# Ask the user to enter grades for six modules
# Store all six grades in a list
# Calculate the lowest grade
# Calculate the highest grade
# Calculate the sum of the grades
# Calculate the average of the grades
# Display the results with proper formatting

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

grades = [module1, module2, module3, module4, module5, module6]

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

print("\n------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest:>10.1f}")
print(f"{'Highest Grade:':<20}{highest:>10.1f}")
print(f"{'Sum of Grades:':<20}{total:>10.1f}")
print(f"{'Average:':<20}{average:>10.2f}")
print("----------------------------------------------")
