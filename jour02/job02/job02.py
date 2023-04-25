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
 
#Instanciation d'un objet de la classe Personne
personne1=Personne()

#Instanciation d'un objet de la classe Eleve
eleve1=Eleve()

#Appel de la méthode bonjonr pour l'éleve
eleve1.bonjour() #Affiche : Hello

#Appel de la méthode allerEnCours pour l'éleve
eleve1.allerEnCours() #Affiche : Je vais en cours

#Redéfinition de l'age de l'élève à 15ans
eleve1.modifeAge(15)

#Instanciation d'un objet Professeur avec 40 ans et la matière enseignée
professeur1=Professeur("Mathématique", 40)

#Appel de la méthode bonjour pour le professeur
professeur1.bonjour()

#Appel de la méthode enseigner pour le professeur
professeur1.enseigner() #Affiche : Le cours va commencer


