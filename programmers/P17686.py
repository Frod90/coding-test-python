def parse(file):
    head, num, tail = '', '', ''
    n = len(file)
    i = 0
    while i < n and not file[i].isdigit():
        head += file[i]
        i += 1
    while i < n and file[i].isdigit():
        num += file[i]
        i += 1
    tail = file[i:]
    return head, num, tail

def solution(files):
    return sorted(files, key=lambda x: (parse(x)[0].lower(), int(parse(x)[1])))