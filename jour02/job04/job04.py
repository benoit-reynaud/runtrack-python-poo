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


# Instanciation de la classe Rectangle
rect = Rectangle(5, 10)
print("Aire du rectangle :", rect.aire())