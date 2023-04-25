class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Assesseur pour la longueur
    def get_longueur(self):
        return self.__longueur

    # Mutateur pour la longueur
    def set_longueur(self, longueur):
        self.__longueur = longueur

    # Assesseur pour la largeur
    def get_largeur(self):
        return self.__largeur

    # Mutateur pour la largeur
    def set_largeur(self, largeur):
        self.__largeur = largeur

# Création d'un rectangle avec une longueur de 10 et une largeur de 5
rectangle1 = Rectangle(10, 5)

# Accès aux valeurs initiales des attributs longueur et largeur
print("Longueur du rectangle : ", rectangle1.get_longueur())  # Affiche "Longueur du rectangle : 10"
print("Largeur du rectangle : ", rectangle1.get_largeur())  # Affiche "Largeur du rectangle : 5"

# Modification de la longueur et de la largeur du rectangle
rectangle1.set_longueur(15)
rectangle1.set_largeur(7)

# Vérification des modifications
print("Longueur du rectangle après modification : ", rectangle1.get_longueur())  # Affiche "Longueur du rectangle après modification : 15"
print("Largeur du rectangle après modification : ", rectangle1.get_largeur())  # Affiche "Largeur du rectangle après modification : 7"
