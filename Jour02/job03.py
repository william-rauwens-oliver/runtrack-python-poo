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
