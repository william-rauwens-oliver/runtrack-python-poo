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
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours de mathématiques va commencer")

eleve = Eleve()
eleve.modifierAge(15)
eleve.bonjour()
eleve.allerEnCours()
eleve.afficherAge()
professeur = Professeur(age=40)
professeur.bonjour()
professeur.enseigner()