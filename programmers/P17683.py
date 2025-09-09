def solution(m, musicinfos):
    def replaceMelody(m):
        tmp = []
        for melody in m:
            if melody == '#':
                tmp[-1] = chr(ord(tmp[-1]) - ord('A') + ord('a'))
            else:
                tmp.append(melody)
        return ''.join(tmp)
    
    def calRunningTime(start, end):
        sh, sm = start.split(':')
        eh, em = end.split(':')
        startTime, endTime = int(sh) * 60 + int(sm), int(eh) * 60 + int(em)
        return endTime - startTime
                            
    baseMelody = replaceMelody(m)
    candidates = []
    for i, info in enumerate(musicinfos):
        start, end, name, melody = info.split(',')
        
        runningTime = calRunningTime(start, end)
        tmp = replaceMelody(melody)
        length = len(tmp)

        repeatCount, index = runningTime // length, runningTime % length
        if runningTime > len(tmp):
            tmp = tmp * repeatCount + tmp[:index]
        elif runningTime < len(tmp):
            tmp = tmp[:index]
        
        if baseMelody in tmp:
            candidates.append([runningTime, i, name])
    
    if not candidates:
        return "(None)"
    
    candidates.sort(key=lambda x:(-x[0], x[1]))
    return candidates[0][2]