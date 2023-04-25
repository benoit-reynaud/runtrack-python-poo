# Création de la classe "Operation"
class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        return resultat

# Instanciation de la classe "Operation"
addition = Operation(12, 3)

# Appel de la méthode "addition" pour effectuer l'addition
resultat = addition.addition()

# Affichage du résultat
print("Résultat de l'addition :", resultat)