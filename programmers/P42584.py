def solution(prices):
    answer = [0] * len(prices)
    s = []
    for i, price in enumerate(prices):
        while s and s[-1][0] > price:
            bp, index = s.pop()
            answer[index] = i - index
        s.append((price, i))
    
    while s:
        bp, index = s.pop()
        answer[index] = len(prices) - index - 1
    
    return answer