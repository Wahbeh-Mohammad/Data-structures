# Stack module
## Classes
-Node
-Stack

# In this implementation I used nodes.

## The Class Node
```
class Node:
    __slots__ = 'data','next'
    def __init__(self,data,nxt=None):
        self.data = data
        self.next = nxt   
```
## Variables
-data: The data the node represents
-next: pointer to the next node

# Stack
- __init__: to initialize the Stack.
- push: Pushes a new value into the stack.
- pop: Pops a value from the stack.
- peek: returns the top of the stack.
- __len__: returns the number of nodes.
- __str__: String representation of the stack.
``` 
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
```
