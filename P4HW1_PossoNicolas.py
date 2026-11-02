# Nicolas Posso
# 11/02/2026
# P4HW1 - Score Average
# This program collects scores, drops the lowest score, and calculates the average and letter grade.

# Pseudocode:
# 1. Ask the user how many scores they want to enter.
# 2. Create an empty list to store the scores.
# 3. Use a loop to collect each score.
# 4. Check if each score is between 0 and 100.
# 5. If a score is invalid, display an error and ask for it again.
# 6. Add each valid score to the list.
# 7. Find and display the lowest score.
# 8. Remove the lowest score from the list.
# 9. Display the modified score list.
# 10. Calculate and display the average.
# 11. Determine and display the letter grade.

number_of_scores = int(input("How many scores do you want to enter? "))

scores = []

for count in range(1, number_of_scores + 1):

    score = float(input("Enter score #" + str(count) + ": "))

    while score < 0 or score > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #" + str(count) + " again: "))

    scores.append(score)

lowest_score = min(scores)

scores.remove(lowest_score)

average = sum(scores) / len(scores)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print()
print("-------------Results-------------")
print("Lowest Score  :", lowest_score)
print("Modified List :", scores)
print("Scores Average: {:.2f}".format(average))
print("Grade         :", grade)
print("---------------------------------")