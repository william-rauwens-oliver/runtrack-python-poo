import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    def attaquer(self, adversaire, degats):
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégats.")
        adversaire.vie -= degats