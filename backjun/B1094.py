
n = int(input())
arr = [64]
arr_sum = 64

while arr_sum != n:
  p = arr.pop()
  dv = p // 2
  arr.append(dv)

  if arr_sum - dv >= n:
    arr_sum -= dv
  else:
    arr.append(dv)

print(len(arr))

