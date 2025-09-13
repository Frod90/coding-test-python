from itertools import permutations

ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b
}

def cal(nums, opers, base_operation):
    tmp_nums, tmp_opers = [nums[0]], []
    for i, op in enumerate(opers):
        if base_operation == op:
            tmp_nums[-1] = ops[op](tmp_nums[-1], nums[i + 1])
        else:
            tmp_nums.append(nums[i + 1])
            tmp_opers.append(op)
    
    return tmp_nums, tmp_opers

def solution(expression):
    nums, operates = [], []
    j = 0
    for i, ch in enumerate(expression):
        if ch == '+' or ch == '*' or ch == '-':
            operates.append(ch)
            nums.append(int(expression[j:i]))
            j = i + 1
    nums.append(int(expression[j:]))
    
    answer = 0
    for per in permutations(set(operates)):
        tmp_nums, tmp_op = nums, operates
        for operation in per:
            tmp_nums, tmp_op = cal(tmp_nums, tmp_op, operation)
        answer = max(answer, abs(tmp_nums[0]))
            
    return answer