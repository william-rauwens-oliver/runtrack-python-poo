class Produit:
    def __init__(self, nom, prixHT, tva):
        self.nom = nom
        self.prixHT = prixHT
        self.tva = tva

    def calculer_prix_ttc(self):
        return self.prixHT * (1 + self.tva / 100)

    def afficher(self):
        info_produit = f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.tva}%, Prix TTC: {self.calculer_prix_ttc()}"
        return info_produit

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def obtenir_nom(self):
        return self.nom

    def obtenir_prix_ht(self):
        return self.prixHT

    def obtenir_tva(self):
        return self.tva