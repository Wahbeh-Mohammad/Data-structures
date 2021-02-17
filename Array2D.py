from Array import Array

class Array2D(object):
    def __init__(self,numRows,numCols):
        self._theRows = Array(numRows)
        for i in range(numRows):
            self._theRows[i] = Array(numCols)
        self.Clear(None)
        self.Indx = 0
            
    def numRows(self):
        return len(self._theRows)
    
    def numCols(self):
        return len(self._theRows[0])
    
    def Clear(self,value):
        for row in range(self.numRows()):
            self._theRows[row].clear(value)
  
    def __len__(self):
        return len(self._theRows)

    def __getitem__(self,ndxTuple):
        assert len(ndxTuple)==2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows()
        assert col >=0 and col < self.numCols()
        return self._theRows[row][col]
    
    def __setitem__(self,ndxTuple,Value):
        assert len(ndxTuple)==2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows()
        assert col >=0 and col < self.numCols()
        self._theRows[row][col] = Value
    
    def __add__(self,Scalar):
        for row in range(self.numRows()):
            for col in range(self.numCols()):
                self._theRows[row][col]+=Scalar
        return self
    
    def __sub__(self,Scalar):
        for row in range(self.numRows()):
            for col in range(self.numCols()):
                self._theRows[row][col]-=Scalar
        return self
    
    def __mul__(self,Scalar):
        for row in range(self.numRows()):
            for col in range(self.numCols()):
                self._theRows[row][col]*=Scalar
        return self
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.Indx == len(self):
            self.Indx = 0
            raise StopIteration
        else:
            current = self._theRows[self.Indx]
            self.Indx+=1
            return current

    def __str__(self):
        String = ''
        for i,c in enumerate(self):
            if i==0:
                String+='['+str(c)
            elif i==len(self)-1:
                String+='\n '+str(c)+']'
            else:
                String+='\n '+str(c)
        return String