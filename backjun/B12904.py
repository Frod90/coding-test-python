import sys
input = sys.stdin.readline
sys.setrecursionlimit(2_000)

def recur(arr, is_reversed):
  global answer

  if len(base) == len(arr):

    candidate = ''.join(arr[::-1]) if is_reversed else ''.join(arr)
    if base == candidate:
      answer = 1

    return

  if not is_reversed and arr[-1] == 'A':
    recur(arr[:-1], is_reversed)
  elif is_reversed and arr[0] == 'A':
    recur(arr[1:], is_reversed)

  if not is_reversed and arr[-1] == 'B':
    recur(arr[:-1], not is_reversed)
  elif is_reversed and arr[0] == 'B':
    recur(arr[1:], not is_reversed)

base = input().rstrip()
target = list(input().rstrip())

answer = 0
recur(target, False)
print(answer)