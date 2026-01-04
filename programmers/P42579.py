def solution(genres, plays):
    d = dict()
    details = dict()
    for i, genre in enumerate(genres):
        d[genre] = d.get(genre, 0) + plays[i]
        details.setdefault(genre, []).append((i, plays[i]))
        
    sorted_d = sorted(d.items(), key=lambda x:-x[1])
    answer = []
    for key, _ in sorted_d:
        sorted_values = sorted(details[key], key=lambda x:-x[1])
        for i in range(min(2, len(sorted_values))):
            answer.append(sorted_values[i][0])
        
    return answer