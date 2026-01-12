def solution(sequence):
    subtotal_a, subtotal_b = 0, 0
    answer = 0
    for i, v in enumerate(sequence):
        a = v if i % 2 == 0 else -v
        b = -v if i % 2 == 0 else v
        
        subtotal_a = max(a, subtotal_a + a)
        subtotal_b = max(b, subtotal_b + b)
        answer = max(answer, subtotal_a, subtotal_b)
    
    return answer