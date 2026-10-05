class Cola:
    def __init__(self):
        self.cabeza = self.Nodo()
        self.cola = self.Nodo()
        self.cabeza.siguiente = self.cola
        self.cola.anterior = self.cabeza


    class Nodo:
        def __init__(self, info=None):
            self.anterior = None
            self.siguiente = None
            self.info = info

    def add(self, objeto):
        nodo = self.Nodo(objeto)
        if (self.cabeza.siguiente == None and self.cola.anterior == None):
            self.cabeza.siguiente = nodo
            self.cola.anterior = nodo
            nodo.anterior = self.cabeza
            nodo.siguiente = self.cola
            return nodo
            
        else:
            anterior = self.cola.anterior 
            siguiente = self.cola
            anterior.siguiente = nodo
            nodo.siguiente = siguiente
            siguiente.anterior = nodo
            nodo.anterior = anterior
            return nodo
        
    def peek(self):
        if self.cabeza.siguiente != None and self.cola.anterior != self.cabeza:
            return self.cabeza.siguiente.info
        else:
            return None

    def poll(self):
        if self.cabeza.siguiente != None and self.cola.anterior != self.cabeza:
            nodo = self.cabeza.siguiente
            informacion = nodo.info
            anterior = self.cabeza
            siguiente = nodo.siguiente
            anterior.siguiente = siguiente
            siguiente.anterior = anterior
            nodo.anterior = None
            nodo.siguiente = None
            nodo.info = None
            del nodo
            return informacion
        return None

        
    def mostrar(self):
        actual = self.cabeza.siguiente
        while actual != self.cola:
            print(actual.info)
            actual = actual.siguiente




