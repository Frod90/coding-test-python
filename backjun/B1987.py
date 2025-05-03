import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

h, w = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(h)]
visited_states = set()

def dfs(x, y, visited, count):
    
    global answer

    if (x, y, visited) in visited_states:
        return
    
    visited_states.add((x, y, visited))
    answer = max(answer, count)

    for ex, ey in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nx, ny = x + ex, y + ey

        if 0 <= nx < w and 0 <= ny < h:
            bit = 1 << (ord(graph[ny][nx]) - ord('A'))

            if not (visited & bit):
                dfs(nx, ny, visited | bit, count + 1)

start_bit = 1 << (ord(graph[0][0]) - ord('A'))
answer = 0
dfs(0, 0, start_bit, 1)
print(answer)