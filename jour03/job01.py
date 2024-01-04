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

