
class Node(object):
    def __init__(self, key):
        self.key = key
        self.is_end = False
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for digit in string:
            if digit not in current_node.child:
                current_node.child[digit] = Node(digit)
            current_node = current_node.child[digit]
    
        current_node.is_end = True

    def has_start_with(self, prefix):
        current_node = self.head

        for digit in prefix:
            if current_node.is_end:
                return True
            if digit not in current_node.child:
                return False
            current_node = current_node.child[digit]

        return True

def solution(phone_book):
    trie = Trie()
    for phone_num in phone_book:
        if trie.has_start_with(phone_num):
            return False
        trie.insert(phone_num)
    
    return True