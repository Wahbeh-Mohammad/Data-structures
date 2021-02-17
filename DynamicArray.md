# DynamicArray Module
### Same as the module Array
### This module contains a set of custom errors and a helper class called { _ArrayIterator } for making the main class Iterable
### Therefor i won't be explaining them here you can check the file "Array.md" in this branch to see their explainations.

# DynamicArray Class
## Variables
- self._length: a variable that contains how much elements we have added to the array.
- self._capacity: the actual capacity the array can hold.
- self._elements: Same with the Array class this is a reference to the memory allocated for the data.
## Functions
- __init__: to initialize the dynamic array with the size wanted.
- get_Capacity: a method to return the actual capacity of the array.
- _clear: a method to initialize the values of the dynamic array.
- __getitem__: a method to retrieve items at a certain index
- __setitem__: a method to set the value at a certain index
- append: a method to append an item to the end of the array
- _resize: a method to resize the array if the current capacity meets the length
- __len__: a method to return the number of elements the array has
- __str__: a method to return a string type representation of the array's contents
# DynamicArray
``` 
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
```
