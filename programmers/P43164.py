import sys
sys.setrecursionlimit(10_001)
from collections import defaultdict

def solution(tickets):
    links = defaultdict(list)
    for a, b in tickets:
        links[a].append([b, False])
    for link in links.values():
        link.sort(key=lambda x:x[0])
    
    def recur(node):
        if len(arr) == len(tickets) + 1:
            return True
        
        for i, (next_node, visit) in enumerate(links[node]):
            if not visit:
                links[node][i][1] = True
                arr.append(next_node)
                if recur(next_node):
                    return True
                arr.pop()
                links[node][i][1] = False
        return False
    
    arr = ["ICN"]
    recur("ICN")
    return arr