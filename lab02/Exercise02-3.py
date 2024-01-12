"""Exercise02-3"""
class ArrayStack:
    """____stack"""

    def __init__(self):
        """____"""
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        """delete data"""
        try:
            self.size -= 1
            return self.data.pop()
        except (TypeError, ValueError, ArithmeticError, AttributeError, IndexError):
            print("Underflow: Cannot pop data from an empty list")
            return None

    def is_empty(self):
        """check empty data"""
        return len(self.data) == 0

    def get_stack_top(self):
        """get top of the stack"""
        try:
            return self.data[-1]
        except (TypeError, ValueError, ArithmeticError, AttributeError, IndexError):
            print("Underflow: Cannot get stack top from an empty list")
            return None

    def get_size(self):
        """return size"""
        return len(self.data)

    def print_stack(self):
        """PRINT"""
        print(self.data)

def spam_matching():
    """Paren check"""
    txt = input().strip()
    data1 = ArrayStack()
    data2 = ArrayStack()
    data3 = ArrayStack()
    for i in txt:
        if i == "(":
            data1.push("(")
        elif i == ")":
            data1.pop()
        if i == "{":
            data2.push("{")
        elif i == "}":
            data2.pop()
        if i == "[":
            data3.push("[")
        elif i == "]":
            data3.pop()
    con1 = txt.count("(") == txt.count(")")
    con2 = txt.count("{") == txt.count("}")
    con3 = txt.count("[") == txt.count("]")
    ans1 = con1 and data1.is_empty()
    ans2 = con2 and data2.is_empty()
    ans3 = con3 and data3.is_empty()
    print(ans1 and ans2 and ans3)
spam_matching()
