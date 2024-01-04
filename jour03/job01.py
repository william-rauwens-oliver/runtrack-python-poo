class Ville:
    def __init__(self, prenom, nombre_habitants):
        self.prenom = prenom
        self.nombre_habitants = nombre_habitants
    def get_nombre_habitants(self):
        return self._nombre_habitants
    def ajouter_population(self):
        self.get_nombre_habitants +=1

class Personne:
    def __init__(self, prenom, age, ville):
            self._prenom = prenom
            self._age = age
            self.ville = ville
            ville.ajouter_population()

    def ajouter_population(self):
         self._ville.ajouter_population()

paris = Ville("Paris", 1000000)
print(f"Nombre d'habitants à Paris : {paris.get_nombre_habitants}")

marseille = Ville("Marseille", 861635)
print(f"Nombre d'habitant à Marseille : {marseille.get_nombre_habitants}",)

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)
