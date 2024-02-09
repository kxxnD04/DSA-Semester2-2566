"""CalculatorV2"""
def calculator(num, count=0):
    """count how many press"""
    if num == 1:
        return 1
    else:
        for i in range(1, len(str(num))+1):
            num_range = range(10**(i-1), (10**i)-1)
            num_cal = ((10**i)) - (10**(i-1))
            if num in num_range:
                num_cal = (num - (10**(i-1)))+1
            count += num_cal*(1+i)
        return count
print(calculator(int(input())))
