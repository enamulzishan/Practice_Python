print("Welcome to Student Score Tracker System")

names = []
scores = []
students = int(input("Enter the number of students: "))

for i in range(students):
    name = input(f"Enter the name of student {i +1}:")
    score = float(input(f"Enter the score of student {i +1}:"))
    names.append(name)
    scores.append(score)

print("Names", names)
print("Scores", scores)

max_score = max(scores)
min_score = min(scores)
print("Maximum Score:", max_score)
print("Minimum Score:", min_score)

score_tuple = tuple(scores)
print("Scores as Tuple:", score_tuple)
try:
    score_tuple[0] = 100
except TypeError:
    print("Cannot modify tuple, it is immutable.")

if len(score_tuple) > 3:
    score1, score2, score3, *others = score_tuple
    print(f"First:{score1}, Second: {score2}, Third: {score3}")
else:
    print("Not enough scores to unpack.")


total_score = sum(scores)
count = len(scores)
if count > 0:
    average_score = total_score / count
    print("Average Score:", average_score)
else:
    print("No scores to calculate average.")