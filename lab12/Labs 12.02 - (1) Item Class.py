""""Labs 12.02 - (1) Item Class"""
class Item:
    """Labs 12.02 - (1) Item Class"""
    def __init__(self, name: str, price: float, weight: int):
        """init"""
        self.__name = name
        self.__price = price
        self.__weight = weight
    def get_name(self):
        """get name"""
        return self.__name
    def get_price(self):
        """get price"""
        return self.__price
    def get_weight(self):
        """get weight"""
        return self.__weight
    def get_cost(self):
        """get cost"""
        return self.__price//self.__weight

def main():
    """main fuction"""
    import json
    item_in = json.loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item.get_name(), item.get_price(), item.get_weight(), sep='\n')

main()
