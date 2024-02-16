"""Labs 11.02 - selectionSort()"""
import json as jack
def selection_sort(lis: list, last: int):
    """selection sort"""
    compare = 0
    current = 0
    while current < last:
        mi_n = current
        walker = current +1
        while walker <= last:
            compare += 1
            if lis[walker] < lis[mi_n]:
                mi_n = walker
            walker += 1
        lis[current], lis[mi_n] = lis[mi_n], lis[current]
        current += 1
        print(lis)
    print("Comparison times:", compare)
selection_sort(jack.loads(input()), int(input()))
