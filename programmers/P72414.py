def solution(play_time, adv_time, logs):
    def to_seconds(time):
        h, m, s = map(int, time.split(":"))
        return h * 3600 + m * 60 + s
    
    maxi_time = to_seconds(play_time)
    dist = [0] * (maxi_time + 1)
    for log in logs:
        start, end = log.split("-")
        start = to_seconds(start)
        end = to_seconds(end)
        dist[start] += 1
        dist[end] -= 1
    for i in range(1, maxi_time):
        dist[i] += dist[i - 1]
        
    adv_length = to_seconds(adv_time)
    count = sum(dist[:adv_length])
    maxi_count = count
    adv_start_time = 0
    for i in range(adv_length, maxi_time):
        count += dist[i] - dist[i - adv_length]
        if count > maxi_count:
            maxi_count = count
            adv_start_time = i - adv_length + 1
    
    h = adv_start_time // 3600
    m = (adv_start_time % 3600) // 60
    s = adv_start_time % 60
    
    return f"{h:02d}:{m:02d}:{s:02d}"