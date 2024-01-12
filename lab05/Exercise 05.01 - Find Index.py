"""Exercise 05.01 - Find Index"""
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

    def insert_front(self, data):
        """INSERT"""
        new_node = DataNode(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def insert_before(self, node, data):
        """TRY EXCEPT PLS HELP ME"""
        new_node = DataNode(data)
        current = self.head
        try:
            if self.head.get_data() == node:
                self.insert_front(data)
                return
            while True:
                if current.get_next().get_data() == node:
                    new_node.set_next(current.get_next())
                    current.set_next(new_node)
                    self.count += 1
                    break
                current = current.get_next()
        except AttributeError:
            print("Cannot insert, {} does not exist.".format(node))

    def delete(self, data):
        """TRY EXCEPT PLS HELP ME"""
        current = self.head
        try:
            if self.head.get_data() == data:
                self.head = current.get_next()
                self.count -= 1
                return
            while True:
                if current.get_next().get_data() == data:
                    current.set_next(current.get_next().get_next())
                    self.count -= 1
                    break
                current = current.get_next()
        except AttributeError:
            print("Cannot delete, {} does not exist.".format(data))
def find_index():
    """find index of node"""
    link = SinglyLinkedList()
    while True:
        in_ = input().strip()
        if in_ == "Last":
            break
        link.insert_last(in_)
    index = int(input())
    try:
        i = 1
        current = link.head
        while i != index:
            current = current.get_next()
            i += 1
        print(current.get_data())
    except AttributeError:
        print("Error")
find_index()
