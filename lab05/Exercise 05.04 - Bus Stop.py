"""Exercise 05.04 - Bus Stop"""
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
def find_first_index(link):
    """find index of node"""
    for i in link:
        ans = int(i)
        break
    return ans

def bus_stop():
    """bus"""
    buss = SinglyLinkedList()
    bus_ans = SinglyLinkedList()
    cap = int(input())
    sign = int(input())
    ans = 0
    for _ in range(sign):
        buss.insert_last(input().split())
    current = buss.head
    for j in range(1, sign+1):
        check_ans = bus_ans.head
        lab_del = 0
        for _ in range(bus_ans.count):
            if check_ans.get_data() == j:
                ans += 1
                lab_del += 1
            check_ans = check_ans.get_next()
        for _ in range(lab_del):
            bus_ans.delete(j)
        current = buss.head
        for _ in range(sign):
            if find_first_index(current.get_data()) == j:
                break
            current = current.get_next()
        first_round = False
        for num in current.get_data():
            if first_round == False:
                first_round = True
                continue
            else:
                if bus_ans.count < cap and int(num) >= j:
                    bus_ans.insert_last(int(num))
    print(ans)
bus_stop()
