def solution(msg):   
    d = {chr(i) : i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
    next_index = len(d) + 1

    answer = []
    i = 0
    while i < len(msg):
        j = i + 1
        while j < len(msg) and msg[i:j + 1] in d:
            j += 1
        
        if j < len(msg):
            d[msg[i:j + 1]] = next_index
            next_index += 1
        
        answer.append(d[msg[i:j]])
        i = j
        
    return answer