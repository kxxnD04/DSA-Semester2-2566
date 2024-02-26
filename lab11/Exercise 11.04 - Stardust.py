"""Exercise 11.04 - Stardust"""
def stardust(lis: list):
    """laong daow"""
    lis.sort()
    print("%.2f\n%.2f\n%.2f" % (sum(lis)/len(lis), lis[(len(lis)//2)] if len(lis)%2\
        else (lis[(len(lis)//2)-1] + lis[(len(lis)//2)])/2,\
        ((sum([i**2 for i in lis]) - (len(lis)*((sum(lis)/len(lis))**2)))/(len(lis)))**0.5))
stardust([int(input()) for _ in range(int(input()))])
