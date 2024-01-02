class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)

if __name__ == "__main__":

    joueur = Personnage(0, 0)

    joueur.droite()
    joueur.bas()

    position_actuelle = joueur.position()

    print("Position actuelle du personnage:", position_actuelle)