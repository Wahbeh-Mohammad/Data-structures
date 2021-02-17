# Important Libraries
import ctypes 
import sys

# Helper Classes & Custom Errors
# Base error class
class Error(Exception):
    """ """
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

# Iterator Class for the Array
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

# =============================================================================
# Array Class
# =============================================================================
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

if __name__ == '__main__':
    Ar = Array(5)
    Ar._clear(15)
    Ar[4] += 125
    print(Ar)
    for i,c in enumerate(Ar):
        print(i,c)
        
    # Class Array can be used to make a Arrays that have higher dimensions
    # 2d Array Example
    Ar2d = Array(5,Array(5))
    print(Ar2d)
