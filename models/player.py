"""
Classe joueur: nom, prénom, date de naissance, idne
"""
class Player:

    def __init__(self, atts):
        self.firstName = atts['firstName']
        self.lastName = atts['lastName']
        self.birthDate = atts['birthDate']
        self.idne = atts['idne']

    def json_serialize(self):
        self.atts = {
            'firstName' : self.firstName,
            'lastName' : self.lastName,
            'birthDate' : self.birthDate,
            'idne' : self.idne,
        }

    def __str__(self):
        result = f"Nom du joueur : {self.lastName}\n"
        result += f"Prenom : {self.firstName}\n"
        result += f"Date de naissance : {self.birthDate}\n"
        result += f"Identifiant national : {self.idne}\n"

        return result
    
    def __repr__(self):
        return str(self)