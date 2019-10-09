

import sys

class Queue:
    def __init__(self, initial_capacity):
        self.length_ = initial_capacity
        self.array_ = self.length_ * [0]
        self.tail_ = 0
        self.head_ = 0
        self.num_elements_ = 0

    # size of new array is double of old array; elements are copied from old to new array
    # since queue may wrap around the array, we need to cover such case
    def increase_capacity(self):
        new_length = 2 if self.length_ == 0 else 2 * self.length_
        old_array = self.array_
        self.array_ = new_length * [0]
        for i in range(self.num_elements_):
            self.array_[i] = old_array[(self.head_ + i) % self.length_]
        self.head_ = 0
        self.tail_ = self.num_elements_
        self.length_ = new_length

    def empty(self):
        return self.num_elements_ == 0

    def enqueue(self, x):
        try:
            assert(self.num_elements_!= self.length_)
        except:
            print("Queue Overflow")
            sys.exit()
        
        self.array_[self.tail_]=x

        self.tail_ += 1

        if (self.tail_> self.length_):
            self.tail_ = 1
        
        self.num_elements_ += 1

        return

    def dequeue(self):
        try:
            assert(not(self.empty()))
        except:
            print("Queue Underflow")
            sys.exit()
        
        x = self.head_

        self.head_ += 1
        if (self.head_> self.length_):
            self.head_ = 1
        
        self.num_elements_ -=1

        return x

    # return a list with the elements in queue
    def as_list(self):
        if self.num_elements_ == 0:
            q = []
        elif self.head_ < self.tail_:
            q = self.array_[self.head_:self.tail_]
        else:
            q = self.array_[self.head_:self.length_]
            q.extend(self.array_[0:self.tail_])
        return q[::-1] # reverse elements

    # printing
    def __str__(self):
        return "Queue: len=%d, n=%d, head=%d, tail=%d, array=%s, queue=%s" % (self.length_, self.num_elements_, self.head_, self.tail_, str(self.array_), str(self.as_list()))
    
    __repr__ = __str__