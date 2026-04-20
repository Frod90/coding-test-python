import sys
input = sys.stdin.readline

total_money, company_count = map(int, input().split())
profits = [[0] * (company_count + 1)]
for _ in range(total_money):
  profits.append(list(map(int, input().split())))
dists = [[0] * (total_money + 1) for _ in range(company_count + 1)]
choices = [[0] * (total_money + 1) for _ in range(company_count + 1)]

for company in range(1, company_count + 1):
  for money in range(total_money + 1):
    for k in range(money + 1):
      if dists[company - 1][money - k] + profits[k][company] > dists[company][money]:
        dists[company][money] = dists[company - 1][money - k] + profits[k][company]
        choices[company][money] = k

route = []
index = total_money
for i in range(company_count, 0, -1):
  k = choices[i][index]
  route.append(k)
  index -= k

print(dists[company_count][total_money])
print(*route[::-1])