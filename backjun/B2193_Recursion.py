import sys
sys.setrecursionlimit(100000)

n = int(input())

dp = [[-1 for _ in range(n + 1)] for _ in range(2)]

def _recur(bv, i):
    if dp[bv][i] != -1:
        return dp[bv][i]

    if i == n:
        return 1

    total = 0

    if bv == 1:
        total = _recur(0, i + 1)
    else:
        total = _recur(0, i + 1) + _recur(1, i + 1)

    dp[bv][i] = total
    return total

print(_recur(1, 1))