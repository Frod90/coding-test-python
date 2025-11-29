
from collections import defaultdict
from bisect import bisect_left

def solution(priorities, location):
    d = defaultdict(list)
    for i, v in enumerate(priorities):
        d[v].append(i)

    base_index = 0
    arr = []
    for key in sorted(d.keys(), reverse = True):
        indexs = d[key]
        s = bisect_left(indexs, base_index)
        for index in indexs[s:]:
            arr.append(index)
        for index in indexs[:s]:
            arr.append(index)
        base_index = arr[-1]

    return arr.index(location) + 1