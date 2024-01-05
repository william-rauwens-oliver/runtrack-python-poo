class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
    
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
    def aire(self):
        return 3.14 * self.radius ** 2
    
rectangle = Rectangle(6, 13)
aire_rectangle = rectangle.aire()
print(f"L'aire du rectangle demandé est : {aire_rectangle}")

cercle = Cercle(5)
air_cercle = cercle.aire()
print(f"L'air du cercle demandé est : {air_cercle}")