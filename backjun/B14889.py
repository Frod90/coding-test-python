import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
scores = [list(map(int, input().split())) for _ in range(n)]

def _calc(team):

  total = 0
  for i in range(n // 2):
    for j in range(i + 1, n // 2):
      total += scores[team[i]][team[j]] + scores[team[j]][team[i]]
  
  return total


teams = list(combinations([i for i in range(n)], n // 2))

answer = 100 * n**2
for i in range(len(teams) // 2):
  team_a = teams[i]
  team_b = teams[-i - 1]
  answer = min(answer, abs(_calc(team_a) - _calc(team_b)))

print(answer)