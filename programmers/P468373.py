import sys
sys.setrecursionlimit(99999999)
from collections import deque

def bfs(n, links, pipe_type, infections):
    q = deque()
    visit = [False] * (n + 1)
    next_infections = []
    for infection in infections:
        visit[infection] = True
        q.append(infection)
        next_infections.append(infection)
        
    while q:
        current_node = q.popleft()
        for next_node in links[current_node][pipe_type]:
            if not visit[next_node]:
                visit[next_node] = True
                q.append(next_node)
                next_infections.append(next_node)
    return next_infections

def recur(n, links, pipe_type, infections, depth, k):
    if depth > k:
        return len(infections)

    next_infections = bfs(n, links, pipe_type, infections)
    case1 = recur(n, links, (pipe_type + 1) % 3, next_infections, depth + 1, k)
    case2 = recur(n, links, (pipe_type + 2) % 3, next_infections, depth + 1, k)
    return max(case1, case2)

def solution(n, infection, edges, k):
    links = [[[] for _ in range(3)] for _ in range(n + 1)]
    for a, b, t in edges:
        links[a][t - 1].append(b)
        links[b][t - 1].append(a)
    
    answer = 0
    for pipe_type in range(3):
        answer = max(answer, recur(n, links, pipe_type, [infection], 1, k))
    return answer