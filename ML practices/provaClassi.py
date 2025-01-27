class Animale:
  def verso(self):
    raise NotImplementedError

class Cane(Animale):
  def verso(self):
    print("Woof!")

class Gatto(Animale):
  def verso(self):
    print("Miao!")

animali = [Cane(), Gatto()]
for animale in animali:
  animale.verso()  # Output: Woof! Miao!