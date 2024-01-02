class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

mon_animal = Animal()

print("Âge initial de l'animal :", mon_animal.age)

mon_animal.vieillir()
print("Âge de l'animal après vieillissement :", mon_animal.age)

mon_animal.nommer("Fido")
print("Nom de l'animal :", mon_animal.prenom)