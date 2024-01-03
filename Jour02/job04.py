class Student:
    def __init__(self, nom, prenom, numero_de_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_de_etudiant = numero_de_etudiant
        self.__credits = credits
        self.__level = self._student_eval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
        else:
            print("Erreur : Le nombre de crédits doit etre supérieur à zéro")

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >=60
            return "Passable"
        else: 
            return "Insuffisant"
        
