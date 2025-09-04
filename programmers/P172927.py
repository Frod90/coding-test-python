def solution(picks, minerals):
    n = min(len(minerals), sum(picks) * 5)
    sections = []
    for i in range(0, n, 5):
        tmp = [0, 0, 0]
        for j in range(i, min(i + 5, n)):
            if minerals[j] == "diamond":
                tmp[0] += 1
            elif minerals[j] == "iron":
                tmp[1] += 1
            else:
                tmp[2] += 1
        sections.append(tmp)
    sections.sort(key=lambda x:(-x[0], -x[1], -x[2]))

    answer = 0
    for dia, iron, stone in sections:
        if picks[0] > 0:
            picks[0] -= 1
            answer += dia + iron + stone
        elif picks[1] > 0:
            picks[1] -= 1
            answer += dia * 5 + iron + stone
        elif picks[2] > 0:
            picks[2] -= 1
            answer += dia * 25 + iron * 5 + stone
        else:
            break
    
    return answer