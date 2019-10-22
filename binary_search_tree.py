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