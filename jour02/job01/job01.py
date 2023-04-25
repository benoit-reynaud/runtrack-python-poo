class Personne :
    def __init__(self, age=14):
        self.age=age
        
    def afficheAge(self):
        print("AGe de la personne :", self.age)
        
    def bonjour(self):
        print("Hello")
        
    def modifeAge(self, nouvel_age):
        self.age=nouvel_age
        
class Eleve (Personne):
    def allerEnCours(self):
        print("Je vais en cours")
        
    def afficheAge(self):
        print("J'ai", self.age, "ans")
        
class Professeur (Personne):
    def __init__ (self, matiereEnseignee, age=14):
        super().__init__(age)
        self.matiereEnseignee=matiereEnseignee
        
    def enseigner(self):
        print("Le cours va commencer")
        
#Instanciation d'un objet de la class Personne et d'un Eleve

personne1 = Personne()
eleve1 = Eleve()

#Affichage de l'age par defaut de l'éleve

eleve1.afficheAge()