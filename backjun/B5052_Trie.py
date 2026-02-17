import sys
input = sys.stdin.readline

class Node(object):
  def __init__(self, key):
    self.key = key
    self.is_end = False
    self.child = {}

class Trie:
  def __init__(self):
    self.head = Node(None)

  def insert(self, num):
    current = self.head

    for digit in num:
      if digit not in current.child:
        current.child[digit] = Node(digit)
      current = current.child[digit]

    current.is_end = True

  def has_start_with(self, prefix):
    current = self.head

    for digit in prefix:
      if current.is_end:
        return True
      
      if digit not in current.child:
        return False
      
      current = current.child[digit]

    return True

def conduct():
  n = int(input())
  phones = [input().rstrip() for _ in range(n)]

  trie = Trie()
  for phone in phones:
    if trie.has_start_with(phone):
      print("NO")
      return

    trie.insert(phone)
  
  print("YES")

t = int(input())
for _ in range(t):
  conduct()