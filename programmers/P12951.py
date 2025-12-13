def solution(s):
    words = s.split(" ")

    answer = []
    for i, word in enumerate(words):
        if word == "":
            answer.append("")
            continue
        
        tmp = []
        if word[0].isalpha() and word[0].islower():
            tmp.append(word[0].upper())
        else:
            tmp.append(word[0])
        
        for i in range(1, len(word)):
            if word[i].isalpha() and word[i].isupper():
                tmp.append(word[i].lower())
            else:
                tmp.append(word[i])
                
        answer.append(''.join(tmp))

    return " ".join(answer)