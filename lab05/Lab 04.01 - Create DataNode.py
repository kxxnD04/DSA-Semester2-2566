"""Lab 04.01 - Create DataNode"""
class DataNode:
    """data node _"""
    def __init__(self, data):
        """____"""
        self.__data = data
        self.__next = None
    def get_data(self):
        """get data"""
        return self.__data
    def set_data(self, data):
        """set_data()"""
        self.__data = data
    def get_next(self):
        """get_next()"""
        return self.__next
    def set_next(self, next_node):
        """set_next()"""
        self.__next = next_node
_INPUT = DataNode(input().strip())
print(_INPUT.get_data())
print(_INPUT.get_next())
