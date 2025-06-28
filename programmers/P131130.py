
def solution(cards):
    answer = 0
    visit  = [False] * len(cards)
    
    def _open(i):
        if visit[i]:
            return 0
        visit[i] = True
        return _open(cards[i] - 1) + 1
    
    lengths = []
    for i in range(len(cards)):
        tmp = _open(i)
        if tmp > 0:
            lengths.append(tmp)

    if len(lengths) < 2:
        return 0
    
    lengths.sort()
    return lengths[-1] * lengths[-2]
