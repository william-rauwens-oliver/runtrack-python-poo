class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte : {self.__numero_compte}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Solde : {self.__solde} EUR")
        print(f"Découvert autorisé : {self.__decouvert}")
        print("\n")

    def afficher_solde(self):
        print(f"Le solde actuel est de : {self.__solde} EUR")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} EUR effectué avec succès.")
        self.afficher_solde()

