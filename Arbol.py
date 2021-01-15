puntero= 0
x= 0

class NodoArbol:

    def __init__(self, value, izq= None, der= None):
        self.data= value
        self.izq= izq
        self.der= der

    def recorrer(self):
        global contador
        print(self.data, "Nivel: ", contador)
        if self.izq:
            contador +=1
            self.izq.recorrer()
        elif self.der:
            contador +=1
            self.der.recorrer()
        contador= 0

