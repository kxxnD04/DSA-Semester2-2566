"""Labs 12.02 - (2) Knapsack"""


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
        return (self.__price/self.__weight)/10


def knapsack(items: list, cap: float):
    """greedy algor"""
    total, new_items, weight = 0, [], 0
    for each in items:
        new_items.append(
            (each.get_name(), (each.get_cost(), each.get_weight()), each.get_price()))
    new_items.sort(key=lambda x: ((x[1][0])), reverse=True)
    print("Knapsack Size: {} kg".format(cap))
    print("===============================")
    for name, tupp, price in new_items:
        if weight + tupp[1] <= cap:
            weight += tupp[1]
            total += price
            print("{} -> {} kg -> {} THB".format(name, tupp[1], price))
    print("Total: {} THB".format(total))


def main():
    """main function"""
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(
            Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)


main()
