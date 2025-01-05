
number = int(input())

limit = int(number**0.5)

for i in range(2, limit + 1):

  while(number % i == 0):
    number = number / i
    print(i)

if(number > limit):
  print(int(number))