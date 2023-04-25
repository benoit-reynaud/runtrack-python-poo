class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True  # Nouvel attribut "disponible" initialisé à True par défaut

    # Assesseurs et mutateurs pour titre, auteur, nb_pages (comme dans l'exemple précédent)
    ...

    # Méthode pour vérifier si le livre est disponible
    def vérification(self):
        return self.__disponible

    # Méthode pour emprunter le livre
    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    # Méthode pour rendre le livre
    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre est déjà disponible.")

# Création d'un livre avec un titre, un auteur et un nombre de pages
livre1 = Livre("Titre du livre", "Auteur du livre", 200)

# Accès à la valeur de l'attribut disponible
print("Disponibilité du livre : ", livre1.vérification())  # Affiche "Disponibilité du livre : True"

# Emprunt du livre
livre1.emprunter()  # Affiche "Le livre a été emprunté."

# Tentative d'emprunt du livre déjà emprunté
livre1.emprunter()  # Affiche "Le livre n'est pas disponible pour l'emprunt."

# Rendu du livre
livre1.rendre()  # Affiche "Le livre a été rendu."

# Tentative de rendu du livre déjà rendu
livre1.rendre()  # Affiche "Le livre est déjà disponible."

# Vérification de la disponibilité du livre après rendu
print("Disponibilité du livre après rendu : ", livre1.vérification())  # Affiche "Disponibilité du livre après rendu : True"
