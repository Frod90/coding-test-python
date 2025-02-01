import sys
input = sys.stdin.readline

n = int(input())
base = list(map(int, input().split()))

m = int(input())
compare = list(map(int, input().split()))

base.sort()

def find(a):
    
    i, j = 0, n - 1

    while i <= j:
        mid = (i + j) // 2
        if a == base[mid]:
            return 1
        elif a > base[mid]:
            i = mid + 1
        else:
            j = mid - 1
            
    return 0

answers = [find(a) for a in compare]
print(*answers)
