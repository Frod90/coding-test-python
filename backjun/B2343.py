
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

def calTime(time):

  count = 1
  tmpSum = 0
  for number in numbers:
    
    if tmpSum + number > time:
      tmpSum = number
      count += 1
    else:
      tmpSum += number

  return count <= m

start = max(numbers)
end = 100_000 * 10_000 + 1
answer = 0
while start <= end:

  mid = (start + end) // 2
  isAnswer = calTime(mid)

  if isAnswer:
    answer = mid
    end = mid - 1
  else:
    start = mid + 1

print(answer)