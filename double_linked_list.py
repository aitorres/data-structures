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


class DoubleLinkedList:
    
    def __init__(self):
        self.size_ = 0
        self.head_ = None

    def empty(self):
        return self.size_ == 0

    def size(self):
        return self.size_

    # asume que ptr es un apuntador a ElementForDoubleLinkedList                                                  
    def insert(self, ptr):
        ptr.next_ = self.head_
        if self.head_ != None:
            self.head_.prev_ = ptr
        ptr.prev_ = None
        self.head_ = ptr
        self.size_ += 1

    # asume que ptr es un apuntador a ElementForDoubleLinkedList                                                  
    def delete(self, ptr):
        if ptr.prev_ != None:
            ptr.prev_.next_ = ptr.next_
        if ptr.next_ != None:
            ptr.next_.prev_ = ptr.prev_
        if ptr.prev_ == None:
            self.head_ = ptr.next_
        self.size_ -= 1
               
    # busca key en la lista                                                                                       
    def search(self, key):
        ptr = self.head_
        while ptr != None and ptr.key_ != key:
            ptr = ptr.next_
        return ptr 
    
    # retorna una representacion en forma de string de los elementos en la lista                                  
    def __str__(self):
        as_string = "{"
        x = self.head_
        while x is not None:
            as_string += "%s" % str(x)
            if x.next_ is not None: as_string += ","
            x = x.next_
        as_string += "}"
        return as_string

    