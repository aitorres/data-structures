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

    def __repr__(self):
        return str(self)

    def reverse(self):
        #Creamos la cola auxiliar que nos servirá para hacer reverse de nuestra lista
        colauxiliar=Queue(self.size_)
        x=self.head_

        # Primero, vaciamos nuestra lista en unacola, de tal forma que el primero que entre
        # Sea el primero en ser insertado
        while x is not None:
            # Asginamos solo el key proque no es necesario ni practico insertar la ED
            y=x.key_ 
            colauxiliar.enqueue(y)
            self.delete(self.head_)
            x=self.head_
        
        # Dado que la inserción en la lista funciona como una pila, el primero en ser insertado
        # sera el ultimo de la lista. Y como el primero en la cola, es el primero de la lista
        # original, al insertarlo será el ultimo de la nueva lista, cumpliendo con lo requerido
        for i in range(0,colauxiliar.length_):
            z=colauxiliar.dequeue()
            #Creamos una nueva estrucutra, que insertaremos en la lista
            PorInsertar=ElementForDoubleLinkedList(z)
            self.insert(PorInsertar)
        
        return
    
    def clone(self):
        # Creamos la lista a ser clonada y tomamos el primer elemento
        clonedList=DoubleLinkedList()
        x=self.head_

        # Luego, agregamos a la nueva lista, cada elemento de la anterior, creando
        # un nuevo elemento para cada inserción
        while x is not None:
            y=ElementForDoubleLinkedList(x.key_)
            clonedList.insert(y)
            x=x.next_

        # Como la inserción de la lista funciona como una pila, para que la copia
        # sea exacta, hacemos reverse de la lista para que quede como la original
        clonedList.reverse()
        return clonedList

    # Sin modificar la lista original, determina si una lista es palindrome
    def palindrome(self):
        # Creamos 2 copias para no utilizar la lista original y a una le aplicamos
        # reverse, de tal forma que si es palindormo, debe permanecer igual en su
        # contenido
        l1= self.clone()
        l2= self.clone()
        l2.reverse()

        # De entrada asignamos el valor True a la variable resultado. Que solo cambia
        # de valor si en algun momento los elementos son diferentes
        resultado=True

        # Evaluamos cada elemento de l1 con l2 reversed, de tal formaque si es palindromo
        # al evaluar cada head, sus contenidos deberian ser iguales 
        for i in range(0,l1.size_-1):
            # Buscamos el valor de cada head para compararlo
            x=l1.head_.key_
            y=l2.head_.key_

            # Comparamos los valores, si son diferentes, resultado se vuelve false y por
            # tanto no es palindromo
            if x!=y:
                resultado=False
            
            # Eliminamos los head para evaluar los siguientes
            l1.delete(l1.head_)
            l2.delete(l2.head_)

        return resultado