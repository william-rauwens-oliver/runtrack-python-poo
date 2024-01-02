class Animal():
    def __init__(self, prenom="", age = 0):
        self.prenom = prenom
        self.age = age

    def veillir(self):
        self.age = input("Quel est l'age de votre animal :")
        self.age =+1
        print("Animal a", self.age)
    
    def nommer(self):
        self.prenom = input("Quel est le nom de votre animal :")
        print("Le nom de l'animal est", self.prenom)

patte = Animal()

patte.veillir()
patte.nommer()