def solution(data, col, row_begin, row_end):    
    data.sort(key=lambda x:(x[col - 1], -x[0]))
    answer = 0
    
    for i in range(row_begin - 1, row_end):
        sum_data = 0
        for j in range(len(data[i])):
            sum_data += data[i][j] % (i + 1)
        answer ^= sum_data
    
    return answer