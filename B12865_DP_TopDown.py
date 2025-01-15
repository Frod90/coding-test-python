import sys
sys.setrecursionlimit(99999999)

input = sys.stdin.readline

n, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

def recur(i, weight):

  if weight > k:
    return -99999999
  if i == n:
    return 0

  if dp[i][weight] != -1:
    return dp[i][weight]
  
  dp[i][weight] = max(recur(i + 1, weight + table[i][0]) + table[i][1], recur(i + 1, weight))
  return dp[i][weight]

dp = [[-1 for _ in range(100_001)] for _ in range(n)]
print(recur(0, 0))