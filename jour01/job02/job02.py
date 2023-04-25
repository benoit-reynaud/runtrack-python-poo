class Operation :
    
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
operation1 = Operation(12, 3)        
print("La valeur de nombre1 : ", operation1.nombre1)
print("La valeur de nombre2 : ", operation1.nombre2)