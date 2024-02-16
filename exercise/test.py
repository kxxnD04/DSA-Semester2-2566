def plus(nnn):
    if nnn == 0:
        return nnn
    else:
        return nnn + plus(nnn-1)
print(plus(5))