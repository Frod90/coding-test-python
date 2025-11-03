def solution(s):
    graph = []
    for row in s[1:-2].split('},'):
        graph.append(list(map(int, row[1:].split(','))))
    graph.sort(key=lambda x:len(x))
    
    answer = []
    bit = 0
    for row in graph:
        for e in row:
            if 0 == (bit & (1 << e)):
                bit |= (1 << e)
                answer.append(e)
                break
    return answer