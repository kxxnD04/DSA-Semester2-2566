"""Point Sorting"""
def pointso_rt(num):
    """main function"""
    for _ in range(num):
        lis = [list(map(int, input().split())) for _ in range(int(input()))]
        lis.sort(key=lambda x: (x[0] + x[-1], x[0]))
        for i in lis:
            print(*i)
pointso_rt(int(input()))
