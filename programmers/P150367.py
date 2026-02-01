
def solution(numbers):
    def valid(left, right):
        if left == right:
            return True
        
        mid = (left + right) // 2
        left_valid = valid(left, mid - 1)
        right_valid = valid(mid + 1, right)
        
        if not left_valid or not right_valid:
            return False
        
        if bit[mid] == '0':
            for i in range(left, mid):
                if bit[i] == '1':
                    return False
            for i in range(mid + 1, right + 1):
                if bit[i] == '1':
                    return False
        return True
    
    answer = []
    for num in numbers:
        bit = bin(num)[2:]
        k = 1
        while (2**k - 1) < len(bit):
            k += 1
        bit = bit.zfill(2**k - 1)

        if valid(0, len(bit) - 1):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer