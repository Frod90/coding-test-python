def solution(s):    
    st = []
    
    for digit in s:
        if digit == ')':
            if st and st[-1] == '(':
                st.pop()
                continue
            else:
                return False        
        
        st.append('(')
    
    if st:
        return False
    
    return True