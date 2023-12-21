"""Extra Exercise week 2-1"""
def sumofpower2(val_n):
    """return sum of power 2 of number that below n"""
    return sum([i*i for i in range(val_n)])
print(sumofpower2(int(input())))
