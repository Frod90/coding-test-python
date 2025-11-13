def solution(arr1, arr2):
    w, h = len(arr2[0]), len(arr1)
    answer = [[0] * w for _ in range(h)]
    
    for y in range(h):
        for x in range(w):
            for k in range(len(arr2)):
                answer[y][x] += arr1[y][k] * arr2[k][x]
    
    return answer