class Animal:
    
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

# Fonction pour saisir l'âge initial et le nom de l'animal
def saisir_infos_animal():
    while True:
        try:
            age_initial = int(input("Veuillez entrer l'âge initial de l'animal : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre entier pour l'âge.")

    nom_animal = input("Veuillez entrer le nom de l'animal : ")
    return age_initial, nom_animal

initial_age, animal_name = saisir_infos_animal()

mon_animal = Animal()

mon_animal.age = initial_age
mon_animal.nommer(animal_name)

print("Âge initial de l'animal :", mon_animal.age)

mon_animal.vieillir()
print("Âge de l'animal après vieillissement :", mon_animal.age)

print("Nom de l'animal :", mon_animal.prenom)