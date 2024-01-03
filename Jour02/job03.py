class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
        self.__disponible = True

# Assesseurs

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    def est_disponible(self):
        return self.__disponible

# Mutateurs

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nombre_de_pages(self, nouveau_nombre_de_pages):
        if isinstance(nouveau_nombre_de_pages, int) and nouveau_nombre_de_pages > 0:
            self.__nombre_de_pages = nouveau_nombre_de_pages
        else:
            print("Erreur : Le nombre de pages demandé doit être un nombre entier positif !")

    def emprunter(self):
        if self.est_disponible = False
            self.__disponible = False
            print("Livre emprunté avec succés.")
        else:
            print("Erreur : Le livre ne peut pas etre emprunté.")

    def rendre(self):
        if not self.est_disponible():
            self.__disponible = True
            print("Livre rendu avec succès.")
        else :
            print ("Erreur ! Le livre n'a pas été emprunté.")