# encoding=utf-8

'''
Basic implementation of a Hash table using classes and a Linked List in Python.
Implemented in Python 3.7.6
Source:
    Cormen, T. et al. "Introduction to Algorithms", 2nd Edition
Author:
    Luis Alfonso Pino
    @lapy0110 on github
Tutor:
    Andrés Ignacio Torres
    @aitorres on github
    @andresitorresm on twitter
'''

class HashTable:
    def __init__(self, hash_function, dimension):
        self.hash_function_ = hash_function
        self.dimension_ = dimension
        self.size_ = 0

    def dimension(self):
        return self.dimension_

    def size(self):
        return self.size_

    def load_factor(self):
        return float(self.size_) / float(self.dimension_)

    def contains(self, key):
        return self.search(key) != None