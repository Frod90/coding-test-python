import sys
sys.setrecursionlimit(99999999)

def solution(spell, dic):
    arr = []
    visited = [0 for _ in range(len(spell))]

    def _makeWord(i, word):
        
        if i == len(spell):
            arr.append(word)
            return
        
        for j in range(len(spell)):
            
            if visited[j] == 1:
                continue
            
            visited[j] = 1
            _makeWord(i + 1, word + spell[j])
            visited[j] = 0
    _makeWord(0, "")
    
    answer = 2    
    for compare in dic:
        if compare in arr:
            answer = 1
            break
    return answer