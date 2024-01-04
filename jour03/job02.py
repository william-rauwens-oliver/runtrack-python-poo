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

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} EUR effectué avec succès.")
            self.afficher_solde()
        else:
            print("Solde insuffisant. Opération annulée.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux_agios
            self.__solde -= agios
            print(f"Agios de {agios} EUR appliqués.")
            self.afficher_solde()

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} EUR effectué avec succès.")
            self.afficher_solde()
        else:
            print("Solde insuffisant. Virement annulé.")

compte1 = CompteBancaire(numero_compte="12345", nom="Melina", prenom="Herrera", solde=1000)
compte1.afficher()
compte1.versement(500)
compte1.retrait(200)
compte1.agios(taux_agios=0.02)
compte2 = CompteBancaire(numero_compte="67890", nom="Kevin", prenom="Ngo", solde=-200, decouvert=True)
compte2.afficher()
compte1.virement(compte_destinataire=compte2, montant=1200)