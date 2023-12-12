"""lab02 max min avg without max min sorted"""
import json
def main():
    """MEM BROKE"""
    list1 = json.loads(input().strip())
    av_g = round(sum(list1)/len(list1), 2) if len(list1) != 0 else 0
    ma_x, mi_n = list1[0], list1[0]
    for i in list1:
        ma_x = i if ma_x < i else ma_x
        mi_n = i if mi_n > i else mi_n
    ma_x = round(ma_x, 2) if ma_x != 0 else 0
    mi_n = round(mi_n, 2) if mi_n != 0 else 0
    print((ma_x, mi_n, av_g))
main()
