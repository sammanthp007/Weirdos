class Stack:
    def __init__(self):
        self.top = 0
        self.stack = [None] * 3

    def is_empty(self):
        if self.top == 0:
            return True
        return False

    def push(self, n):
        self.top += 1
        self.stack[self.top] = n

    def pop(self):
        if self.is_empty():
            return False
        self.top -= 1
        return self.stack[self.top + 1]



A = Stack()
print(A.is_empty())
A.push(3)
print(A.is_empty())

print(A.pop())
print(A.is_empty())
