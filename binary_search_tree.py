# encoding=utf-8

'''
Basic implementation of a Binary Search Tree using objects in Python.
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
class BinaryTreeNode:

    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None

    def inorder(self, traversal):
        if self.left != None:
            self.left.inorder(traversal)
        traversal.append(self.key)
        if self.right != None:
            self.right.inorder(traversal)

    def __str__(self, indent = 0):
        spacer = ' ' * indent
        return "%s%s" % (spacer, str(self.key))

    def __repr__(self):
        return str(self)

class BinarySearchTreeNode(BinaryTreeNode):
   
    def __init__(self, key):
        BinaryTreeNode.__init__(self, key) 

    def search(self, key):
        if self == None or self.key == key:
            return self

        if key < self.key:
            return self.left.search(key)
        else:
            return self.right.search(key)

    def minimum(self):
        while self != None and self.left != None:
            self = self.left
        return self

    def maximum(self):
        while self != None and self.right != None:
            self = self.right
        return self

    def predecessor(self):
        # Se asume key != None
        # Caso de subarbol izquierdo no vacio
        if self.left != None:
            return self.left.maximum()

        # Caso de subarbol izquierdo vacio
        # y es el padre de x
        y = self.p
        # mientras x sea hijo derecho 
        while y != None and self == y.left:
            self = y
            y = y.p
        return y

    def successor(self):
        # Se asume key != None
        # Caso de subarbol derecho no vacio
        if self.right != None:
            return self.right.minimum()

        # Caso de subarbol derecho vacio
        # y es el padre de x
        y = self.p
        # mientras x sea hijo derecho 
        while y != None and self == y.right:
            self = y
            y = y.p
        return y