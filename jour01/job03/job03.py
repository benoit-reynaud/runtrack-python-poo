
#création de la classe
class Operation :
    
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
#Ajout à l'Opération l'addition
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        return resultat
        
addition = Operation(12, 3) 
resultat = addition.addition()       
print("Resultat de l'addition : ", resultat)
        