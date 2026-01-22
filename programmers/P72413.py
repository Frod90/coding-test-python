import heapq

def solution(n, s, a, b, fares):
    def di(start_node):
        dists = [float('inf')] * (n + 1)
        dists[start_node] = 0
        q = [(0, start_node)]
        while q:
            value, current = heapq.heappop(q)
            if dists[current] < value:
                continue
                
            for next_node, ev in links[current]:
                next_value = value + ev
                if next_value < dists[next_node]:
                    dists[next_node] = next_value
                    heapq.heappush(q, (next_value, next_node))
        return dists
        
    links = [[] for _ in range(n + 1)]
    for node_a, node_b, cost in fares:
        links[node_a].append((node_b, cost))
        links[node_b].append((node_a, cost))
    
    dists_a = di(a)
    dists_b = di(b)
    dists_s = di(s)
    
    answer = float('inf')
    for i in range(1, n + 1):
        answer = min(answer, dists_a[i] + dists_b[i] + dists_s[i])
    return answer