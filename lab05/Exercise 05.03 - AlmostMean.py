"""Exercise 05.03 - AlmostMean"""
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
def almost_mean():
    """Find almost mean"""
    students = int(input())
    find_mean = 0
    stu_id = SinglyLinkedList()
    stu_scores = SinglyLinkedList()
    for _ in range(students):
        _id, scores = input().split()
        scores = float(scores)
        find_mean += scores
        stu_id.insert_last(_id)
        stu_scores.insert_last(scores)
    find_mean /= students
    ans_id = stu_id.head.get_data()
    ans_scor = stu_scores.head.get_data()
    compare_id = stu_id.head
    compare_scores = stu_scores.head
    for _ in range(students):
        if (abs(ans_scor- find_mean) > abs(compare_scores.get_data() - find_mean))\
        and (compare_scores.get_data() <= find_mean) or (ans_scor > find_mean):
            ans_scor = compare_scores.get_data()
            ans_id = compare_id.get_data()
        compare_scores = compare_scores.get_next()
        compare_id = compare_id.get_next()
    print(ans_id, ans_scor, sep='\t')

almost_mean()
