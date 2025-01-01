import math

class Okumura_Hata:
    """
    Classe représentant le modèle de propagation Okumura-Hata, utilisé pour calculer la perte de signal
    (atténuation) dans différents environnements tels que les zones urbaines et suburbaines.
    """

    def __init__(self, freq, hauteurbase, hauteurmobile, distance):
        """
        Initialisation de la classe Okumura_Hata avec les paramètres nécessaires pour effectuer les calculs.
        
        :param freq: Fréquence de la transmission en Hz.
        :param hauteurbase: Hauteur de la station de base en mètres.
        :param hauteurmobile: Hauteur de la station mobile en mètres.
        :param distance: Distance entre la station de base et la station mobile en kilomètres.
        """
        self.freq = freq  # Fréquence de transmission en Hz
        self.hauteurbase = hauteurbase  # Hauteur de la station de base en mètres
        self.hauteurmobile = hauteurmobile  # Hauteur de la station mobile en mètres
        self.distance = distance  # Distance entre les stations en kilomètres

    def calcul_facteur_correction(self):
        """
        Calcule le facteur de correction en fonction de la taille de la ville et de la hauteur de la station mobile.
        
        :return: Le facteur de correction pour la perte de signal.
        """
        taille_ville = str(input("Petite ou grande ville ? (petite/grande) : ")).lower()

        if taille_ville == "petite":
            # Pour les villes de taille moyenne ou petite
            if 1 <= self.hauteurmobile <= 10:  # Vérifie que la hauteur du mobile est dans la plage valide
                facteur_correction = (1.1 * math.log10(self.freq) - 0.7) * self.hauteurmobile - (1.56 * math.log10(self.freq) - 0.8)
                return facteur_correction
            else:
                raise ValueError("Erreur : la hauteur du mobile doit être comprise entre 1 et 10 mètres.")
        elif taille_ville == "grande":
            if self.freq <= 200_000_000:  # Fréquence <= 200 MHz pour une grande ville
                facteur_correction = 8.29 * math.log10(1.54 * self.hauteurmobile) - 1.1
            else:  # Fréquence > 200 MHz pour une grande ville
                facteur_correction = 3.2 * math.log10(11.75 * self.hauteurmobile) - 4.97
            return facteur_correction
        else:
            # Gestion d'une entrée invalide pour la taille de la ville
            raise ValueError("Erreur : la taille de la ville doit être 'petite' ou 'grande'.")

    def attenuation_moyenne(self):
        """
        Calcule l'atténuation moyenne en utilisant le modèle Okumura-Hata pour un environnement urbain.
        
        :return: L'atténuation moyenne (perte de signal) en dB.
        """
        facteur_correction = self.calcul_facteur_correction()  # Calcul du facteur de correction

        # Vérifie que les paramètres sont dans les limites définies pour une bonne estimation
        if 150_000_000 < self.freq <= 1_500_000_000:  # Fréquence entre 150 MHz et 1.5 GHz
            if 30 < self.hauteurbase <= 300:  # Hauteur de la station de base entre 30 m et 300 m
                if 1_000 <= self.distance <= 20_000:  # Distance entre 1 km et 20 km
                    # Calcul de l'atténuation en utilisant les différentes parties de la formule Okumura-Hata
                    L1 = 69.55 + 26.16 * math.log10(self.freq)  # Partie de la formule Okumura-Hata
                    L2 = 13.82 * math.log10(self.hauteurbase) - facteur_correction  # Partie de la formule
                    L3 = (44.9 - 6.55 * math.log10(self.hauteurbase)) * math.log10(self.distance)  # Partie de la formule
                    attenuation_environnement = L1 - L2 + L3  # Atténuation totale calculée
                    return attenuation_environnement
                else:
                    raise ValueError("Erreur : la distance doit être comprise entre 1 km et 20 km.")
            else:
                raise ValueError("Erreur : la hauteur de l'antenne de base doit être comprise entre 30 m et 300 m.")
        else:
            raise ValueError("Erreur : la fréquence doit être comprise entre 150 MHz et 1.5 GHz.")

    def attenuation_moyenne_suburbain(self):
        """
        Calcule l'atténuation moyenne pour un environnement suburbain en ajustant l'atténuation 
        obtenue dans un environnement urbain avec une formule spécifique.
        
        :return: L'atténuation moyenne dans un environnement suburbain en dB.
        """
        attenuation_moyenne = self.attenuation_moyenne()  # Calcul de l'atténuation en environnement urbain
        div = self.freq / 28  # Diviseur basé sur la fréquence
        # Ajustement de l'atténuation pour un environnement suburbain
        attenuation_moyenne_sub = attenuation_moyenne - 2 * (math.log10(div))**2 - 5.4
        return attenuation_moyenne_sub
