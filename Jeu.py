import Interface
class Jeu():
    def __init__(self):
        self.interface = Interface(self)

    def déplacer(self, int):
        print(int)

if __name__ == "__main__":
    jeu = Jeu()
    print("done")