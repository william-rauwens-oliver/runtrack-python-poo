import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire, degats):
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        adversaire.vie -= degats

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1 facile, 2 moyen, 3 difficile) : "))

    def lancerJeu(self):
        self.choisirNiveau()

        points_joueur = self.niveau * 10
        points_ennemi = self.niveau * 10

        joueur = Personnage("Joueur", points_joueur)
        ennemi = Personnage("Ennemi", points_ennemi)

        print(f"Le combat commence ! Niveau de difficulté : {self.niveau}")
        self.deroulementPartie(joueur, ennemi)

    def verifierVie(self, personnage):
        if personnage.vie <= 0:
            print(f"{personnage.nom} n'a plus de vie.")

    def verifierGagnant(self, joueur, ennemi):
        if joueur.vie <= 0:
            print("Vous avez perdu. L'ennemi a gagné.")
        elif ennemi.vie <= 0:
            print("Félicitations, vous avez gagné.")
        else:
            return False
        return True

    def deroulementPartie(self, joueur, ennemi):
        while True:
            joueur.attaquer(ennemi, 5)
            self.verifierVie(ennemi)

            ennemi_attaque_points = random.randint(1, 5)
            ennemi.attaquer(joueur, ennemi_attaque_points)
            self.verifierVie(joueur)

            if self.verifierGagnant(joueur, ennemi):
                break

jeu = Jeu()
jeu.lancerJeu()