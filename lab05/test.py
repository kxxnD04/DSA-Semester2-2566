"""AlmostMean"""
def findalmostmean(num):
    """PLS LEAVE ME ALONE"""
    list1 = [input().split() for _ in range(num)]
    list2 = []
    total = 0
    for i in list1:
        total += float(i[-1])
    avg = total/float(num)
    list2.append(avg)
    for i in list1:
        list2.append(float(i[-1]))
    list2.sort(reverse=True)
    ans = 0
    for i in range(len(list2)):
        if list2[i] == avg:
            ans = list2[i+1]
            break
    for i in list1:
        if float(i[-1]) == ans:
            print(i[0], i[1], sep="\t")
findalmostmean(int(input()))