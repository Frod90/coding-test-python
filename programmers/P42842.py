def solution(brown, yellow): 
    for height in range(1, int(yellow**0.5) + 1):
        if yellow % height != 0:
            continue
        
        width = yellow // height
        if (height + 2) * (width + 2) - yellow == brown:
            return [width + 2, height + 2]
        
    return []