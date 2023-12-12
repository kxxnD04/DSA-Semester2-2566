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
print(LaewTaeApp().list_foods())
