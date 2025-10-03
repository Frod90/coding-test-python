from collections import defaultdict

def solution(record):
    d = defaultdict(str)
    arr = []
        
    for r in record:
        tmp = r.split(" ")
        
        if tmp[0] == "Enter":
            arr.append([tmp[1], "님이 들어왔습니다."])
            d[tmp[1]] = tmp[2]
        elif tmp[0] == "Leave":
            arr.append([tmp[1], "님이 나갔습니다."])
        elif tmp[0] == "Change":
            d[tmp[1]] = tmp[2]

    answer = [d[r[0]] + r[1] for r in arr]
    return answer

