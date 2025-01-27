class Nodo:
    def __init__(self,valore):
        self.valore = valore
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.testa = None
        
    def insertForward(self,testa):
        newNode = Nodo(testa)
        newNode.successivo = self.testa
        self.testa = newNode
        
    def insertBackward(self,dato):
        newNode = Nodo(dato)
        if not self.testa:
            self.testa = newNode
            return
        ultimo = self.testa
        while ultimo.successivo:
            ultimo = ultimo.successivo 
        ultimo.successivo = newNode
        
    def search(self,dato):
        corrente = self.testa
        while corrente:
            if corrente.valore == dato:
                return True
            corrente = corrente.successivo
            
        return False
    
