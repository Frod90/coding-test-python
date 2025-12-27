
def solution(n, computers):
    def recur(node):
        for next_node in range(n):
            if computers[node][next_node] and not visit[next_node]:
                visit[next_node] = True
                recur(next_node)

    answer = 0
    visit = [False] * n
    for node in range(n):
        if not visit[node]:
            answer += 1
            visit[node] = True
            recur(node)
            
    return answer