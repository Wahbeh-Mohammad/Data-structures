# In the Module Array
## Classes:
  - Error
  - _ArrayIterator
  - Array

# Class Explainations:
## Error Class
```
class Error(Exception):
  """ Base Class Error """
  def __init__(self,desc):
      self.desc = desc

  def __str__(self):
      return self.desc
```
## This is a base class for custom Exceptions/Errors
## It allows us to define some custom errors such as these below.
```
class InvalidSize(Error):
    """ Invalid Size: Raised when the size passed is less than or equal to 0 """
    def __init__(self,desc):
        Error.__init__(self,desc)

class IndexOutofRange(Error):
    """ IndexOutofRange: Raised when the index is out of bounds"""
    def __init__(self,desc):
        Error.__init__(self,desc)
```

# _ArrayIterator
## This is a helper class that allows the Main class {Array} to become iterable.
```
class _ArrayIterator(object):
    def __init__(self,theArray):
        self._arrayref = theArray
        self.curNdx = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.curNdx<len(self._arrayref):
            entry = self._arrayref[self.curNdx]
            self.curNdx+=1
            return entry
        else:
            raise StopIteration
```

# Array
## The Implementation of the ADT Array has a set of functions and a set of variables
### Variables
- self._elements: The Memory allocated for the elements of the array.
- self._size: The Size of the array.
### Functions
- __init__: method to initialize the array with a size and a specific value.
- __len__: method to return the size of the array.
- __iter__: method for the class to become iterable
- __getitem__: method to retrieve items at a certain index
- __setitem__: method to set the value at a certain index
- _clear: method to set the initial values of the array
- __str__: method to return a string type representation of the array's contents
```
class Array(object):
    def __init__(self, Size,value=None):
        try:
            if( Size <= 0 ):
                raise InvalidSize("Array Size cannot be less than or equal to 0")    
            self._size = Size
        except InvalidSize as ISE:
            print(ISE)
            sys.exit()
        
        # Allocate memory of size = self._size
        pyArrayType = ctypes.py_object*self._size
        self._elements = pyArrayType()
        
        # Fill it with None momentarily
        self._clear(value)
    
    def __len__(self):
        return self._size
    
    def __iter__(self):
        return _ArrayIterator(self._elements)
    
    def __getitem__(self,index):
        try:
            if index >= 0 and index < len(self):
                return self._elements[index]
            raise IndexOutofRange(f"Index out of range {index}, index must be between [0,{len(self)}).")
        except IndexOutofRange as IOo:
            print(IOo)
            sys.exit()
    
    def __setitem__(self,index,value):
        try:
            if index>=0 and index < len(self):
                self._elements[index] = value
            else:
                raise IndexOutofRange(f"Index out of range {index}, index must be between [0,{len(self)})")
        except IndexOutofRange as IOo:
            print(IOo)
            sys.exit()
    
    def _clear(self,value):
        for i in range(len(self)):
            self._elements[i] = value
    
    def __str__(self):
        ret = '['
        for i,c in enumerate(self):
            if(i+1 == len(self)):ret += str(c)
            else: ret += str(c) + ','
        return ret + ']'
```
