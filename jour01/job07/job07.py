class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    # Assesseur pour le titre
    def get_titre(self):
        return self.__titre

    # Mutateur pour le titre
    def set_titre(self, titre):
        self.__titre = titre

    # Assesseur pour l'auteur
    def get_auteur(self):
        return self.__auteur

    # Mutateur pour l'auteur
    def set_auteur(self, auteur):
        self.__auteur = auteur

    # Assesseur pour le nombre de pages
    def get_nb_pages(self):
        return self.__nb_pages

    # Mutateur pour le nombre de pages
    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

# Création d'un livre avec un titre, un auteur et un nombre de pages
livre1 = Livre("Titre du livre", "Auteur du livre", 200)

# Accès aux valeurs initiales des attributs titre, auteur et nombre de pages
print("Titre du livre : ", livre1.get_titre())  # Affiche "Titre du livre : Titre du livre"
print("Auteur du livre : ", livre1.get_auteur())  # Affiche "Auteur du livre : Auteur du livre"
print("Nombre de pages du livre : ", livre1.get_nb_pages())  # Affiche "Nombre de pages du livre : 200"

# Modification du titre, de l'auteur et du nombre de pages du livre
livre1.set_titre("Nouveau titre du livre")
livre1.set_auteur("Nouvel auteur du livre")
livre1.set_nb_pages(300)

# Vérification des modifications
print("Titre du livre après modification : ", livre1.get_titre())  # Affiche "Titre du livre après modification : Nouveau titre du livre"
print("Auteur du livre après modification : ", livre1.get_auteur())  # Affiche "Auteur du livre après modification : Nouvel auteur du livre"
print("Nombre de pages du livre après modification : ", livre1.get_nb_pages())  # Affiche "Nombre de pages du livre après modification : 300"

# Tentative de modification du nombre de pages avec une valeur invalide
livre1.set_nb_pages(-50)  # Affiche "Erreur : Le nombre de pages doit être un nombre entier positif."
