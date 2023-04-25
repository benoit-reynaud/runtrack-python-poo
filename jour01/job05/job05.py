class Animal:
    def __init__(self, prenom=''):
        self.age = 0
        self.prenom = prenom
    
    def vieillir(self):
        self.age += 1
        
# Instanciation d'un objet Animal
animal1 = Animal()

# Affichage de l'âge initial de l'animal
print("Âge initial de l'animal : ", animal1.age)

# Appel de la méthode vieillir() pour faire vieillir l'animal
animal1.vieillir()

# Affichage de l'âge de l'animal après avoir vieilli
print("Âge de l'animal après avoir vieilli : ", animal1.age)






class Animal:
    def __init__(self, prenom=''):
        self.age = 0
        self.prenom = prenom
    
    def vieillir(self):
        self.age += 1
        
    def nommer(self, nom):
        self.prenom = nom
        
# Instanciation d'un objet Animal
animal1 = Animal()

# Affichage du prénom initial de l'animal
print("Prénom initial de l'animal : ", animal1.prenom)

# Appel de la méthode nommer() pour attribuer un nom à l'animal
animal1.nommer("Félix")

# Affichage du nom de l'animal après l'avoir nommé
print("Nom de l'animal : ", animal1.prenom)