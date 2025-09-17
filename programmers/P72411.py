from collections import defaultdict
from itertools import combinations

def count(order, n, dic):
    arr = sorted(list(order))
    for combi in combinations(arr, n):
        st = "".join(combi)
        dic[st] += 1

def solution(orders, course):
    answer = []
    for n in course:
        dic = defaultdict(int)
        for order in orders:
            count(order, n, dic)
        
        tmp = []
        max_count = 0
        for key in dic:
            value = dic[key]
            if value < 2:
                continue
            if value > max_count:
                tmp = [key]
                max_count = value
            elif value == max_count:
                tmp.append(key)
        
        for key in tmp:
            answer.append(key)
    
    answer.sort()
    return answer