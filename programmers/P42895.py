def solution(N, number):
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    if b == 0:
                        continue
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a // b)
                    dp[i].add(a * b)
        
        if number in dp[i]:
            return i
    
    return -1