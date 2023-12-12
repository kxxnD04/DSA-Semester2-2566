"""Ex03"""
def name(amount: int):
    """name"""
    namelist = []
    for _ in range(amount):
        namelist.append([input()])
    while len(namelist) > 1:
        eleone = namelist.pop(0)
        eletwo = namelist.pop(0)
        popresult = []
        while eleone and eletwo:
            if eleone[0] > eletwo[0]:
                popresult.append(eletwo.pop(0))
            else:
                popresult.append(eleone.pop(0))
        popresult += eleone + eletwo
        namelist.append(popresult)
    if namelist:
        print(*namelist[0], sep="\n")
name(int(input()))