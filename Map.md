# Map
## Variables:
- self._entryList : a list that has the map entries
## Functions:
- __init__: method to initialize the map
- add: method to add a new map entry
- valueOf: returns the value of a key
- __iter__: to make the class Map iterable
- _findPosition: returns the index of a key, if not found returns None
- __len__: returns the length of the map
- __contains__: returns True/False whether the key is in the map or not
- __str__: string representation of the map
```
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
```
