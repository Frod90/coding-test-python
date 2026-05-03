def toBase(n, num):
    if num == 0:
        return 0
    
    arr = []
    while num > 0:
        rest = num % n
        num //= n
        arr.append(str(rest))
    return int("".join(arr[::-1]))

def isBase(operation, n):
    a = int(operation[1], n)
    b = int(operation[2], n)
    num = a + b if operation[0] == '+' else a - b
    return int(operation[3]) == toBase(n, num)
    
def solution(expressions):
    max_digit = 0
    operations = []
    results = []
    
    for expression in expressions:
        arr = list(expression.split(" "))
        operation = [arr[1]]
        
        for i in range(0, 5, 2):
            num = arr[i]
            operation.append(num)
            for j in range(len(num)):
                if num[j] != 'X' and int(num[j]) > max_digit:
                    max_digit = int(num[j])
                    
        if arr[4] == 'X':
            results.append(operation)
        else:
            operations.append(operation)
    
    candidates = []
    for base in range(9, max_digit, -1):
        is_base = True
        for operation in operations:
            if not isBase(operation, base):
                is_base = False
                break

        if is_base:
            candidates.append(base)

    answer = []
    for op, a, b, _ in results:
        values = set()

        for base in candidates:
            x = int(a, base)
            y = int(b, base)

            value = x + y if op == '+' else x - y
            values.add(toBase(base, value))

        result = values.pop() if len(values) == 1 else "?"
        answer.append(f"{a} {op} {b} = {result}")
    return answer