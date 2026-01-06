def solution(user_id, banned_id):
    def _check(u, b):
        if len(b) != len(u):
            return False
        
        for i in range(len(b)):
            if b[i] == '*':
                continue
            if b[i] != u[i]:
                return False
        return True
    
    def recur(index):
        if len(banned_id) == index:
            answers.add(frozenset(arr))
            return
        
        for user in candidates[index]:
            if user not in arr:
                arr.append(user)
                recur(index + 1)
                arr.pop()

    candidates = {i:[] for i in range(len(banned_id))}
    for i, b in enumerate(banned_id):
        for u in user_id:
            if _check(u, b):
                candidates[i].append(u)
                
    answers = set()
    arr = []
    recur(0)
    return len(answers)