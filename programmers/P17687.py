digits = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

def convert(num, n):
    q, r = divmod(num, n)
    if q == 0:
        return digits[r]
    return convert(q, n) + digits[r]

def getString(length, n):
    st = '0'
    num = 1
    while len(st) < length:
        st += convert(num, n)
        num += 1
    return st

def solution(n, t, m, p):
    length = p + (t - 1) * m
    st = getString(length, n)
    answer = ''
    i = p - 1
    while t > 0:
        answer += st[i]
        t -= 1
        i += m
    return answer