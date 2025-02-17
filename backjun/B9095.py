
answers = [0] * 12

answers[1], answers[2], answers[3] = 1, 2, 4

for i in range(4, 12):
  answers[i] = answers[i - 1] + answers[i - 2] + answers[i - 3]

for i in range(int(input())):
  n = int(input())
  print(answers[n])
