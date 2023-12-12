"""Exercise 01.02 - Laew Tae App V.1"""
class LaewTaeApp:
    """Laew tae app"""
    def __init__(self):
        """init"""
        self.food_list = ['Pizza', 'Fried Chicken', 'Hamburger', 'Steak']
        self.random_times = 0

    def random_foods(self):
        """random"""
        return self.random_times + 1

    def list_foods(self):
        """Food list"""
        return sorted(self.food_list)

    def add_food_item(self, name):
        """add menu to food list"""
        self.food_list += name
FOOD_ = LaewTaeApp()
FOOD_.add_food_item([input() for _ in range(int(input()))])
print(FOOD_.list_foods())
