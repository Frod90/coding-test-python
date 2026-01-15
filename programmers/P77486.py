def solution(enroll, referral, seller, amount):
    links = {enroll[i]:r for i, r in enumerate(referral)}
    dists = {e:0 for e in enroll}
    
    for i, s in enumerate(seller):
        sell_amount = amount[i] * 100
        send = sell_amount // 10
        dists[s] += sell_amount - send
        
        parent = links[s]
        while parent != "-" and send > 0:
            tmp = send // 10
            dists[parent] += send - tmp
            parent = links[parent]
            send = tmp
            
    return [dists[e] for e in enroll]