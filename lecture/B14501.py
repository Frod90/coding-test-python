
n = int(input())

times = []
pays = []

for _ in range(n):
  time, pay = map(int, input().split())
  times.append(time)
  pays.append(pay)

arr = []
answers = []
def recur(i):

  if i >= n:
    answer = calculatePay()
    answers.append(answer)
    return
  
  arr.append(i)
  recur(i + times[i])
  arr.pop()
  recur(i + 1)

def calculatePay():

  sum = 0
  for i in arr:
    if i + times[i] <= n:
      sum += pays[i]

  return sum

recur(0)
print(max(answers))