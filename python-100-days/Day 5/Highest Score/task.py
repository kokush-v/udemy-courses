student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
score_sum = 0
max_score = student_scores[0]
for score in student_scores:
    score_sum += score
    if score > max_score:
        max_score = score

print(max(student_scores))
print(max_score)
print(sum(student_scores))
print(score_sum)
