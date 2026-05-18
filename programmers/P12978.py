import heapq

def solution(N, road, K):
    links = [[] for _ in range(N + 1)]
    for a, b, v in road:
        links[a].append((b, v))
        links[b].append((a, v))
    
    INF = float('inf')
    dists = [INF] * (N + 1)
    dists[1] = 0
    q = [(0, 1)]
    
    while q:
        current_value, current_node = heapq.heappop(q)
        if dists[current_node] < current_value:
            continue
            
        for next_node, ev in links[current_node]:
            next_value = current_value + ev
            if next_value < dists[next_node]:
                dists[next_node] = next_value
                heapq.heappush(q, (next_value, next_node))
    
    answer = 0
    for node in range(1, N + 1):
        if dists[node] <= K:
            answer += 1
    return answer