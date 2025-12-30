from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    dists = {word:-1 for word in words}
    dists[begin] = 0
    
    q = deque([begin])
    while q:
        current = q.popleft()
        if current == target:
            break
            
        for word in words:
            if dists[word] != -1:
                continue
                
            check_count = 0
            for i in range(len(word)):
                if word[i] != current[i]:
                    check_count += 1
                if check_count > 1:
                    break
            if check_count == 1:
                dists[word] = dists[current] + 1
                q.append(word)

    return dists[target] if dists[target] != -1 else 0