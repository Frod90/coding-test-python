
n = int(input())
nums = list(map(int, input().split()))

numSet = sorted(set(nums))
comp ={numSet[i] : i for i in range(len(numSet))}

answers = [comp[num] for num in nums]
print(*answers)
