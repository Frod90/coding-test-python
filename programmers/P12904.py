def solution(s):
    n = len(s)
    def cal(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left + 1 - 2
    
    answer = 1
    for i in range(n):
        answer = max(answer, cal(i, i))
        answer = max(answer, cal(i, i + 1))
    return answer