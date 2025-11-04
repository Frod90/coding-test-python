# 전화번호 목록 42577

def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        a, b = phone_book[i - 1], phone_book[i]
        if len(a) <= len(b) and a == b[:len(a)]:
            return False
        
    return True