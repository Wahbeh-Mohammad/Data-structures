# In the Module Array
## Classes:
  - Error
  - _ArrayIterator
  - Array

## Class Explainations:
  # Error Class
  ```
  class Error(Exception):
    """ """
    def __init__(self,desc):
        self.desc = desc
    
    def __str__(self):
        return self.desc
  ```
