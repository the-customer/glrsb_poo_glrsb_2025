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

    def infos(self):
        print(f"Marque: {self.marque}")
        print(f"Prix: {self.prix}")
        print(f"Style: {self.style}")
        print(f"Bracelet: {self.bracelet}")
        print(f"Couleur: {self.couleur}")


# Creeation d'une instance de la classe Montre:
montre_01 = Montre("Rolex",1500,"Electronique","Metal")
montre_01.prix = 20000
montre_01.couleur = "Rouge"

montre_01.infos()

# Montre.infos(montre_01)