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

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.nelements = 0

    def inorder(self, traversal):
        if self.root != None:
            self.root.inorder(traversal)

    def search(self, key):
        if self.root == None:
            return None
        else:
            return self.root.search(key)

    def minimum(self):
        # Se hace la llamada a la funcion de los nodos del arbol binario de busqueda
        return self.root.minimum()

    def maximum(self):
        # Se hace la llamada a la funcion de los nodos del arbol binario de busqueda
        return self.root.maximum()

    def predecessor(self, ptr):
        # Se hace la llamada a la funcion de los nodos del arbol binario de busqueda
        if ptr == None:
            raise Exception("BinarySearchTree: predecessor() called on <null> reference")
        else:
            return ptr.predecessor()

    def successor(self, ptr):
        # Se hace la llamada a la funcion de los nodos del arbol binario de busqueda
        if ptr == None:
            raise Exception("BinarySearchTree: successor() called on <null> reference")
        else:
            return ptr.successor()

    def insert(self, z):
        y = None
        x = self.root
        # Se busca donde insertar
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        # Asignar y como nuevo padre del nuevo nodo z
        z.p = y
        # El arbol esta vacio
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self.nelements = self.nelements + 1

    def transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != None: v.p = u.p


    def delete(self, z):
        if z.left == None:
            # Caso 1 y 2 (z sin subarbol izquierdo)
            self.transplant(z, z.right)
        elif z.right == None:
            # Caso 2 (z sin subarbol derecho)
            self.transplant(z, z.left)
        else:
            # Caso 3 (z tiene ambos hijos)
            # y es sucesor de z 
            y = z.right.minimum()
            if y.p != z:
                # caso 3: y es hijo izquierdo 
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
        self.nelements = self.nelements - 1

    def size(self):
        return self.nelements

    def __str__(self):
        if self.root == None:
            return "<empty-tree>"
        else:
            inorder_ = []
            self.root.inorder(inorder_)
            return str(inorder_)
            
    def __repr__(self):
        return str(self)