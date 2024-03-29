class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeTaches:
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

    def TacheFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminée"
                print(f"Tâche marquée comme terminée : {tache.titre}")
                return
        print(f"Tâche introuvable : {titre}")

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

tache1 = Tache("Faire les courses", "Acheter des légumes et du lait")
tache2 = Tache("Répondre aux emails", "Vérifier la boîte de réception")
tache3 = Tache("Faire du sport", "30 minutes de jogging")
liste_de_taches = ListeTaches()
liste_de_taches.ajouterTache(tache1)
liste_de_taches.ajouterTache(tache2)
liste_de_taches.ajouterTache(tache3)
liste_de_taches.afficherListe()
liste_de_taches.TacheFinie("Faire les courses")
liste_de_taches.supprimerTache("Répondre aux emails")
liste_de_taches.afficherListe()
taches_a_faire = liste_de_taches.ListeFiltrer("à faire")