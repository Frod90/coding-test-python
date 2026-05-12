
def solution(n, words):
    s = set()
    before_word = words[0]
    s.add(before_word)
    
    for i in range(1, len(words)):
        word = words[i]
        
        if before_word[-1] != word[0] or word in s:
            return [i % n + 1, i // n + 1]
        
        before_word = word
        s.add(word)
    
    return [0, 0]