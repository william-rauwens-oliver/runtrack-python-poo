class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": self.__statut_commande}

    def annuler_commande(self):
        self.__statut_commande = "annulé"
        for plat in self.__plats_commandes:
            self.__plats_commandes[plat]["statut"] = self.__statut_commande

    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    def afficher_commande(self):
        print(f"Commande #{self.__numero_commande}:")
        for plat, details in self.__plats_commandes.items():
            print(f"{plat}: {details['prix']} € - Statut: {details['statut']}")
        total = self.__calculer_total()
        print(f"Total à payer: {total} €")

    def calculer_tva(self, taux_tva):
        total = self.__calculer_total()
        tva = total * (taux_tva / 100)
        return tva

commande1 = Commande(1)
commande1.ajouter_plat("Lasagne", 9.99)
commande1.ajouter_plat("Coulant au chocolat", 4.99)
commande1.afficher_commande()

tva_calculee = commande1.calculer_tva(5)
print(f"TVA calculée : {tva_calculee} €")

commande1.annuler_commande()
commande1.afficher_commande()