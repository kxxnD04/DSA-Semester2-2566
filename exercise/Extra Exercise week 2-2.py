"""Extra Exercise week 2-2"""
def sumofpower2(val_n):
    """return sum of power 2 of number that below n and is odd"""
    return sum([i*i for i in range(val_n) if i%2])
print(sumofpower2(int(input())))
