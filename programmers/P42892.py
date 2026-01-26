import sys
sys.setrecursionlimit(10_000_000)

def solution(nodeinfo):
    def recur(sub_nodes):
        if not sub_nodes:
            return
        
        root = sub_nodes[0]
        left = [n for n in sub_nodes if n[1] < root[1]]
        right = [n for n in sub_nodes if n[1] > root[1]]

        pre_order.append(root[0])
        recur(left)
        recur(right)
        post_order.append(root[0])
        
    nodes = [(i + 1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda x:(-x[2], x[1]))
    
    pre_order = []
    post_order = []
    recur(nodes)
    
    return [pre_order, post_order]