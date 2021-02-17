# Important libraries
import sys
import ctypes

# Helper Classes and Custom Errors
# Base Error Class
class Error(Exception):
    def __init__(self,desc):
        self.desc = desc
    
    def __str__(self):
        return self.desc

class InvalidSize(Error):
    """ """
    def __init__(self,desc):
        Error.__init__(self,desc)

class IndexOutofRange(Error):
    """ """
    def __init__(self,desc):
        Error.__init__(self,desc)

# Array Iterator Class
class _ArrayIterator(object):
    def __init__(self,ar_ref):
        self.ar_ref = ar_ref
        self.curIndx = 0
    
    def __next__(self):
        if self.curIndx == len(self.ar_ref):
            raise StopIteration
        value = self.ar_ref[self.curIndx]
        self.curIndx += 1
        return value
    
    
# Dynamic Array Class
class DynamicArray:
    def __init__(self,n):
        try:
            if(n <= 0):
                raise InvalidSize(f"Invalid Size, Size passed {n}, Size cannot be less than or equal to 0")
            self._length = n 
            self._capacity = n
        except InvalidSize as IS:
            print(IS)
            sys.exit()
        _allocateMemory = ctypes.py_object*(n) 
        self._elements = _allocateMemory()
        self._clear(None)
    
    def get_Capacity(self):
        return self._capacity
    
    def _clear(self,value):
        for i in range(self._length):
            self._elements[i] = value
    
    def __setitem__(self,ndx,value):
        if ndx>=self._length:
            if ndx>=self._capacity:
                self._resize()
            self._length+=1
        if 0<=ndx<=self._capacity:
            self._elements[ndx] = value
            
        
    def __getitem__(self,ndx):
        try:
            if 0<=ndx<self._length:
                return self._elements[ndx]
            raise IndexOutofRange(f"Index Out of Range, index passed {ndx}, [0,{self._length})")
        except IndexOutofRange as IOo:
            print(IOo)
            sys.exit()
        
        
    def append(self,value):
        if self._length==self._capacity:
            self._resize()
        self._elements[self._length] = value
        self._length+=1
    
    def _resize(self):
        self._capacity *= 2
        temp = self._elements
        self._elements = (ctypes.py_object*self._capacity)()
        self._clear(None)
        for i in range(self._length):
            self._elements[i] = temp[i]
    
    def __len__(self):
        return self._length
    
    def __str__(self):
        s = "["
        for i in range(self._length):
            if i==self._length-1:
                s+=str(self._elements[i])
                break
            s+=str(self._elements[i])+","
        return s+"]"
    
if __name__ == '__main__':
    da = DynamicArray(5)
    for i in range(10):
        da[i] = i
    print(da)
    print(da.get_Capacity())
    for i in range(10,25):
        da[i] = i
    print(da)            
    print(da.get_Capacity())
            
            
            
            
            
            
            
            
            