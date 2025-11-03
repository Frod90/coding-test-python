d = {}
index = 1

def recur(s, depth):
    global index
    if depth == 5:
        return 
    
    for digit in ['A', 'E', 'I', 'O', 'U']:
        d[s + digit] = index
        index += 1
        recur(s + digit, depth + 1)

def solution(word):
    recur('', 0)
    return d[word]