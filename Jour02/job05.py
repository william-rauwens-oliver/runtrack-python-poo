class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

# Mutateurs (setters) et assesseurs (getters) pour chaque attribut

    def get_marque(self):
        return self.__marque

    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def get_reservoir(self):
        return self.__reservoir
    
# vérifie le niveau de carburant du reservoir

    def __verifier_plein_voiture(self):
        return self.__reservoir
    
# démarrage de la voiture

    def demarrer(self):
        if self.__verifier_plein_voiture() > 5:
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("Le réservoir est trop bas. La voiture ne peut pas démarrer.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture est arrêtée.")

ma_voiture = Voiture("McLaren", "720S", 2023, 3000)

print(ma_voiture.get_marque())
print(ma_voiture.get_modele())
print(ma_voiture.get_annee())
print(ma_voiture.get_en_marche())
print(ma_voiture.get_reservoir())

ma_voiture.demarrer()
ma_voiture.arreter()