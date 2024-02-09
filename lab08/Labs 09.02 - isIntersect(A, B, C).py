"""Labs 09.02 - isIntersect(A, B, C)"""
import json as j
def is_intersect(aaa: list, bbb: list, ccc: list):
    """try to not use set"""
    return aaa[0] in bbb and aaa[0] in ccc
print(is_intersect(*[j.loads(input()) for _ in range(3)]))
