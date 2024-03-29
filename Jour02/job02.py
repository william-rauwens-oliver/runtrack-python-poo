class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages

# Assesseurs

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

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

livre1 = Livre("Paris", "Guy de Maupassant", 200)
print(f"Titre: {livre1.get_titre()}, Auteur: {livre1.get_auteur()}, Nombre de pages: {livre1.get_nombre_de_pages()}")

livre1.set_titre("Willy")
livre1.set_auteur("Kevin")
livre1.set_nombre_de_pages(300)

print(f"Titre: {livre1.get_titre()}, Auteur: {livre1.get_auteur()}, Nombre de pages: {livre1.get_nombre_de_pages()}")

livre1.set_nombre_de_pages(-50)