n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
  v = i

  for j in range(int(i**(0.5)), 0, -1):
    tmp = j * j

    if i == tmp:
      v = 1
      break
    else:
      v = min(v, dp[i - tmp] + 1)

  dp[i] = v

print(dp[-1])