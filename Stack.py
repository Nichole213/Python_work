import contiguous

class Stack:
     #DO NOT EDIT THIS MODULE#
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0

    def top(self):
        if self.is_empty():
            return None
        return self._items[-1]
    
    
stack1 = Stack()