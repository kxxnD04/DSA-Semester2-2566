"""f format cant use on ejudge WTF?"""
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
_IN = Person(input().strip(), int(input()))
print(_IN.get_details())
print(_IN.say_hello())
