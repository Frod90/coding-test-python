def solution(w,h):    
    def _gcd(a, b):
        if a == 0:
            return b
        return _gcd(b % a, a)
        
    return w * h - (w + h - _gcd(min(w, h), max(w, h)))