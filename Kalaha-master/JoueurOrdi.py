from Joueur import Joueur
from random import *
class JoueurOrdi(Joueur):
    def __init__(self, difficulty):
        self.humain = False
        self.difficulty = difficulty

    def jouer(self):
        return randint(0, 5)


if __name__ == "__main__":
    j2 = JoueurOrdi(1)

    print(j2.jouer())


