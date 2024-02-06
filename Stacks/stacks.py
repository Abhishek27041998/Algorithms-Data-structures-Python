"""
This is an implementation of Stack data structure
"""


class Stack:
    def __init__(self, max_size=10):
        self.stack = []
        self.max_size = max_size
        self.top = -1

    def push(self, element):
        if self.top == self.max_size - 1:
            return "Stack Overflow!!"
        else:
            self.stack.append(element)
            self.top += 1

    def is_empty(self):
        return self.top == -1

    def pop(self):
        if self.is_empty():
            return "Stack Underflow!!"
        else:
            self.top -= 1
            return self.stack.pop()

    def top_element(self):
        if self.is_empty():
            return "Stack is Empty"
        else:
            return self.stack[-1]

    def size(self):
        return self.top + 1

    def print_elements(self):
        if self.is_empty():
            return "Stack is Empty!!"
        else:
            print('----------------')
            for item in self.stack:
                print(item)


if __name__ == '__main__':
    stack = Stack(5)

    # Insert 3 values to stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_elements()

    # Pop an element
    stack.pop()
    stack.print_elements()

    # Insert 4 values to get Stack Overflow
    print('-----------')
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.push(6))   # This line causes Stack Overflow

    # Get top element
    print('------------')
    print(stack.top_element())

    # Get size
    print('------------')
    print(stack.size())

    # Pop all the elements until Stack Underflow
    print('-------------')
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack.pop())     # This causes Stack Underflow

