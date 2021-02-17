class Set(object):
    def __init__(self,elements=[]):
        self.__items = []
        if elements:
            for element in elements:
                self.add(element)
        self._length = len(self.__items)
        self.__curindx = 0
        
    def length(self):
        return self._length
    
    def contains(self,element):
        for i in self.__items:
            if i==element:
                return True
        return False
    
    def add(self,element):
        if not self.contains(element):
            self.__items.append(element)
    
    def remove(self,element):
        if self.contains(element):
            self.__items.remove(element)
    
    def equals(self,setB):
        a = sorted(self.__items)
        b = sorted(setB.__items)
        return a==b
    
    def isSubsetof(self,setB):
        for element in self:
            if element not in setB:
                return False
        return True
    
    def union(self,setB):
        newS = Set()
        for i in self:
            newS.add(i)
        for j in setB:
            newS.add(j)
        return newS
    
    def intersect(self,setB):
        newS = Set()
        for i in self:
            if setB.contains(i):
                newS.add(i)
        for j in setB:
            if self.contains(j):
                newS.add(j)
        return newS
    
    def difference(self,setB):
        newS = Set()
        for i in self:
            if not setB.contains(i):
                newS.add(i)
        for j in setB:
            if not self.contains(j):
                newS.add(j)
        return newS
    
    def sort(self):
        self.__items.sort()
        return self
    
    def List(self):
        return self.__items
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__curindx < len(self.__items):
            curr = self.__items[self.__curindx]
            self.__curindx+=1
            return curr
        else:
            raise StopIteration
            
    def __str__(self):
        if self.length()>100:
            return "<"+",".join([str(i) for i in self.__items[:3]])+" ... "+",".join([str(i) for i in self.__items[-3:]])+">"
        else:
            return "<"+",".join([str(i) for i in self.__items])+'>'
    
    def __len__(self):
        return self.length()
