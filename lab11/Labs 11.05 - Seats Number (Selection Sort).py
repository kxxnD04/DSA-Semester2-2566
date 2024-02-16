"""Labs 11.02 - selectionSort()"""
import json as jack
def compare_seat(seat1: str, seat2: str):
    """for seat compare"""
    if seat1[0] != seat2[0]:
        return seat1 < seat2
    return int(seat1[1:]) < int(seat2[1:])
def selection_sort(lis: list, last: int):
    """selection sort"""
    compare = 0
    current = 0
    while current < last:
        mi_n = current
        walker = current +1
        while walker <= last:
            compare += 1
            if compare_seat(lis[walker], lis[mi_n]):
                mi_n = walker
            walker += 1
        lis[current], lis[mi_n] = lis[mi_n], lis[current]
        current += 1
        print(lis)
    print("Comparison times:", compare)
selection_sort(jack.loads(input().replace("'", '"')), int(input()))
