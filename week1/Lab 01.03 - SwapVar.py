"""SWAP"""
def swap(tup):
    """main function"""
    xx1 = '%.1f' % float(tup[1]) if '.' not in tup[1] else tup[1]
    xx2 = '%.1f' % float(tup[0]) if '.' not in tup[0] else tup[0]
    print((float(xx1), float(xx2)))
swap(input().replace('(', '').replace(')', '').split(', '))
