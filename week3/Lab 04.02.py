"""Lab 04.02 Singly Linked List (Traversal and Insert Last)"""
class DataNode:
    """NO MORE SETTER GETTER"""
    def __init__(self, data):
        """____"""
        self.__data = data
        self.__next = None
    def set_data(self, new):
        """set"""
        self.__data = new
    def get_data(self):
        """return data"""
        return self.__data
    def set_next(self, next_node):
        """set"""
        self.__next = next_node
    def get_next(self):
        """re"""
        return self.__next

class SinglyLinkedList:
    """LLL"""
    def __init__(self):
        """INIT"""
        self.head = None
        self.count = 0

    def traverse(self):
        """TRAVERSE"""
        if self.head is None:
            print("This is an empty list.")
        else:
            current_node = self.head
            while current_node:
                print(current_node.get_data(), end="")
                if current_node.get_next() != None:
                    print(' -> ', end='')
                current_node = current_node.get_next()

    def insert_last(self, data):
        """INSERT"""
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.get_next():
                current_node = current_node.get_next()
            current_node.set_next(new_node)
        self.count += 1
LIST1_ = SinglyLinkedList()
for i in range(int(input())):
    LIST1_.insert_last(input())
LIST1_.traverse()
