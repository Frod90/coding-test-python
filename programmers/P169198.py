def solution(m, n, startX, startY, balls):
    answer = []        
    for x, y in balls:
        v = (2 * m)**2 + (2 * n)**2
                
        if not (startY == y and startX > x):
            v = min(v, (startY - y)**2 + (startX + x)**2)
        
        if not (startX == x and startY > y):
            v = min(v, (startY + y)**2 + (startX - x)**2)
            
        if not (startY == y and startX < x):
            v = min(v, (startY - y)**2 + (startX - (2*m - x))**2)
            
        if not (startX == x and startY < y):
            v = min(v, (startY - (2*n - y))**2 + (startX - x)**2)
        
        answer.append(v)

    return answer

