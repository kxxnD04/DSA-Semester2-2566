"""Labs 11.03 - bubbleSort()"""
import json as jack
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
            if lis[walker] < lis[walker-1]:
                sor = False
                lis[walker], lis[walker-1] = lis[walker-1], lis[walker]
            walker -= 1
        current += 1
        print(lis)
    print("Comparison times:", compare)
bubble_sort(jack.loads(input()), int(input()))
