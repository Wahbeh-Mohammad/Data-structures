class Error(Exception):
    def __init__(self,desc):
        self.desc = desc
    
    def __str__(self):
        return self.desc

class InvalidQueueLength(Error):
    def __init__(self,desc):
        Error.__init__(self,desc)

class FullQueue(Error):
    def __init__(self):
        Error.__init__(self,"Full Queue")

class EmptyQueue(Error):
    def __init__(self):
        Error.__init__(self,"Empty Queue")

from Array import Array

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
    
if  __name__ == '__main__':
    Q = Queue(5)
    for i in range(5):
        Q.enqueue(i)
        print(Q)
    
    for j in range(5):
        Q.dequeue()
        print(Q)
    
    
