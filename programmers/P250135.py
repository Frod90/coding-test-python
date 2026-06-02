def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    if m1 == 0 and s1 == 0:
        if h1 == 0 or h1 == 12:
            answer += 1
	
    if h1 < 12 and 12 <= h2:
        answer -= 1
	
    hSp = 360 / (3600 * 12)
    mSp = 360 / 3600
    sSp = 360 / 60

    hsGapSeconds = 360 / (sSp - hSp)
    msGapSeconds = 360 / (sSp - mSp)

    time1 = h1 * 3600 + m1 * 60 + s1
    time2 = h2 * 3600 + m2 * 60 + s2

    hMeet1 = int(time1 / hsGapSeconds)
    hMeet2 = int(time2 / hsGapSeconds)

    mMeet1 = int(time1 / msGapSeconds)
    mMeet2 = int(time2 / msGapSeconds)

    answer += hMeet2 + mMeet2 - hMeet1 - mMeet1
    return answer