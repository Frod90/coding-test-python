import heapq

def solution(jobs):
    jobs.sort()
    
    heap = []
    time = 0
    i = 0
    total = 0
    
    while i < len(jobs) or heap:
        while i < len(jobs) and jobs[i][0] <= time:
            request, work = jobs[i]
            heapq.heappush(heap, (work, request))
            i += 1
        
        if heap:
            work, request = heapq.heappop(heap)
            time += work
            total += time - request
        else:
            time = jobs[i][0]
    
    return total // len(jobs)
