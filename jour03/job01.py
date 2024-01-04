class Ville:
    def __init__(self, nom, nombre_habitants):
        self.nom = nom
        self._nombre_habitants = nombre_habitants
    def get_nombre_habitants(self):
        return self._nombre_habitants
    def ajouter_population(self):
        self._nombre_habitants += 1

class Personne:
    def __init__(self, prenom, age, ville):
        self._prenom = prenom
        self._age = age
        self._ville = ville
        ville.ajouter_population()
        
    def ajouter_population(self):
        self._ville.ajouter_population()

paris = Ville("Paris", 1000000)
print(f"Nombre d'habitants à Paris : {paris.get_nombre_habitants()}")

marseille = Ville("Marseille", 861635)
print(f"Nombre d'habitants à Marseille : {marseille.get_nombre_habitants()}")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

print(f"Nombre d'habitants à Paris à l'arrivée de John et Myrtille : {paris.get_nombre_habitants()}")
print(f"Nombre d'habitants à Marseille à l'arrivée de Chloé : {marseille.get_nombre_habitants()}")