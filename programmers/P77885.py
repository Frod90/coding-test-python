def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
            continue
        
        bit = '0' + bin(num)[2:]
        index = bit.rfind('0')
        tmp = bit[:index] + "10" + bit[index + 2:]
        answer.append(int(tmp, 2))
    
    return answer