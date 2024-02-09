"""lab10 02"""


class Student:
    """student"""

    def __init__(self, std_id, name, gpa):
        """init"""
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self):
        """get id"""
        return self.std_id

    def get_name(self):
        """get name"""
        return self.name

    def get_gpa(self):
        """get gpa"""
        return self.gpa

    def print_details(self):
        """p detail"""
        print("ID: " + str(self.std_id))
        print("Name: " + self.name)
        print("GPA: %.2f" % self.gpa)


class ProbHash:
    """Hashing"""
    def __init__(self, size):
        """init"""
        self.hash_table = [" "]*size
        self.size = size

    def hash(self, key):
        """hash"""
        return key % self.size

    def rehash(self, hkey):
        """rehash"""
        return (hkey+1) % self.size

    def insert_data(self, std: Student):
        """add std to hash table"""
        if self.hash_table.count(" ") == 0:
            print("The list is full. %d could not be inserted." %
                  int(std.get_std_id()))
        else:
            index = self.hash(std.get_std_id())
            while self.hash_table[index] != " ":
                index = self.rehash(index)
            self.hash_table[index] = std
            print("Insert %d at index %d" % (std.get_std_id(), index))

    def search_data(self, std_id):
        """search item"""
        for item in self.hash_table:
            if item != " ":
                if item.get_std_id() == std_id:
                    print("Found %d at index %d" %
                          (std_id, self.hash_table.index(item)))
                    return item
        print("%d does not exist." % std_id)
        return None


def main():
    """main function"""
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")


main()
