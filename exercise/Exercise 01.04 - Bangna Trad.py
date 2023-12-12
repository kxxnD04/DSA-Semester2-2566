"""Exercise 01.04 - Bangna Trad"""
def bangnaroad(num):
    """bangna"""
    if num >= 52.900 and num <= 58.855:
        print('Chachoengsao' if num == 52.900 else 'Chon Buri')
    elif num >= 35.477 and num <= 52.900:
        print('Samut Prakarn' if num == 35.477 else 'Chachoengsao')
    elif num >= 5.032 and num <= 35.477:
        print('Bangkok' if num == 5.032 else 'Samut Prakarn')
    else:
        print('Bangkok' if num >= 0 and num <= 58.855 else 'InValid')
bangnaroad(float(input()))
