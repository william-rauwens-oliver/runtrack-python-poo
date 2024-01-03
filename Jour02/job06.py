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
