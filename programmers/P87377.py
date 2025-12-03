from itertools import combinations
from collections import defaultdict

def solution(line):
    d = defaultdict(set)
    for a, b in combinations(line, 2):
        lower = a[0] * b[1] - a[1] * b[0]
        if lower == 0:
            continue
        
        x_upper = a[1] * b[2] - a[2] * b[1]
        y_upper = a[2] * b[0] - a[0] * b[2]
        
        if x_upper % lower == 0 and y_upper % lower == 0:
            d[y_upper // lower].add(x_upper // lower)
    
    y_min, y_max = min(d.keys()), max(d.keys())
    x_min = min(min(values) for values in d.values())
    x_max = max(max(values) for values in d.values())
    
    answer = []
    for y in range(y_max, y_min - 1, -1):
        row = ['.'] * (x_max - x_min + 1)
        
        if y in d:
            for x in d[y]:
                row[x - x_min] = '*'
        
        answer.append(''.join(row))
    
    return answer