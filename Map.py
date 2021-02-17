# Helper Classes
class _MapEntry:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __str__(self):
        return "{" + f"{self.key} : {self.value}" + "}"

class _MapIterator:
    def __init__(self,theList):
        self.List = theList
        self.curndx = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if 0<=self.curndx<len(self.List):
            cur = self.List[self.curndx]
            self.curndx+=1
            return cur
        else:
            raise StopIteration

# Custom Errors
class Error(Exception):
    def __init__(self,desc):
        self.desc = desc
    
    def __str__(self):
        return self.desc

class KeyNotFound(Error):
    def __init__(self,desc):
        Error.__init__(self,desc)

# Map Class
class Map(object):
    def __init__(self):
        self._entryList = []
    
    def add(self,key,value):
        ndx = self._findPosition(key)
        if ndx is not None:
            self._entryList[ndx].value = value
        else:
            entry = _MapEntry(key,value)
            self._entryList.append(entry)
            
    def valueOf(self,key):
        ndx = self._findPosition(key)
        if ndx is None:
            raise KeyNotFound("Key not Found.")
        return self._entryList[ndx].value
    
    def __iter__(self):
        return _MapIterator(self._entryList)
    
    def _findPosition(self,key):
        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
        return None
    
    def __len__(self):
        return len(self._entryList)

    def __contains__(self,key):
        ndx = self._findPosition(key)
        return ndx is not None
    
    def __str__(self):
        S = ",".join([str(i) for i in self._entryList])
        return "("+S+")"
    
if __name__ == '__main__':
    X = Map()
    X.add(1,1)
    X.add(2,4)
    X.add(3,9)
    for entry in X:
        print(entry)
    print(X)