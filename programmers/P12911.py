
def solution(n):
    base = '0' + bin(n)[2:]
    index = base.rfind('01')
    tmp = base[:index] + '10'
    
    rest_one_count = base.count('1') - tmp.count('1')
    rest_zero_count = len(base) - len(tmp) - rest_one_count
    
    for _ in range(rest_zero_count):
        tmp += '0'
    for _ in range(rest_one_count):
        tmp += '1'
    
    return int(tmp, 2)