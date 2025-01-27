class nodo:
    def __init__(self,dato):
        self.dato = dato
        self.successivo = None
        
class LL:
    def __init__(self):
        self.testa = None
        
    def insertFoward(self,dato):
        newNode = nodo(dato)
        newNode.successivo = self.testa
        self.testa= newNode
        
    def search(self,dato):
        corrente = self.testa
        while corrente:
            if corrente.dato == dato:
                return True
            corrente = corrente.successivo
        return False
    
class Stack:
    def __init__(self):
        self.top = None
        
    def isEmpty(self):
        return True if self.top = None
    
    def push(self,valore):
        newNode = nodo(valore)
        newNode.successivo = self.top
        self.top = newNode
        
    def pop(self):
        if not self.top:
            return None