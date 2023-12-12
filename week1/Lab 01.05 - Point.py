"""lab 05 point"""


class Point:
    """point"""

    def __init__(self, val_x=0, val_y=0):
        """___"""
        self.set_coordinates(val_x, val_y)

    def set_coordinates(self, val_x, val_y):
        """cor"""
        self.val_x = val_x
        self.val_y = val_y

    def get_coordinates(self):
        """get tuple"""
        return (self.val_x, self.val_y)

    def calculate_distance(self, other_point):
        """distance"""
        return ((other_point.val_x - self.val_x)**2 + (other_point.val_y - self.val_y)**2) ** 0.5


def main():
    """point"""
    point1 = Point(float(input()), float(input()))
    point2 = Point(float(input()), float(input()))
    print('%.2f' % point1.calculate_distance(point2))


main()
