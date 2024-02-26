"""Exercise 11.03 - Runner"""
def find_winner(distance: int, people: int):
    """find winner of running race"""
    lis = [list(map(int, input().split() + [i])) for i in range(1, people+1)]
    print(sorted(lis, key=lambda x: ((distance-x[1])/x[0], -x[0]))[0][-1])
find_winner(int(input()), int(input()))
