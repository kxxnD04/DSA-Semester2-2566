"""ขบวนรถธรรมดาที่ 283- Final exam"""
def final_crisis():
    """ข้อสอบดีมากครับ คนทำไม่ผ่านหลายคนเลย """
    start, stop = input().split(", ")
    distance1, distance2 = "", ""
    try:
        while True:
            station = input()
            if station == "Done":
                break
            station = station.split(", ")
            if station[0] == start:
                distance1 = float(station[-1])
            if station[0] == stop:
                distance2 = float(station[-1])
            if distance1 != "" and distance2 != "":
                break
        print("%.2f" % float(abs(distance2-distance1)))
    except (TypeError, EOFError):
        print("Error")
final_crisis()
