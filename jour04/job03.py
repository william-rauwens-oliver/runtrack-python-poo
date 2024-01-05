class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur
    def get_longueur(self):
        return self._longueur
    def set_longueur(self, value):
        if value > 0:
            self._longueur = value
        else:
            print("La longueur doit être positive.")

    def get_largeur(self):
        return self._largeur
    def set_largeur(self, value):
        if value > 0:
            self._largeur = value
        else:
            print("La largeur doit être positive.")

    def perimetre(self):
        return 2 * (self._longueur + self._largeur)
    def surface(self):
        return self._longueur * self._largeur
