def solution(s):
    st = []
    for digit in s:
        if st and digit == st[-1]:
            st.pop()
        else:
            st.append(digit)
    
    if st:
        return 0
    else:
        return 1