def compress(s, length):
    n = len(s)
    before_word = s[:length]
    compressed_length = 0
    count = 1
    for i in range(length, n + length, length):
        current_word = s[i:i + length]
        if current_word == before_word:
            count += 1
            continue
        
        compressed_length += len(before_word)
        if count > 1:
            compressed_length += len(str(count))
        
        count = 1
        before_word = current_word
    
    return compressed_length
    

def solution(s):
    answer = len(s)
    for length in range(1, len(s) // 2 + 1):
        answer = min(answer, compress(s, length))
    return answer