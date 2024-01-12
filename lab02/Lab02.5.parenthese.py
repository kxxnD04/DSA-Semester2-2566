"""LAB02-5"""
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


def is_parentheses_matching():
    """Paren check"""
    txt = input().strip()
    data = ArrayStack()
    for i in txt:
        if i == "(":
            data.push("(")
        elif i == ")":
            data.pop()
    con1 = txt.count("(") == txt.count(")")
    ans = con1 and data.is_empty()
    print("Parentheses in " + txt + " are" +
          (" matched" if ans else " unmatched"))
    print(ans)
is_parentheses_matching()
