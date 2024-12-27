import math

class Okumura_Hata:

    def __init__(self, freq, hauteurbase, hauteurmobile, distance):
        self.freq = freq
        self.hauteurbase = hauteurbase
        self.hauteurmobile = hauteurmobile
        self.distance = distance

    # Modèle d’Okumura-Hata en environnement urbain
    def calcul_facteur_correction(self):
        taille_ville = str(input("Petite ou grande ville ? (petite/grande) : ")).lower()

        if taille_ville == "petite":
            # Pour les villes de taille moyenne ou petite
            if 1 <= self.hauteurmobile <= 10:
                facteur_correction = (1.1 * math.log10(self.freq) - 0.7) * self.hauteurmobile - (1.56 * math.log10(self.freq) - 0.8)
                return facteur_correction
            else:
                raise ValueError("Erreur : la hauteur du mobile doit être comprise entre 1 et 10 mètres.")
        elif taille_ville == "grande":
            if self.freq <= 200_000_000:  # Fréquence <= 200 MHz
                facteur_correction = 8.29 * math.log10(1.54 * self.hauteurmobile) - 1.1
            else:  # Fréquence > 200 MHz
                facteur_correction = 3.2 * math.log10(11.75 * self.hauteurmobile) - 4.97
            return facteur_correction
        else:
            raise ValueError("Erreur : la taille de la ville doit être 'petite' ou 'grande'.")

    def attenuation_moyenne(self):
        facteur_correction = self.calcul_facteur_correction()

        if 150_000_000 < self.freq <= 1_500_000_000:  # Vérifie que la fréquence est entre 150 MHz et 1.5 GHz
            if 30 < self.hauteurbase <= 300:  # Vérifie la hauteur de l'antenne de base
                if 1_000 <= self.distance <= 20_000:  # Vérifie la distance entre 1 km et 20 km
                    L1 = 69.55 + 26.16 * math.log10(self.freq)
                    L2 = 13.82 * math.log10(self.hauteurbase) - facteur_correction
                    L3 = (44.9 - 6.55 * math.log10(self.hauteurbase)) * math.log10(self.distance)
                    attenuation_environnement = L1 - L2 + L3
                    return attenuation_environnement
                else:
                    raise ValueError("Erreur : la distance doit être comprise entre 1 km et 20 km.")
            else:
                raise ValueError("Erreur : la hauteur de l'antenne de base doit être comprise entre 30 m et 300 m.")
        else:
            raise ValueError("Erreur : la fréquence doit être comprise entre 150 MHz et 1.5 GHz.")
