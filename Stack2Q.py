import sys 
from Queue import Queue

class StackWithQueues:
    
    def __init__(self, initial_capacity):
        self.length_ = initial_capacity
        self.array_ = self.length_ * [0]
        self.top_ = -1
        Q1=Queue(self.length_)
        Q2=Queue(self.length_)
        return     
    
    def empty(self):
        """Devuelve True si la lista esta vacia, False si no """
        return self.top_ == []

    def push(self, x):
        try:
            assert(not(self.top_ == self.length_))
        except:
            print('stack overflow')
            sys.exit()
        
        Q1.enqueue(x)
        return

    def pop(self):
        try:
            assert(not(self.empty()))
        except:
            print('stack underflow')
            sys.exit()

        self.top_=self.top_ - 1
        return self.array_[0:(self.top_ + 1)]


    # return a list with the elements in queue
    def as_list(self):
        return []

    # printing
    def __str__(self):
        return "Stack: len=%d, top=%d, array=%s, stack=%s" % (self.length_, Q1.array_, Q1)

    __repr__ = __str__








