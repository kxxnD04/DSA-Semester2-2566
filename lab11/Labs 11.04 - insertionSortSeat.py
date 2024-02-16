"""Labs 11.01 - insertionSort"""
import json as jack
def compare_seat(seat1: str, seat2: str):
    """for seat compare"""
    if seat1[0] != seat2[0]:
        return seat1 >= seat2
    return int(seat1[1:]) >= int(seat2[1:])
def insertion_sort(lis: list, last):
    """index"""
    cut = lis[last+1:]
    lis = lis[:last+1]
    compare = 0
    finish, unfinish = [lis.pop(0)], lis.copy()
    while unfinish:
        first = unfinish.pop(0)
        pointer = len(finish)-1
        while pointer >= 0:
            compare += 1
            if compare_seat(first, finish[pointer]):
                finish.insert(pointer+1, first)
                break
            else:
                if pointer == 0:
                    finish.insert(pointer, first)
            pointer -= 1
        print(finish+unfinish+cut)
    print("Comparison times:", compare)
insertion_sort(jack.loads(input().replace("'", '"')), int(input()))
