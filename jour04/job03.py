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

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self._hauteur = hauteur

    def get_hauteur(self):
        return self._hauteur
    
    def set_hauteur(self, value):
        if value > 0:
            self._hauteur = value
        else:
            print("La hauteur doit être positive.")

    def volume(self):
        return self._longueur * self._largeur * self._hauteur
