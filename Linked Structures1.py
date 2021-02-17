class LinkedList:
    class Node:
        __slots__ = 'data','next'
        def __init__(self,data,N=None):
            self.data = data
            self.next = N
    
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def add(self,val):
        newnode = LinkedList.Node(val)
        if self.head != None:
            newnode.next = self.head
            self.head = newnode
        else:
            self.head = newnode
        self.size += 1
    
    def max_element(self):
        Head = self.head
        Max = Head.data
        while True:
            if Head==None:
                break
            else:
                if Head.data>Max:
                    Max = Head.data
                Head = Head.next
        return Max
    
    def count_even(self):
        Head = self.head
        evens = 0
        while True:
            if Head==None:
                break
            else:
                if Head.data%2==0:
                    evens+=1
                Head = Head.next
        return evens

    def __str__(self):
        data = []
        head = self.head
        while True:
            if head == None:
                break
            else:
                data.append(head.data)
                head = head.next
        data.reverse()
        return str(data)

class LinkedStack:
    class Node:
        __slots__ = 'data','next'
        def __init__(self,data,N = None):
            self.data = data
            self.next = N
        
    def __init__(self):
        self.size = 0
        self.head = None
    
    def empty(self):
        return self.size==0
    
    def push(self,val):
        newnode = LinkedStack.Node(val)
        if self.head != None:
            newnode.next = self.head
            self.head = newnode
            self.size += 1
        else:
            self.head = newnode
            self.size += 1
    
    def pop(self):
        if self.head != None:
            val = self.head.data
            self.size -= 1
            self.head = self.head.next
            return val
    
    def __str__(self):
        data = []
        head = self.head
        while True:
            if head == None:
                break
            else:
                data.append(head.data)
                head = head.next
        data.reverse()
        return str(data)

class LinkedQueue:
    class Node:
        __slots__ = 'data','next'
        def __init__(self,data,N=None):
            self.data = data
            self.next = N
        
        def __str__(self):
            return str(self.data) + " , " + str(self.next)
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def empty(self):
        return self.size==0
    
    def enqueue(self, data):
        if self.tail is None:
            self.head = LinkedQueue.Node(data)
            self.tail = self.head
        else:
            self.tail.next = LinkedQueue.Node(data)
            self.tail = self.tail.next
        self.size+=1 
 
    def dequeue(self):
        if self.head == None:
            self.head = None
            self.tail = None
            return None
        else:
            val = self.head.data
            self.head = self.head.next
            self.size-=1
            return val

    def __str__(self):
        head = self.head
        data = []
        while True:
            if head == None:
                break
            data.append(head.data)
            head = head.next
        return str(data)            

import ctypes

class CircularQueue:
    def __init__(self,capacity):
        pyobj = ctypes.py_object * capacity
        self.queue = pyobj()
        self.head = 0
        self.tail = 0
        self.maxSize = capacity

    def enqueue(self,data):
        if self.size() == self.maxSize-1:
            return "Queue Full!"
        self.queue[self.tail] = data
        self.tail = (self.tail + 1) % self.maxSize

    def dequeue(self):
        if self.size()==0:
            return "Queue Empty!"
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data

    def isempty(self):
        return self.size()==0

    def __getitem__(self,index):
        assert 0<=index<self.maxSize
        return self.queue[index]

    def size(self):
        if self.tail>=self.head:
            return (self.tail-self.head)
        return (self.maxSize - (self.head-self.tail))

    def sum_even(self):
        pass

    def __str__(self):
        s = ''
        for i in range(self.size()):
            s+= str(self.queue[i])+" "
        return s

 

