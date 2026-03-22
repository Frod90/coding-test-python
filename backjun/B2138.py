import sys
input = sys.stdin.readline

n = int(input())
num_infos = list(map(int, list(input().rstrip())))
target = input().rstrip()
target_infos = list(map(int, list(target)))

case1_info = num_infos[:]
case2_info = num_infos[:]
INF = float('inf')

case1 = 0
for i in range(1, n):
  if case1_info[i - 1] == target_infos[i - 1]:
    continue

  for j in range(i - 1, min(i + 2, n)):
    case1_info[j] = (case1_info[j] + 1) % 2
  case1 += 1
if "".join(map(str, case1_info)) != target:
  case1 = INF

case2_info[0] = (case2_info[0] + 1) % 2
case2_info[1] = (case2_info[1] + 1) % 2
case2 = 1
for i in range(1, n):
  if case2_info[i - 1] == target_infos[i - 1]:
    continue

  for j in range(i - 1, min(i + 2, n)):
    case2_info[j] = (case2_info[j] + 1) % 2
  case2 += 1
if "".join(map(str, case2_info)) != target:
  case2 = INF

answer = min(case1, case2)
print(answer if answer != INF else -1)