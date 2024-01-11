class ListFullError(Exception):
    pass

class ListEmptyError(Exception):
    pass

class ValueNotFoundError(Exception):
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
        p = self.start
        
        if p == None:
            return None
        
        orderedList = []
        orderedList.append(self.list[p].data)
        
        while self.list[p].pointer != None:
            p = self.list[p].pointer
            orderedList.append(self.list[p].data)
        
        return orderedList
        
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

                    else:
                        break
                
                temp = self.list[previous].pointer
                self.list[previous].pointer = self.nextfree
                self.list[self.nextfree] = Node(data, temp)
                self.nextfree = self.findfree()
    
    def delete(self, data):
        if self.start == None:
            raise ListEmptyError("linked list is empty")
        
        else:
            p = self.start
            
            if self.list[p].data == data:
                self.start = self.list[p].pointer
                self.list[p].data, self.list[p].pointer = None, None
                self.nextfree = self.findfree()
            
            else:
                try:
                    while self.list[self.list[p].pointer].data != data:
                        p = self.list[p].pointer

                    temp = self.list[self.list[p].pointer].pointer
                    self.list[self.list[p].pointer].data, self.list[self.list[p].pointer].pointer = None, None
                    self.list[p].pointer = temp
                    self.nextfree = self.findfree()
                
                except TypeError:
                    raise ValueNotFoundError("the value wasn't found in the linked list")
