from itertools import combinations

l, c = map(int, input().split())
chars = list(input().split())
chars.sort()

for combi in combinations(chars, l):

  tmp = set(['a', 'e', 'i', 'o', 'u'])
  tmp.update(combi)

  leng = len(tmp)
  if leng < 7 or leng == l + 5:
    continue

  print("".join(combi))