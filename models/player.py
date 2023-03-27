"""
Classe joueur: nom, prénom, date de naissance, idne
"""
class Player:

    def __init__(self, firstName, lastName, birthDate, idne):
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.idne = idne

    def __str__(self):
        result = f"Nom du joueur : {self.lastName}\n"
        result += f"Prenom : {self.firstName}\n"
        result += f"Date de naissance : {self.birthDate}\n"
        result += f"Identifiant national : {self.idne}\n"

        return result
    
    def __repr__(self):
        return str(self)