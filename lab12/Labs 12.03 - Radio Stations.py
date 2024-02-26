"""Labs 12.03 - Radio Stations"""
from json import loads as jack
def findstations(stations: list):
    """Silicon Valley"""
    data, stations, ans = [], set(stations), []
    for _ in range(int(input())):
        data.append(jack(input()))
    while stations:
        data.sort(key=lambda x: len(set(x["Cities"]).intersection(stations)), reverse=True)
        current = data.pop(0)
        loop = set(current["Cities"]).intersection(stations)
        if not loop:
            break
        ans.append(current["Name"])
        for town in loop:
            stations.remove(town)
    print(sorted(ans))
findstations(jack(input()))
