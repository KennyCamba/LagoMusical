from tda.node import Node


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.__size__ = 0
        # Diccionario para acceso eficiente a los nodos
        self.nodes = dict() 
    
    @property
    def size(self):
        return self.__size__

    def add(self, data):
        """
        Agrega un elemento al final de la lista.
        """
        node = Node(data)
        self.nodes[data] = node
        if self.first == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.__size__ += 1        
        
    
    def next(self, data):
        """	
        Devuelve el elemento siguiente de un elemento dado (data).
        """
        node = self.nodes.get(data)
        if node == None:
            return -1
        
        if node.next == None:
            return None
        
        return node.next.value
    
    
    def contains(self, data):
        """
        Devuelve True si el elemento dado (data) está en la lista.
        """
        return self.nodes.get(data) != None