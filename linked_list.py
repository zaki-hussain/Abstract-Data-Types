class ListFullError(Exception):
    pass

class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

class LinkedList:
    def __init__(self, size):
        self.list = [Node(None, None)] * size
        self.start = None
        self.nextfree = 0

    def findfree():
        for i, node in self.list:
            if node.pointer == None:
                return i
        return False


    def insert(self, data):
        if self.nextfree == False:
            raise ListFullError("linked list is full")

        if self.start == None:
            self.list[0] = Node(data, 1)

        else:
            p = self.start
            while True:
                if not self.list[p].pointer == None:
                    if data > self.list[self.list[p].pointer].data:
                        p = self.list[p].pointer
                    else:
                        break
                else:
                    break
        
            temp = self.list[p].pointer
            self.list[p].pointer = self.nextfree
            self.list[self.nextfree] = Node(data, temp)
            self.nextfree = self.findfree()

a = LinkedList(5)

# print(a.list[1].pointer)
a.insert(8)