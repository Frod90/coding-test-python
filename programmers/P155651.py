import heapq

def _parse(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(book_time):
    q = []
    times = []
    for s, e in book_time:
        start, end = _parse(s), _parse(e) + 10
        times.append([start, end])
    
    times.sort()
    for start, end in times:
        if q and start >= q[0]:
            heapq.heappop(q)
        heapq.heappush(q, end)
        
    return len(q)