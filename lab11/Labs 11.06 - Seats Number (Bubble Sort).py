"""Labs 11.03 - bubbleSort()"""
import json as jack
def compare_seat(seat1: str, seat2: str):
    """for seat compare"""
    if seat1[0] != seat2[0]:
        return seat1 < seat2
    return int(seat1[1:]) < int(seat2[1:])
def bubble_sort(lis: list, last: int):
    """selection sort"""
    compare = 0
    current = 0
    sor = False
    while current <= last and sor is False:
        walker = last
        sor = True
        while walker > current:
            compare += 1
            if compare_seat(lis[walker], lis[walker-1]):
                sor = False
                lis[walker], lis[walker-1] = lis[walker-1], lis[walker]
            walker -= 1
        current += 1
        print(lis)
    print("Comparison times:", compare)
bubble_sort(jack.loads(input().replace("'", '"')), int(input()))
