"""class person v2"""
class Person:
    """Syntax error ?"""
    def __init__(self, name, age):
        """get name, age"""
        self.name = name
        self.age = age
    def get_details(self):
        """return name and age"""
        return self.name + ", " + str(self.age) + " years old"
    def say_hello(self):
        """return hello name"""
        return "Hello, my name is " + self.name + "!"
class Project:
    """show members of the project"""
    def __init__(self, name, num_members, all_members):
        """____"""
        self.name = name
        self.num_members = num_members
        self.all_members = all_members
    def show_projectname(self):
        """show project name"""
        print("Hello There! This is " + self.name)
    def show_members(self):
        """show members of the project sort by A-Z"""
        print("This project has " + str(self.num_members) + " members")
        for i in self.all_members:
            print(i.say_hello())
_NAME, _MEM = input().strip(), int(input())
_ALLMEM = sorted([Person(input(), int(input())) for _ in range(_MEM)], key=lambda self: self.name)
_INPUT = Project(_NAME, _MEM, _ALLMEM)
_INPUT.show_projectname()
_INPUT.show_members()
