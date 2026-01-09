import heapq

def solution(n, costs):
    links = [[] for _ in range(n)]
    for a, b, c in costs:
        links[a].append((b, c))
        links[b].append((a, c))
    
    q = [(0, 0)]
    visit = [False] * n
    count = 0
    answer = 0
    while q:
        value, current = heapq.heappop(q)
        if visit[current]:
            continue
        
        visit[current] = True
        answer += value
        count += 1
        if count == n:
            break
        
        for next_node, next_value in links[current]:
            heapq.heappush(q, (next_value, next_node))
    
    return answer