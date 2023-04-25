import math

class Forme:
    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur

    # Accesseurs
    def get_largeur(self):
        return self.__largeur

    def get_hauteur(self):
        return self.__hauteur

    # Surcharger la méthode aire
    def aire(self):
        return self.__largeur * self.__hauteur


class Cercle(Forme):
    def __init__(self, radius):
        self.__radius = radius

    # Accesseur
    def get_radius(self):
        return self.__radius

    # Surcharger la méthode aire
    def aire(self):
        return math.pi * self.__radius ** 2


# Instanciation de la classe Rectangle
rect = Rectangle(5, 10)
print("Aire du rectangle :", rect.aire())

# Instanciation de la classe Cercle
cercle = Cercle(3)
print("Aire du cercle :", cercle.aire())