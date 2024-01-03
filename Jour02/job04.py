class Student:
    def __init__(self, nom, prenom, numero_de_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_de_etudiant = numero_de_etudiant
        self.__credits = credits
        self.__level = self._student_eval()

