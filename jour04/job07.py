import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet_cartes = self.creer_paquet()
        self.main_joueur = []
        self.main_croupier = []

    def creer_paquet(self):
        valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def tirer_carte(self):
        return self.paquet_cartes.pop()

    def distribuer_cartes(self):
        self.main_joueur = [self.tirer_carte(), self.tirer_carte()]
        self.main_croupier = [self.tirer_carte(), self.tirer_carte()]

    def calculer_points(self, main):
        total_points = sum(carte.valeur for carte in main)
        as_present = any(carte.valeur == 11 for carte in main)
        
        while total_points > 21 and as_present:
            total_points -= 10
            as_present = any(carte.valeur == 11 for carte in main)
            
        return total_points

    def afficher_principal(self, main, joueur):
        print(f"\nMain {joueur}:")
        for carte in main:
            print(f"{carte.valeur} de {carte.couleur}")

    def jouer_partie(self):
        self.distribuer_cartes()
        
        while True:
            self.afficher_principal(self.main_joueur, "Joueur")
            choix = input("Voulez-vous prendre une carte ? (oui/non): ").lower()
            
            if choix == "oui":
                self.main_joueur.append(self.tirer_carte())
                points_joueur = self.calculer_points(self.main_joueur)
                
                if points_joueur > 21:
                    print("Vous avez dépassé 21 points. Vous avez perdu.")
                    return
            else:
                break
        
        while self.calculer_points(self.main_croupier) < 17:
            self.main_croupier.append(self.tirer_carte())
        
        self.afficher_principal(self.main_joueur, "Joueur")
        self.afficher_principal(self.main_croupier, "Croupier (Banque)")
        
        points_joueur = self.calculer_points(self.main_joueur)
        points_croupier = self.calculer_points(self.main_croupier)
        
        if points_joueur > 21:
            print("Vous avez dépassé 21 points. Vous avez perdu.")
        elif points_joueur > points_croupier or points_croupier > 21:
            print("Félicitations ! Vous avez gagné.")
        elif points_joueur == points_croupier:
            print("Égalité, Personne ne gagne.")
        else:
            print("Désolé le croupier a gagné.")

jeu_blackjack = Jeu()
jeu_blackjack.jouer_partie()