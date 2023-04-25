import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        self.joueurs = []
        self.croupier = []

    def initialiser_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Pique', 'Trèfle']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        for couleur in couleurs:
            for valeur in valeurs:
                carte = Carte(valeur, couleur)
                self.paquet.append(carte)

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def distribuer_cartes(self):
        for i in range(2):
            for joueur in self.joueurs:
                carte = self.paquet.pop()
                joueur.append(carte)
            carte_croupier = self.paquet.pop()
            self.croupier.append(carte_croupier)

    def ajouter_joueur(self, nom):
        joueur = []
        self.joueurs.append(joueur)

    def afficher_cartes(self, joueur, croupier=False):
        print("Cartes du joueur", joueur+1, ":")
        for carte in self.joueurs[joueur]:
            print(carte.valeur, "de", carte.couleur)
        if croupier:
            print("Cartes du croupier :")
            for carte in self.croupier:
                print(carte.valeur, "de", carte.couleur)

    def calculer_points(self, main):
        total = 0
        as_present = False
        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            elif carte.valeur == 'As':
                as_present = True
                total += 11
            else:
                total += int(carte.valeur)
        if total > 21 and as_present:
            total -= 10
        return total

    def jouer_partie(self):
        self.initialiser_paquet()
        self.melanger_paquet()
        self.distribuer_cartes()
        for i in range(len(self.joueurs)):
            self.afficher_cartes(i)
        self.afficher_cartes(0, croupier=True)
        for i in range(len(self.joueurs)):
            while True:
                choix = input("Joueur " + str(i+1) + ", voulez-vous prendre une carte ? (Oui/Non) ")
                if choix.lower() == 'oui':
                    carte = self.paquet.pop()
                    self.joueurs[i].append(carte)
                    self.afficher_cartes(i)
                    if self.calculer_points(self.joueurs[i]) > 21:
                        print("Le joueur", i+1, "a dépassé 21 points. Il perd.")
                        return
                else:
                    break
        while self.calculer_points(self.croupier) < 17:
            carte = self.paquet.pop()
            self.croupier.append(carte)
            self.afficher_cartes(self.croupier, True)
        points_croupier = self.calculer_points(self.croupier)
        print(f"Total des points pour le croupier: {points_croupier}")

        # Déterminer le gagnant
        for joueur in self.joueurs:
            total_points_joueur = self.calculer_points(joueur)
            if total_points_joueur > 21:
                print(f"{joueur} a dépassé 21 points. Vous avez perdu !")
            elif total_points_joueur > points_croupier:
                print(f"{joueur} a gagné !")
            elif total_points_joueur == points_croupier:
                print(f"{joueur} et le croupier ont le même total de points. C'est un match nul.")
            else:
                print(f"{joueur} a perdu.")

    def afficher_cartes(self, main, croupier=False):
        """Méthode pour afficher les cartes dans la main d'un joueur."""
        if croupier:
            print(f"Croupier: [{self.croupier[0]}] [Carte cachée]")
        else:
            print(f"{main}: {main.cartes}")

    def calculer_points(self, main):
        """Méthode pour calculer le total des points dans une main."""
        total_points = 0
        has_as = False
        for carte in main.cartes:
            total_points += carte.valeur
            if carte.valeur == 1:
                has_as = True
        if has_as and total_points <= 11:
            total_points += 10
        return total_points