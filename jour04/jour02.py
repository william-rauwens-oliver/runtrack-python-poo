class Personne:
    def __init__(self, age=14):
        self.age = age

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
        print(f"Le cours de {self.__matiereEnseignee} va commencer")

eleve = Eleve()
eleve.modifierAge(15)
eleve.bonjour()
eleve.allerEnCours()
eleve.afficherAge()
professeur = Professeur(age=40, matiereEnseignee="Mathématiques")
professeur.bonjour()
professeur.enseigner()