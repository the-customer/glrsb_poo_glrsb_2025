# - attribut d'objet
# - constructeur

class Montre:
    # Attributs de classe
    nbre_montre = 0
    def __init__(self, marque, prix, style, bracelet):
        # print("Creation d'un objet")
        # Attributs d'objet:
        self.marque = marque
        self.prix = prix
        self.style = style
        self.bracelet = bracelet
        self.couleur = "Noir"
        Montre.nbre_montre += 1



# Creeation d'une instance de la classe Montre:
montre_01 = Montre("Rolex",1500,"Electronique","Metal")
montre_01.prix = 20000
montre_01.couleur = "Rouge"
montre_02 = Montre("Rolex",1500,"Electronique","Metal")
montre_04 = Montre("Rolex",1500,"Electronique","Metal")
montre_03 = Montre("Rolex",1500,"Electronique","Metal")
montre_05 = Montre("Rolex",1500,"Electronique","Metal")


print(Montre.nbre_montre)
