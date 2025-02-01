
n = int(input())

sours = []
bits = []

for _ in range(n):
  sour, bit = map(int, input().split())
  sours.append(sour)
  bits.append(bit)

sourSums = [1]
bitSums = [0]
answers = []

def recur(index):

  if index == n:
    return
  
  for i in range(index, n):

    tmpSour = sourSums[-1] * sours[i]
    tmpBit = bitSums[-1] + bits[i]
    sourSums.append(tmpSour)
    bitSums.append(tmpBit)
    answers.append(abs(tmpSour - tmpBit))
    recur(i + 1)
    sourSums[-1] = sourSums[-1] // sours[i]
    bitSums[-1] = bitSums[-1] - bits[i]

recur(0)
print(min(answers))