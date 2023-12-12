"""QUICK QUICK QUICK"""
def quickSort(mylist):
    """for main func"""
    quickSortHelper(mylist,0,len(mylist)-1)
    return mylist
def quickSortHelper(mylist,first,last):
    """for quick sort func"""
    if first<last:
        splitpoint = partition(mylist,first,last)
        quickSortHelper(mylist,first,splitpoint-1)
        quickSortHelper(mylist,splitpoint+1,last)
def partition(mylist,first,last):
    """part of quicksort"""
    pivotvalue = mylist[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and mylist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while mylist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            temp = mylist[leftmark]
            mylist[leftmark] = mylist[rightmark]
            mylist[rightmark] = temp
    temp = mylist[first]
    mylist[first] = mylist[rightmark]
    mylist[rightmark] = temp
    return rightmark
def main():
    """main func for quick sort"""
    mylist = [input() for _ in range(int(input()))]
    print(*quickSort(mylist), sep='\n')
main()
