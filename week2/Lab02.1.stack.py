"""LAB02-1"""
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


STACK_ = ArrayStack()

STACK_.push("100")
STACK_.push(100)
STACK_.push("3.14")
STACK_.push(3.14)
STACK_.push("66.4a")
STACK_.push("Ackerman")

STACK_.print_stack()

print(STACK_.get_size())
VAR1_ = STACK_.pop()
print(VAR1_)
STACK_.print_stack()
print(STACK_.get_size())

while not STACK_.is_empty():
    print(STACK_.pop())

print()
print(STACK_.pop())
print(STACK_.get_stack_top())
print(VAR1_)
