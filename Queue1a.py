##
## =======================================================
## Nichole Huang (20995930)
## CS 234 Fall 2024
## Assignment 2, P1
## =======================================================
##

from Stack import *
from contiguous import *      


class QueueUsingStacks:
    """
    Queue class implementing a queue using two stacks.
    """
    def __init__(self):
        """
        QueueUsingStacks() produces a new, empty queue.
        Effects: Creates a new, empty queue.
        __init__: -> Queue
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def create(self):
        """
        self.create() initializes a new queue.
        Effects: Resets the queue to empty.
        create: QueueUsingStacks -> None
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def is_empty(self):
        """
        self.is_empty() produces True if the queue is empty and False otherwise.
        is_empty: QueueUsingStacks -> Bool
        """
        return self.stack1.is_empty() and self.stack2.is_empty()

    def front(self):
        """
        self.front() produces the front item without removing it.
        front: QueueUsingStacks -> Any
        Requires: self is nonempty
        """
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.top()
         
    def enqueue(self, value):
        """
        self.enqueue(value) adds value to the queue.
        Effects: Adds value to the queue.
        enqueue: QueueUsingStacks Any -> None
        """
        self.stack1.push(value)
        
    def dequeue(self):
        """
        self.dequeue() produces and removes the front item from the queue.
        Effects: Removes the front item from the queue.
        dequeue: QueueUsingStacks -> Any
        Requires: self is nonempty
        """
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.pop()


