from math import gcd
from functools import reduce

def gcd_arr(arr):
    return reduce(gcd, arr)

def is_valid(arr, divi):
    if divi == 1:
        return False
    return all(x % divi != 0 for x in arr)

def solution(arrayA, arrayB):
    answer = 0
    gcdA, gcdB = gcd_arr(arrayA), gcd_arr(arrayB)

    if is_valid(arrayB, gcdA):
        answer = max(answer, gcdA)
    if is_valid(arrayA, gcdB):
        answer = max(answer, gcdB)

    return answer
