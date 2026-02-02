from itertools import permutations

def solution(n, weak, dist):
    expand_weak = weak + [w + n for w in weak]

    INF = float('inf')
    answer = INF
    for start_index in range(len(weak)):
        for perm in permutations(dist):
            count = 1
            position = expand_weak[start_index] + perm[0]
            
            for i in range(1, len(weak)):
                index = start_index + i
                if expand_weak[index] > position:
                    count += 1
                    if count > len(perm):
                        count = INF
                        break
                        
                    position = expand_weak[index] + perm[count - 1]
                    
            answer = min(answer, count)
    
    return answer if answer != INF else -1