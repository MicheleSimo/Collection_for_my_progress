import random

class WorkerForCinema:
    def __init__(self,nome):
        self.nome = nome
        
class Actor(WorkerForCinema):
    def __init__(self, nome,ruolo):
        super().__init__(nome)
        self.ruolo = ruolo
        
class Director(WorkerForCinema):
    def __init__(self, nome,età,filmGenre):
        super().__init__(nome)
        self.età = 0
        self.filmGenre = filmGenre
        
    def modificaEtà(self):
        self.età = random.randint(28,50)
        
firstDirector = Director("Chris Nolan",0,"Comedy")
print(firstDirector.età)
firstDirector.modificaEtà()
print(firstDirector.età)
#firstDirector.