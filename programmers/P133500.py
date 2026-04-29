import sys
sys.setrecursionlimit(100_001)

def solution(n, lighthouse):
    def recur(current_node, visit, links):
        nonlocal answer
        
        has_light = True
        for next_node in links[current_node]:
            if not visit[next_node]:
                visit[next_node] = True
                if not recur(next_node, visit, links):
                    has_light = False
        if not has_light:
            answer += 1
        
        return not has_light
    
    links = [[] for _ in range(n + 1)]
    for a, b in lighthouse:
        links[a].append(b)
        links[b].append(a)
        
    visit = [False] * (n + 1)
    visit[1] = True
    answer = 0
    recur(1, visit, links)
    return answer