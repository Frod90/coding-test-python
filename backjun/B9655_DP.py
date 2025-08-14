n = int(input())

if n == 1:
  print('SK')
  exit()
elif n == 2:
  print('CY')
  exit()

dp = ['' for _ in range(n + 1)]
dp[1] = 'SK'
dp[2] = 'CY'
dp[3] = 'SK'

for i in range(4, n + 1):
  if dp[i - 1] == 'CY' or dp[i - 3] == 'CY':
    dp[i] = 'SK'
  else:
    dp[i] = 'CY'

print(dp[-1])