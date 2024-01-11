class QueueEmptyError(Exception):
    pass

class QueueFullError(Exception):
    pass

class CircularQueue:
    def __init__(self, length):
        self.length = length
        self.items = [None] * length
        self.front = 0
        self.rear = -1
        self.size = 0

    def isfull(self):
        return self.size == self.length
    
    def isempty(self):
        return self.size == 0
    
    def enqueue(self, item):
        if self.isfull():
            raise QueueFullError("queue is empty")
        else:
            self.rear = (self.rear + 1) % self.length
            self.items[self.rear] = item
            self.size += 1

    def dequeue(self):
        if self.isempty():
            raise QueueEmptyError("queue is empty")
        else:
            temp = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % self.length
            self.size -= 1
            return temp
