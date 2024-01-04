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

    def tacheFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminée"
                print(f"Tache marquée comme terminée : {tache.titre}")
                return
            print{f"Tache introuvable : {titre}"}
            
    def afficherListe(self):
        print("Liste des tâches :")
        for tache in self.taches:
            print(f"{tache.titre} - {tache.statut}")
    
    def ListeFiltrer(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        print(f"Tâches avec le statut '{statut}':")
        for tache in filtered_list:
            print(f"{tache.titre} - {tache.statut}")
        return filtered_list