# Nicolas Posso
# 11/02/2026
# P4LAB2 - Multiplication Table

# Pseudocode:
# 1. Ask the user to enter an integer.
# 2. Check if the number is 0 or greater.
# 3. If the number is positive or zero, display its multiplication table from 1 to 12.
# 4. If the number is negative, display a message that negative values are not accepted.
# 5. Ask the user if they want to run the program again.
# 6. If the user enters yes, repeat the program.
# 7. If the user enters no, exit the program.

run_again = "yes"

while run_again == "yes":

    number = int(input("Enter an integer: "))

    if number >= 0:
        for count in range(1, 13):
            print(number, "*", count, "=", number * count)

    else:
        print("Negative values are not accepted.")

    run_again = input("Would you like to run the program again? ").lower()

print("Exiting program...")