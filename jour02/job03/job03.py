class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Accesseurs
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    # Accesseur
    def get_hauteur(self):
        return self.__hauteur

    # Mutateur
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.__longueur * self.__largeur * self.__hauteur
    
    
    # Instanciation de la classe Rectangle
rect = Rectangle(5, 10)
print("Longueur du rectangle :", rect.get_longueur())
print("Largeur du rectangle :", rect.get_largeur())
print("Périmètre du rectangle :", rect.perimetre())
print("Surface du rectangle :", rect.surface())

# Instanciation de la classe Parallelepipede
para = Parallelepipede(5, 10, 15)
print("Longueur du parallélépipède :", para.get_longueur())
print("Largeur du parallélépipède :", para.get_largeur())
print("Hauteur du parallélépipède :", para.get_hauteur())
print("Périmètre du parallélépipède :", para.perimetre())
print("Surface du parallélépipède :", para.surface())
print("Volume du parallélépipède :", para.volume())