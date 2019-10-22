# encoding=utf-8

'''
Basic implementation of a Double Linked list using objects in Python.
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

from Queue import Queue

class ElementForDoubleLinkedList:

    def __init__(self, key = None):
        self.prev_ = None
        self.key_ = key
        self.next_ = None

    def __str__(self):
        return "[%s]" % str(self.key_)
    
    def __repr__(self):
        return str(self)


