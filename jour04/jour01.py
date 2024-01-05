class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"L'âge de la personne est : {self.age} ans")

    def bonjour(self):
        print("Bonjour")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def __init__(self, age=14):
        Personne.__init__(self, age)

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee=""):
        Personne.__init__(self, age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

personne = Personne()
personne.afficherAge()
personne.bonjour()

eleve = Eleve()
eleve.afficherAge()
eleve.bonjour()
eleve.allerEnCours()

professeur = Professeur(matiereEnseignee="Mathématiques")
professeur.afficherAge()
professeur.bonjour()
professeur.enseigner()