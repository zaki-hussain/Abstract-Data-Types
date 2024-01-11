class ListFullError(Exception):
    pass

class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

class LinkedList:
    def __init__(self, length):
        self.list = [Node(None, None) for i in range(length)]
        self.start = None
        self.nextfree = 0

    def read(self):
        for _ in self.list:
            print(_.data, _.pointer)
        
    def findfree(self):
        for i, node in enumerate(self.list):
            if node.data == None:
                return i
        return None
    
    def insert(self, data):
        if self.nextfree == None:
            raise ListFullError("linked list is full")
        
        elif self.start == None:
            self.start = 0
            self.nextfree = 1
            self.list[0] = Node(data, None)

        else:
            p = self.start
            if data < self.list[p].data:
                self.start = self.nextfree
                self.list[self.nextfree] = Node(data, p)
                self.nextfree = self.findfree()

            else:
                while True:
                    if self.list[p].pointer == None:
                        if data >= self.list[p].data:
                            previous = p
                        break
                    
                    if data >= self.list[p].data:
                        previous = p
                        p = self.list[p].pointer
                
                temp = self.list[previous].pointer
                self.list[previous].pointer = self.nextfree
                self.list[self.nextfree] = Node(data, temp)
                self.nextfree = self.findfree()
    
