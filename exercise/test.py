class ArrayStack:
    def __init__(self):
        """init stack"""
        self.size = 0
        self.data = list()

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
        if self.size == 0:
            return print("Underflow: Cannot pop data from an empty list")
        self.size -= 1
        return self.data.pop()
    
    def is_empty(self):
        return self.size == 0

    def get_stack_top(self):
        if self.size == 0:
            return print("Underflow: Cannot get stack top from an empty list")
        temp = self.data.pop()
        self.data.append(temp)
        return temp
    
    def get_size(self):
        return self.size
    
    def print_stack(self):
        print(self.data)

s = ArrayStack()
num_group = int(input())
for i in range(num_group):
    s.push(ArrayStack())

num_students = int(input())

all_students = ArrayStack()

for _ in range(num_students):
    all_students.push(input())

while not all_students.is_empty():
    temp1 = ArrayStack()


    while not s.is_empty():
        if all_students.is_empty():
            break
        a = s.pop()
        a.push(all_students.pop())
        temp1.push(a)
    while not s.is_empty():
        temp1.push(s.pop())

    while not temp1.is_empty():
        s.push(temp1.pop())

count = 1
while not s.is_empty():
    temp = s.pop()
    ans = "Group " + str(count) + ": "
    temp2 = ArrayStack()
    while not temp.is_empty():
        temp2.push(temp.pop())
    while not temp2.is_empty():
        ans += temp2.pop() + ", "
    print(ans.rstrip(", "))
    count += 1
