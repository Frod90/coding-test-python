import sys
input = sys.stdin.readline

class Node(object):
  def __init__(self, key):
    self.key = key
    self.is_end = False
    self.child = dict()

class Trie:
  def __init__(self):
    self.head = Node(None)

  def insert(self, arr):
    current_node = self.head

    for value in arr:
      if value not in current_node.child:
        current_node.child[value] = Node(value)
      current_node = current_node.child[value]

    current_node.is_end = True

  def recur(self, depth, node):
    print("--" * depth + node.key)
    if node.is_end:
      return
    for key in sorted(node.child):
      self.recur(depth + 1, node.child[key])

  def print(self):
    current_node = self.head

    for key in sorted(current_node.child):
      self.recur(0, current_node.child[key])

n = int(input())
trie = Trie()
for _ in range(n):
  input_data = list(input().rstrip().split(' '))
  trie.insert(input_data[1:])
trie.print()