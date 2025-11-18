class Pile():   
    def __init__(self) -> None:
        """
        Create the stack.
        """
        self._stack : list = []
        self._size : int = 0
        return None
    
    def empile(self, value) -> None:
        """
        Add an element at the top of the stack.
        """
        self._stack += [value]
        self._size += 1
        return None
    
    def unpile(self):
        """
        Delete and return the last element of the stack.
        Return -1 if the stack is empty.
        """
        if self.IsEmpty():
            return -1
        
        self._size -= 1
        value = self._stack[-1]
        del self._stack[-1]

        return value
    
    def IsEmpty(self) -> bool:
        """
        Check if the stack is empty, True if it is and False if it isn't.
        """
        if self._size == 0:
            return True
        else:
            return False
    
    def GetSize(self) -> int:
        """
        Return the size of the stack.
        """
        return self._size

    def GetStack(self) -> list:
        """
        Return the stack as a list.
        """
        return self._stack
    
    def CountScore(self) -> int:
        """
        To the sum of all the integers of the stack and return it.
        """
        score : int = 0
        while not self.IsEmpty():
            score += self.unpile()
        return score