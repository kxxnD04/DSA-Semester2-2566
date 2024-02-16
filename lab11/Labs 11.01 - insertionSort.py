"""Labs 11.01 - insertionSort"""
import json as jack
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
            if first >= finish[pointer]:
                finish.insert(pointer+1, first)
                break
            else:
                if pointer == 0:
                    finish.insert(pointer, first)
            pointer -= 1
        print(finish+unfinish+cut)
    print("Comparison times:", compare)
insertion_sort(jack.loads(input()), int(input()))
