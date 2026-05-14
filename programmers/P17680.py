
from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    
    for city in cities:
        city = city.lower()
        
        if cache and city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            cache.append(city)
            while len(cache) > cacheSize:
                cache.popleft()
    
    return answer