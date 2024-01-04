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