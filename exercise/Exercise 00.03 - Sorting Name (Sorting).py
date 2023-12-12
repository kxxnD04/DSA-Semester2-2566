"""sorting without sort or sorted"""
def sor_t(list1):
    """SORT (MERGE SORT)"""
    try:
        while len(list1) > 1:
            first, second, final = list1.pop(0), list1.pop(0), []
            while first and second: #compare each element in each list in list1
                if first[0] > second[0]:
                    final.append(second.pop(0))
                else:
                    final.append(first.pop(0))
            list1.append((final+first+second)) #append the merged list
        print(*list1[0], sep='\n')
    except (EOFError, IndexError):
        return
sor_t([[input()] for _ in range(int(input()))])
