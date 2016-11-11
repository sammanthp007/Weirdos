# stack in python: 
# push : list.append()
# pop : list.pop()
# is_empty : len(list)

class Queue:
    def __init__(self, limit):
        self.max_value = limit
        self.input_stack = []
        self.output_stack = []
        self.max_len_input_stack = limit // 2
        if limit % 2 == 0:
            self.max_len_output_stack = limit / 2
        else:
            self.max_len_output_stack = limit // 2 + 1

    def enqueue(self, n):
        combined_len = len(self.output_stack) + len(self.input_stack)

        # case when they need to combine
        if combined_len == self.max_len_output_stack:
            # transfer from output to input and then to input
            self.transfer_from(self.output_stack, self.input_stack)
            self.transfer_from(self.input_stack, self.output_stack)

        # case they already combined
        if len(self.output_stack) == self.max_len_output_stack:
            # case when both of the stacks have maxed out
            if len(self.input_stack) == self.max_len_input_stack:
                return False

        self.input_stack.append(n)

    def transfer_from(self, stack1, stack2):
        while len(stack1) > 0:
            stack2.append(stack1.pop())

    def dequeue(self):
        ret_val = False
        if len(self.output_stack) > 0:
            ret_val = self.output_stack.pop()
            if len(self.output_stack) == 0:
                self.transfer_from(self.input_stack, self.output_stack)
        else:
            self.transfer_from(self.input_stack, self.output_stack)
            if len(self.output_stack) > 0:
                ret_val = self.output_stack.pop()
        return ret_val

a = Queue(4)
a.enqueue(1)
print(a.input_stack, a.output_stack)
a.enqueue(2)
print(a.input_stack, a.output_stack)
a.enqueue(3)
print(a.input_stack, a.output_stack)
a.enqueue(4)

print(a.dequeue())
print(a.input_stack, a.output_stack)
print(a.dequeue())
print(a.input_stack, a.output_stack)
print(a.dequeue())
print(a.input_stack, a.output_stack)
print(a.dequeue())
print(a.input_stack, a.output_stack)
print(a.dequeue())
