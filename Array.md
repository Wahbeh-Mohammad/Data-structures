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
## It allows us to create some custom errors such as these below.
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
