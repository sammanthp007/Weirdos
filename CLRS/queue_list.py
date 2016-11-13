class Queue:
    def __init__(self, limit):
        self.head = 0
        self.tail = 0
        self.max = limit 
        self.queue = [None] * 3

    def enqueue(self, x):
        if self.tail >= self.max:
            return False
        self.tail += 1
        self.queue[self.tail] = x

    def dequeue(self):
        if self.tail == self.head:
            return False
        self.tail -= 1
        return self.queue[self.tail + 1]

A = Queue(2)
A.enqueue(2)
A.enqueue(3)
print(A.dequeue())
print(A.dequeue())
print(A.dequeue())
