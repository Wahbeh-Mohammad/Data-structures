from Array2D import Array2D

class Matrix(object):
    def __init__(self,nRows,nCols):
        self._theGrid = Array2D(nRows,nCols)
        self._theGrid.Clear(0)
    
    def numRows(self):
        return self._theGrid.numRows()
    
    def numCols(self):
        return self._theGrid.numCols()
    
    def Clear(self,value):
        for i in range(self.numRows()):
            self._theGrid.Clear(value)
    
    def __len__(self):
        return len(self._theGrid)
    
    def __getitem__(self,ndxTuple):
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row>=0 and row<self.numRows()
        assert col>=0 and col<self.numCols()
        return self._theGrid[row,col]
    
    def __setitem__(self,ndxTuple,value):
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row>=0 and row<self.numRows()
        assert col>=0 and col<self.numCols()
        self._theGrid[row,col] = value
        return self
    
    def __add__(self,rhsMat):
        if self.numCols()==rhsMat.numCols():
            if self.numRows()==rhsMat.numRows():
                NewMat = Matrix(self.numRows(),self.numCols())
                for i in range(self.numRows()):
                    for j in range(self.numCols()):
                        NewMat._theGrid[i,j] = self._theGrid[i,j]+rhsMat._theGrid[i,j]
                return NewMat

    def __sub__(self,rhsMat):
        if self.numCols()==rhsMat.numCols():
            if self.numRows==rhsMat.numRows():
                NewMat = Matrix(self.nRows(),self.numCols())
                for i in range(self.nRows()):
                    for j in range(self.nCols()):
                        NewMat[i,j] = self._theGrid[i,j]-rhsMat._theGrid[i,j]
                return NewMat
        
    def __mul__(self,Scalar):
        NewMat = Matrix(self.numRows(),self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                NewMat[i,j] = self._theGrid[i,j]*Scalar
        return NewMat

    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self._theGrid)
        
    def __str__(self):
        return str(self._theGrid)