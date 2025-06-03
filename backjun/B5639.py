import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

nodes = []
while True:
    try:
        nodes.append(int(sys.stdin.readline()))
    except:
        break

def _recur(s, e):
    
    if s > e:
        return

    r = nodes[s]

    m = s + 1
    while m <= e and nodes[m] < r:
        m += 1
    
    _recur(s + 1, m - 1)
    _recur(m, e)
    print(r)
    
_recur(0, len(nodes) - 1)