import sys

class Stack:
    def __init__(self, initial_capacity):
        self.length_ = initial_capacity
        self.array_ = self.length_ * [0]
        self.top_ = -1

    # size of new array is double of old array; elements are copied from old to new array
    def increase_capacity(self):
        new_length = 1 if self.length_ == 0 else 2 * self.length_
        old_array = self.array_
        self.array_ = new_length * [0]
        for i in range(self.length_):
            self.array_[i] = old_array[i]
        self.length_ = new_length

    def empty(self):
        """Devuelve True si la lista esta vacia, False si no """
        return self.top_ == []

    def push(self, x):
        try:
            assert(not(self.top_ == self.length_))
        except:
            print('stack overflow')
            sys.exit()
        
        self.top_=self.top_ + 1
        self.array_[self.top_]=x
        return

    def pop(self):
        try:
            assert(not(self.empty()))
        except:
            print('stack underflow')
            sys.exit()

        self.top_=self.top_ - 1
        return self.array_[0:(self.top_ + 1)]

    # return a list with the elements in stack
    def as_list(self):
        return self.array_[0:(self.top_ + 1)]

    # printing
    def __str__(self):
        return "Stack: len=%d, top=%d, array=%s, stack=%s" % (self.length_, self.top_, str(self.array_), str(self.as_list()))
    
    __repr__ = __str__

S= Stack(12)
print(S)
print(S.empty())
S.push(12)
print(S)
S.pop()
print(S)

