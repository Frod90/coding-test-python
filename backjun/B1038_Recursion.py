
answers = [i for i in range(10)]

def _recur(i, n):

  if n > 9:
    return

  tmp = int(i[-1])

  for j in range(tmp):
    answers.append(int(i + str(j)))
    _recur(i + str(j), n + 1)

for i in range(1, 10):
  _recur(str(i), 0)
answers.sort()

n = int(input())

if n >= len(answers):
  print(-1)
else:
  print(answers[n])