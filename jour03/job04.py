class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            print(f"{joueur.nom} - Buts: {joueur.buts_marques}, Passes décisives: {joueur.passes_decisives}, Cartons jaunes: {joueur.cartons_jaunes}, Cartons rouges: {joueur.cartons_rouges}")

    def mettreAJourStatistiquesJoueur(self, joueur, buts=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        joueur.buts_marques += buts
        joueur.passes_decisives += passes_decisives
        joueur.cartons_jaunes += cartons_jaunes
        joueur.cartons_rouges += cartons_rouges

joueur1 = Joueur("Neymar Jr", 10, "Attaquant")
joueur2 = Joueur("Kevin Mbappe", 5, "Milieu")
joueur3 = Joueur("Raphael Varane", 3, "Défenseur")
joueur4 = Joueur("Mohamed Salah", 7, "Attaquant")
joueur5 = Joueur("Bruno Fernandes", 8, "Milieu")
joueur6 = Joueur("Andrew Robertson", 2, "Défenseur")
joueur7 = Joueur("Erling Haaland", 11, "Attaquant")
joueur8 = Joueur("Joshua Kimmich", 6, "Milieu")
joueur9 = Joueur("Ruben Dias", 4, "Défenseur")
joueur10 = Joueur("Harry Kane", 9, "Attaquant")
joueur11 = Joueur("Jan Oblak", 1, "Gardien")

equipe1 = Equipe("ÉquipeC")
equipe2 = Equipe("ÉquipeD")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)
equipe1.ajouterJoueur(joueur4)
equipe1.ajouterJoueur(joueur5)
equipe2.ajouterJoueur(joueur6)
equipe2.ajouterJoueur(joueur7)
equipe2.ajouterJoueur(joueur8)
equipe2.ajouterJoueur(joueur9)
equipe2.ajouterJoueur(joueur10)
equipe2.ajouterJoueur(joueur11)

joueur1.marquerUnBut()
joueur2.effectuerUnePasseDecisive()
joueur3.recevoirUnCartonJaune()

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

equipe1.mettreAJourStatistiquesJoueur(joueur1, buts=1)
equipe1.mettreAJourStatistiquesJoueur(joueur2, passes_decisives=1)
equipe2.mettreAJourStatistiquesJoueur(joueur3, cartons_jaunes=1)

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()