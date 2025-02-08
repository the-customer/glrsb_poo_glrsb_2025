

class Montre:
    # Attributs de classe
    marque = "Rolex"
    prix = 1000
    style="Equille"
    bracelet = "Cuir"


# Creeation d'une instance de la classe Montre:
montre_01 = Montre()
print(montre_01)
montre_01.marque = "TAG HEUER"
montre_01.prix = 2000
Montre.marque = "TAG HEUER"
print(montre_01.marque)

montre_02 = Montre()
print(montre_02)
print(montre_02.marque)
