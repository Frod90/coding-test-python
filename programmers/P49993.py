def isA(skill, tree):
    index = 0
    for t in tree:
        if t in skill:
            if t == skill[index]:
                index += 1
                continue
            else:
                return False
    return True

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        if isA(skill, tree):
            answer += 1
    return answer