
n = int(input())

coordinates = []
x_coordinates = []
y_coordinates = []

for _ in range(n):
  a, b = map(int, input().split())
  coordinates.append([a, b])
  x_coordinates.append(a)
  y_coordinates.append(b)


answers = [2_000_000 * 50] * n

for x in x_coordinates:
  for y in y_coordinates:

    distances = []

    for xi, yi in coordinates:
      distance = abs(x - xi) + abs(y - yi)
      distances.append(distance)

    distances.sort()
    answer = 0

    for i in range(n):
      answer += distances[i]
      answers[i] = min(answers[i], answer)

print(*answers)
