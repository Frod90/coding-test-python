
string = input()

minusSplits = list(string.split("-"))

plusSplit = []
for minusSplit in minusSplits:
  plusSplit.append(list(map(int, minusSplit.split("+"))))

answer = sum(plusSplit[0])
for i in range(1, len(plusSplit)):
  answer -= sum(plusSplit[i])

print(answer)