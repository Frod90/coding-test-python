from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs():
        dists = [-1] * (n + 1)
        dists[1] = 0
        q = deque([1])
        while q:
            node = q.popleft()
            for next_node in graph[node]:
                if dists[next_node] == -1:
                    dists[next_node] = dists[node] + 1
                    q.append(next_node)
        
        maxi = max(dists)
        return dists.count(maxi)
    
    return bfs()