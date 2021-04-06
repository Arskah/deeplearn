rounds = [1,6,6,6,8,8,8,8,8,8,6]
#max_points = sum(rounds)
feedback = [
  1,
  6,
  6,
  6,
  8,
]


# Number of best rounds
best = 8
sorted = feedback.copy()
sorted.sort(reverse=True)
points = sum(sorted[:best])
grade_edges = [0, 24, 32, 40, 48, 56]
grade = [idx for idx, x in enumerate(grade_edges) if x <= points][-1]

print(f"points: {points}, grade: {grade}")