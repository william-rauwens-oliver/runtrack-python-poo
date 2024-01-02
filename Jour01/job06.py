class Animal:
    def __init__(self, age=0):
        self.age = age
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

age_saisi = int(input("Entrez l'âge de l'animal : "))

mon_animal = Animal(age=age_saisi)

print("L'âge de l'animal avant l'appel de la méthode vieillir:", mon_animal.age, "ans")

mon_animal.vieillir()

print("L'âge de l'animal après l'appel de la méthode vieillir:", mon_animal.age, "ans")

nom_saisi = input("Entrez le nom de l'animal : ")

mon_animal.nommer(nom_saisi)

print("Le nom de l'animal est :", mon_animal.prenom)