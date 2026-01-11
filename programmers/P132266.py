from collections import deque

def solution(n, roads, sources, destination):
    links = [[] for _ in range(n + 1)]
    for a, b in roads:
        links[a].append(b)
        links[b].append(a)
    
    dists = [-1] * (n + 1)
    dists[destination] = 0
    
    q = deque()
    q.append(destination)
    while q:
        current = q.popleft()
        for next_node in links[current]:
            if dists[next_node] == -1:
                dists[next_node] = dists[current] + 1
                q.append(next_node)

    answer = [dists[node] for node in sources]
    return answer