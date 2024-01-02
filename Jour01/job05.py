class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée x : {self.x}")

    def afficherY(self):
        print(f"Coordonnée y : {self.y}")

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y

point1 = Point(3, 5)

point1.afficherLesPoints()

point1.afficherX()

point1.afficherY()

point1.changerX(8)

point1.changerY(10)

point1.afficherLesPoints()