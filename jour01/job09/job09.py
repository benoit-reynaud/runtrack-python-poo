class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__nb_credits = 0  # Attribut "nombre de crédits" initialisé à zéro par défaut
        self.__level = self.__studentEval()  # Attribut "level" initialisé avec la méthode "studentEval"

    # Méthode privée pour évaluer le niveau de l'étudiant en fonction du nombre de crédits
    def __studentEval(self):
        if self.__nb_credits >= 90:
            return "Excellent"
        elif self.__nb_credits >= 80:
            return "Très bien"
        elif self.__nb_credits >= 70:
            return "Bien"
        elif self.__nb_credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # Assesseurs et mutateurs pour nom, prénom, numéro d'étudiant, nombre de crédits (comme dans les exemples précédents)
    ...

    # Méthode pour ajouter des crédits au total de l'étudiant (comme dans les exemples précédents)
    ...

    # Méthode pour afficher les informations de l'étudiant en console
    def studentInfo(self):
        print("Nom :", self.__nom)
        print("Prénom :", self.__prenom)
        print("Identifiant :", self.__num_etudiant)
        print("Niveau :", self.__level)

# Utilisation de la classe Student

# Instanciation d'un objet représentant l'étudiant John Doe avec le numéro d'étudiant 145
john_doe = Student("John", "Doe", 145)

# Ajout de crédits à trois reprises
john_doe.add_credits(10)  # Ajoute 10 crédits
john_doe.add_credits(5)   # Ajoute 5 crédits
john_doe.add_credits(8)   # Ajoute 8 crédits

# Appel de la méthode studentInfo pour afficher les informations de John Doe
john_doe.studentInfo()
# Affiche :
# Nom : John
# Prénom : Doe
# Identifiant : 145
# Niveau : Passable
