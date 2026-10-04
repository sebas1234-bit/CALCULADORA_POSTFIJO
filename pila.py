class Pila:
    def __init__(self):
        self.cola = None
        self.cabeza = None

    class Nodo:
        def __init__(self, info=None):
            self.info = info
            self.siguiente = None 

    def push(self, objeto):
        nodo = self.Nodo(objeto)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nodo
        else: 
            self.cola.siguiente = nodo 
        self.cola = nodo
        return nodo

    def pop(self):
        if self.cabeza != None and self.cola != None:
            actual = self.cabeza
            anterior = self.cabeza
            nodo = self.cola
            informacion = self.cola.info
            while(actual != self.cola):
                anterior = actual
                actual = actual.siguiente
            anterior.siguiente = None
            self.cola = anterior
            nodo.info = None
            nodo.siguiente = None
            return informacion




    def mostrar(self):
        actual = self.cabeza
        while actual != None:
            print(actual.info)
            actual = actual.siguiente

pila = Pila()
pila.push(10)
pila.push(20)
pila.push(30)
pila.mostrar()
print()
pila.pop()
pila.mostrar()
    
    
