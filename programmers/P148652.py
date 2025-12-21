def cal(n, d, s, target_index):
    if n == d:
        return 1
    
    unit = 5**(n - d - 1)
    if s + unit * 2 <= target_index < s + unit * 3:
        return 4 ** (n - d - 1) * 2
    
    for section in [0, 1]:
        if s + unit * section <= target_index < s + unit * (section + 1):
            return 4 ** (n - d - 1) * section + cal(
                n, d + 1, s + unit * section, target_index
            )
        
    for section in [3, 4]:
        if s + unit * section <= target_index < s + unit * (section + 1):
            return 4 ** (n - d - 1) * (section - 1) + cal(
                n, d + 1, s + unit * section, target_index
            )

    return 0

def solution(n, l, r):
    upper = cal(n, 0, 0, r - 1) if r > 0 else 0
    lower = cal(n, 0, 0, l - 2) if l > 0 else 0

    return upper - lower