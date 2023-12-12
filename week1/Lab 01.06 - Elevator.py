"""Lab 01.06 - Elevator"""


class Elevator:
    """ELE"""

    def __init__(self, max_floor):
        """___"""
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        """floor"""
        self.current_floor = floor

    def get_maxfloor(self):
        """max"""
        return self.max_floor

    def report_current_floor(self):
        """report"""
        return self.current_floor


def main():
    """main"""
    floor = Elevator(int(input()))
    while True:
        each = input()
        if each == 'Done':
            break
        elif int(each) > floor.get_maxfloor():
            print("Invalid Floor!")
        else:
            floor.go_to_floor(each)
    print(floor.report_current_floor())
main()
