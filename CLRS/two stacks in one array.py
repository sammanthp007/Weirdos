class TwoStacks:
    def __init__(self, limit):
        self.max = limit
        self.array = [None] * self.max
        self.stack1_top = 0
        self.stack2_top = self.max - 1

    def is_stack1_empty(self):
        if self.stack1_top == 0 and self.array[self.stack1_top] == None:
            return True
        return False

    def is_stack2_empty(self):
        if self.stack2_top == self.max - 1:
            if self.array[self.stack2_top] == None:
                return True
        return False

    def push_stack1(self, n):
        if self.stack1_top + 1 == self.max:
            return False

        if self.array[self.stack1_top + 1] != None:
            return False

        if self.is_stack1_empty():
            self.array[self.stack1_top] = n

        else:
            self.stack1_top += 1
            self.array[self.stack1_top] = n

    def push_stack2(self, n):
        if self.stack2_top == 0:
            return False

        if self.array[self.stack2_top - 1] != None:
            return False

        if self.is_stack2_empty():
            self.array[self.stack2_top] = n

        else:
            self.stack2_top -= 1
            self.array[self.stack2_top] = n

    def pop_stack1(self):
        if self.stack1_top == 0:
            return False
        self.stack1_top -= 1
        ret_val = self.array[self.stack1_top + 1]
        self.array[self.stack1_top + 1] = None
        return ret_val

    def pop_stack2(self):
        if self.stack2_top == self.max - 1:
            return False

        self.stack2_top += 1
        ret_val = self.array[self.stack2_top - 1]
        self.array[self.stack2_top - 1] = None
        return ret_val

a = TwoStacks(5)
a.push_stack1(5)
print (a.array)
a.push_stack2(10)
print (a.array)
a.push_stack2(15)
print (a.array)
a.push_stack1(11)
print (a.array)
a.push_stack2(7)
print(a.array)
print(a.pop_stack1())
print(a.array)
print(a.push_stack1(40))
print(a.array)

print(a.pop_stack1())
print(a.pop_stack2())
print(a.array)
print(a.pop_stack1())
print(a.array)

