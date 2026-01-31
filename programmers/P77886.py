def solution(s):
    answer = []    
    for num in s:
        st = []
        count = 0
        
        for ch in num:
            st.append(ch)
            if len(st) >= 3 and st[-1] == '0' and st[-2] == '1' and st[-3] == '1':
                for _ in range(3):
                    st.pop()
                count += 1
                
        tmp = ''.join(st)
        index = tmp.rfind('0')
        if index == -1:
            answer.append("110" * count + tmp)
        else:
            answer.append(tmp[:index + 1] + "110" * count + tmp[index + 1:])
    
    return answer