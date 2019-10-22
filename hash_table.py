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

## BaseCLass of hash table for implement in diferent ways
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

## Chaining method of colision resolving
class HashTableWithChaining(HashTable):
    def __init__(self, hash_function, dimension):
        HashTable.__init__(self, hash_function, dimension)
        self.table_ = [ None ] * self.dimension_
        for i in range(self.dimension_):
            self.table_[i] = DoubleLinkedList()

    # Inserta el objeto apuntado por ptr, de tipo ElementForDoubleLinkedList, en el hash 
    def insert(self, ptr):
        k = self.hash_function_(ptr.key_)
        self.table_[k].insert(ptr)
        self.size_ += 1

    # Elimina el objeto apuntado por ptr, de tipo ElementForDoubleLinkedList, del hash
    def delete(self, ptr):
        k = self.hash_function_(ptr.key_)
        self.table_[k].delete(ptr)
        self.size_ -= 1

    # Busca un elemento con clave key
    def search(self, key):
        k = self.hash_function_(key)
        return self.table_[k].search(key)

    # Retorna una representacion en forma de string el hash completo
    def __str__(self):
        as_string = "{"
        for i in range(0,self.dimension_):
            as_string += str(self.table_[i])
        as_string += "}"
    def __repr__(self):
        return str(self)

