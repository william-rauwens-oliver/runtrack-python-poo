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

# Créer plusieurs produits
produit1 = Produit("Produit1", 50, 20)
produit2 = Produit("Produit2", 30, 10)
produit3 = Produit("Produit3", 80, 15)

print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

# Prix modifier de chaque produit
produit1.modifier_nom("Nouveau Produit1")
produit1.modifier_prix(60)

produit2.modifier_nom("Nouveau Produit2")
produit2.modifier_prix(35)

produit3.modifier_nom("Nouveau Produit3")
produit3.modifier_prix(90)

print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())