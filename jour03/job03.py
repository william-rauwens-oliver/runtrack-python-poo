class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tâche ajoutée : {tache.titre}")

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                print(f"Tâche supprimée : {tache.titre}")
                return
        print(f"Tâche introuvable : {titre}")
