# Custom Errors
class Error(Exception):
    def __init__(self,desc):
        self.desc = desc
    
    def __str__(self):
        return self.desc

class EmptyStack(Error):
    def __init__(self,desc):
        Error.__init__(self, desc)
        
# We will be using Nodes for the data
class Node:
    __slots__ = 'data','next'
    def __init__(self,data,nxt=None):
        self.data = data
        self.next = nxt        

# Stack
class Stack(object):
    def __init__(self):
        self._head = None
        self._length = 0
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node
        self._length += 1

    def pop(self):
        if self._head is None:
            raise EmptyStack("The Stack is Empty.")
        
        n = self._head
        self._head = n.next
        self._length -= 1
        return n.data
    
    def peek(self):
        if self._head is None:
            raise EmptyStack("The Stack is Empty.")
        
        return self.head.data
    
    def __len__(self):
        return self.len
    
    def __str__(self):
        ret = 'None'
        copy = self._head
        
        while(copy is not None):
            ret += '<-'
            ret += str(copy.data)
            copy = copy.next
        return ret+'<-None'

if __name__ == '__main__':
    St = Stack()
    St.push(5)
    St.push(10)
    St.push(15)
    print(St)
    St.pop()
    print(St)