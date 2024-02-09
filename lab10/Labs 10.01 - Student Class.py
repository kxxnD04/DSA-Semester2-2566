"""lab 10 hashing 1"""


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


def main(text_in):
    """hehe"""
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()


main(input())
