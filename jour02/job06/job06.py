class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Année :", self.annee)
        print("Prix :", self.prix)

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, annee, prix, portes):
        super().__init__(marque, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes :", self.portes)

    def demarrer(self):
        print("La voiture démarre. Vroum Vroum!")


class Moto(Vehicule):
    def __init__(self, marque, annee, prix, roue=2):
        super().__init__(marque, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues :", self.roue)

    def demarrer(self):
        print("La moto démarre. Vroooooom!")


# Instanciation d'un objet Voiture
voiture = Voiture("Mercedes", 2020, 18500, 4)
# Appel de la méthode informationsVehicule pour afficher les informations de la voiture
voiture.informationsVehicule()
# Appel de la méthode demarrer pour démarrer la voiture
voiture.demarrer()

# Instanciation d'un objet Moto
moto = Moto("Yamaha", 1987, 4500)
# Appel de la méthode informationsVehicule pour afficher les informations de la moto
moto.informationsVehicule()
# Appel de la méthode demarrer pour démarrer la moto
moto.demarrer()