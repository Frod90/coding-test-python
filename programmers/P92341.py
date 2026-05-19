from collections import defaultdict
from math import ceil

def toMin(time):
    return int(time[:2]) * 60 + int(time[3:])

def solution(fees, records):
    d = defaultdict(list)
    end_time = toMin("23:59")
    
    for record in records:
        info = record.split(" ")
        d[int(info[1])].append(toMin(info[0]))
    
    answer = []
    for key, value in d.items():
        if len(value) % 2 == 1:
            value.append(end_time)
        
        value.sort()
        total_time = 0
        for i in range(0, len(value), 2):
            total_time += value[i + 1] - value[i]
        
        if total_time <= fees[0]:
            answer.append((key, fees[1]))
        else:
            price = fees[1] + ceil((total_time - fees[0]) / fees[2]) * fees[3]
            answer.append((key, price))

    answer.sort()
    return [price for _, price in answer]