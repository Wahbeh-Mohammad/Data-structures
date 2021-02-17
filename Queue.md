# Queue
## Variables:
- self.__maxsize : the max size of the queue
- self._que : the memory allocated for the queue
- self._len : the current amount of elements in the queue
- self._front: current front of the queue
- self._back: the back of the queue
## Functions:
- __init__: method to initialize the Queue
- isEmpty: returns if the queue is empty
- isFull: returns if the queue is full
- equeue: Enques a value into the end of the queue
- dequeue: deques the front of the queue
- __shift: shifts the values of the queue after being dequeued
- __len__: returns the number of elements in the queue
- __iter__: allows the queue to be iterated over
- __str__: String representation of the queue
```
class Queue:
    def __init__(self,maxSize=1):
        if maxSize>=1:
            self.__maxsize = maxSize
        else:
            raise InvalidQueueLength("Invalid Size")
        self._que = Array(self.__maxsize)
        self._len = 0
        self._front = 0
        self._back = self.__maxsize-1
    
    def isEmpty(self):
        return len(self) == 0
    
    def isFull(self):
        return len(self)==self.__maxsize
    
    def enqueue(self,value):
        if self.isFull():
            raise FullQueue
        maxSize = self.__maxsize
        self._back = (self._back+1)%maxSize
        self._que[self._back] = value
        self._len+=1        
        
    def dequeue(self):
        if self.isEmpty(): 
            raise EmptyQueue
        
        item = self._que[self._front]
        self._len-=1
        self._que = self.__shift()
        return item
    
    def __shift(self):
        for i in range(1,len(self)+1):
            self._que[i-1] = self._que[i]
        self._que[len(self)] = None
        return self._que
        
    def __len__(self):
        return self._len
        
    def __iter__(self):
        return self._que.__iter__()
    
    def __str__(self):
        return "O<< ["+ " < ".join(str(self._que)[1:-1].split(","))+ "] <<I"
```
