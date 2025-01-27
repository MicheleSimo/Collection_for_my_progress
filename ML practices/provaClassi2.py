from math import pi

class FormaGeometrica:
  def __init__(self, nome):
    self.nome = nome

  def area(self):
    raise NotImplementedError

  def perimetro(self):
    raise NotImplementedError

class Cerchio(FormaGeometrica):
  def __init__(self, nome, raggio):
    super().__init__(nome)
    self.raggio = raggio

  def area(self):
    return pi * self.raggio**2

  def perimetro(self):
    return 2 * pi * self.raggio

class Rettangolo(FormaGeometrica):
  def __init__(self, nome, base, altezza):
    super().__init__(nome)
    self.base = base
    self.altezza = altezza

  def area(self):
    return self.base * self.altezza

  def perimetro(self):
    return 2 * (self.base + self.altezza)

# Crea un cerchio e un rettangolo
cerchio = Cerchio("Cerchio 1", 5)
rettangolo = Rettangolo("Rettangolo 1", 4, 6)

# Stampa le aree e i perimetri
print(f"Area del {cerchio.nome}: {cerchio.area()}")
print(f"Perimetro del {cerchio.nome}: {cerchio.perimetro()}")
print(f"Area del {rettangolo.nome}: {rettangolo.area()}")
print(f"Perimetro del {rettangolo.nome}: {rettangolo.perimetro()}")

class Dipendente:
    def __init__(self, nome, cognome, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.stipendio = stipendio

    def calcola_bonus(self):
        return self.stipendio * 0.10

class Manager(Dipendente):
    def __init__(self, nome, cognome, stipendio, reparto):
        super().__init__(nome, cognome, stipendio)  # Chiama il costruttore della classe base
        self.reparto = reparto

    def calcola_bonus(self):
        bonus_base = super().calcola_bonus()  # Ottiene il bonus base dalla classe base
        bonus_reparto = self.stipendio * 0.05  # Aggiunge un bonus specifico per i manager
        return bonus_base + bonus_reparto

class Ingegnere(Dipendente):
    def __init__(self, nome, cognome, stipendio, linguaggio):
        super().__init__(nome, cognome, stipendio)  # Chiama il costruttore della classe base
        self.linguaggio = linguaggio

    def calcola_bonus(self):
        bonus_base = super().calcola_bonus()  # Ottiene il bonus base dalla classe base
        bonus_linguaggio = self.stipendio * 0.15 if self.linguaggio == "Python" else 0  # Bonus extra per gli ingegneri Python
        return bonus_base + bonus_linguaggio


# Crea un manager e un ingegnere
manager = Manager("Mario", "Rossi", 50000, "Vendite")
ingegnere = Ingegnere("Luigi", "Verdi", 60000, "Python")

# Calcola i bonus
print(f"Bonus manager: {manager.calcola_bonus()}")  # Output: 7500.0
print(f"Bonus ingegnere: {ingegnere.calcola_bonus()}")  # Output: 15000.0