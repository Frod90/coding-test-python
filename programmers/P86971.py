from collections import deque

def bfs(links, n, a, b):
    visit = [False] * (n + 1)
    visit[a] = visit[b] = True    
    q = deque([a])
    
    count = 1
    while q:
        bi = q.popleft()
        for ni in links[bi]:
            if not visit[ni]:
                visit[ni] = True
                q.append(ni)
                count += 1
                
    return abs((n - count) - count)

def solution(n, wires):
    links = [[] for _ in range(n + 1)]
    for a, b in wires:
        links[a].append(b)
        links[b].append(a)

    return min(bfs(links, n, a, b) for a, b in wires)