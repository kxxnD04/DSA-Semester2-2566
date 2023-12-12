"""LAB 04"""
class Rectangle:
    """main class"""
    def __init__(self, heigh, width):
        """init"""
        self.heigh = heigh
        self.width = width

    def area(self):
        """return area of ractangle"""
        return self.heigh * self.width

    def perimeter(self):
        """return perimeter of rectangle"""
        return 2*(self.heigh + self.width)

def main():
    """main func"""
    ans = Rectangle(float(input()), float(input()))
    con = input()
    print('%.2f' % (ans.area()) if con == 'area' else '%.2f' % (ans.perimeter()))
main()
