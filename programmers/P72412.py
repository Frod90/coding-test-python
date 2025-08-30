from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    db = defaultdict(list)
    for each in info:
        tmp = each.split(" ")
        score = int(tmp.pop())
        for i in range(len(tmp) + 1):
            for combi in combinations(tmp, i):
                key = "_".join(combi)
                db[key].append(score)
    for key in db:
        db[key].sort()

    answer = []
    for q in query:
        q = q.replace("and", "")
        tmp = q.split()
        score = int(tmp.pop())
        key = "_".join(k for k in tmp if k != '-')
        
        arr = db.get(key, [])
        index = bisect_left(arr, score)
        answer.append(len(arr) - index)
    
    return answer