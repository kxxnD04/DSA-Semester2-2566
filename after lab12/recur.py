def ex3(num):
    if num < 5:
        return 3*num
    else:
        return 2*ex3(num-5) + 7
    print("finish")
    return 1
print(ex3(17))