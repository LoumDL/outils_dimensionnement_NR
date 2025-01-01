import math
from Cost231_Hata import Cost231_Hata
from Okumura_Hata import Okumura_Hata
from Couverture import Couverture


class CalculPuissance:
    def __init__(self, freq, hauteurbase, hauteurmobile, distance, city_size, Pe, losscoupleur, lossalimentationBTS, Gmobile, GBTS, lossalimentationMobile, GdBTS):
        self.Pe = Pe  # Puissance émise
        self.freq = freq  # Fréquence
        self.hauteurbase = hauteurbase  # Hauteur de la station de base
        self.hauteurmobile = hauteurmobile  # Hauteur du mobile
        self.distance = distance  # Distance
        self.city_size = city_size  # Taille de la ville (small/large)
        self.losscoupleur = losscoupleur  # Pertes du coupleur
        self.lossalimentationBTS = lossalimentationBTS  # Pertes d'alimentation BTS
        self.Gmobile = Gmobile  # Gain du mobile
        self.GBTS = GBTS  # Gain de la station de base
        self.lossalimentationMobile = lossalimentationMobile  # Pertes d'alimentation mobile
        self.GdBTS = GdBTS  # Gain directionnel BTS

    def PuissanceRecuMobile_Okumura(self):
        """Calcul de la puissance reçue au mobile en utilisant le modèle Okumura-Hata."""
        ok_model = Okumura_Hata(self.freq, self.hauteurbase, self.hauteurmobile, self.distance)
        path_loss = ok_model.attenuation_moyenne()
        path_loss += self.losscoupleur + self.lossalimentationBTS + self.lossalimentationMobile
        Pr = self.Pe + self.GBTS + self.Gmobile - path_loss
        return Pr

    def PuissanceRecuMobile_Cost231Hata(self):
        """Calcul de la puissance reçue au mobile en utilisant le modèle Cost231-Hata."""
        cost_model = Cost231_Hata(self.freq, self.distance, self.hauteurbase, self.hauteurmobile, self.city_size)
        path_loss = cost_model.calculate_path_loss()
        path_loss += self.losscoupleur + self.lossalimentationBTS + self.lossalimentationMobile
        Pr = self.Pe + self.GBTS + self.Gmobile - path_loss
        return Pr

    def PuissanceRecuBTS_Okumura(self):
        """Calcul de la puissance reçue par la BTS en utilisant le modèle Okumura-Hata."""
        ok_model = Okumura_Hata(self.freq, self.hauteurbase, self.hauteurmobile, self.distance)
        path_loss = ok_model.attenuation_moyenne()
        path_loss += self.lossalimentationMobile + self.lossalimentationBTS
        Pr = self.Pe + self.GBTS + self.GdBTS - path_loss
        return Pr

    def PuissanceRecuBTS_Cost231Hata(self):
        """Calcul de la puissance reçue par la BTS en utilisant le modèle Cost231-Hata."""
        cost_model = Cost231_Hata(self.freq, self.distance, self.hauteurbase, self.hauteurmobile, self.city_size)
        path_loss = cost_model.calculate_path_loss()
        path_loss += self.lossalimentationMobile + self.lossalimentationBTS
        Pr = self.Pe + self.GBTS + self.GdBTS - path_loss
        return Pr

    def PIRE(self):
        """Calcul de la puissance isotrope rayonnée équivalente (PIRE)."""
        pire = self.Pe - self.losscoupleur - self.lossalimentationBTS + self.GBTS
        return pire
