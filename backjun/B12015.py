
n = int(input())
nums = list(map(int, input().split()))
arr = [nums[0]]

def _cal(num):

  start, end = 0, len(arr) - 1
  
  while start <= end:

    mid = (start + end) // 2

    if arr[mid] == num:
      return mid
    elif arr[mid] > num:
      end = mid - 1
    else:
      start = mid + 1

  return start

for num in nums:
  if arr[-1] < num:
    arr.append(num)
  else:
    idx = _cal(num)
    arr[idx] = num

print(len(arr))