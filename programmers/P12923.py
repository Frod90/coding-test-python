
def solution(begin, end):
    answer = [1] * (end - begin + 1)
    for i in range(begin, end + 1):
        if i == 1:
            answer[0] = 0
            continue
        
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                tmp_division = i // j
                if tmp_division <= 10_000_000:
                    answer[i - begin] = tmp_division
                    break
                else:
                    answer[i - begin] = j
        
    return answer