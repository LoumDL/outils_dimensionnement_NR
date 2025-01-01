import math
from Okumura_Hata import Okumura_Hata
from Cost231_Hata import Cost231_Hata

class Couverture:
    
    def __init__(self, type_modele: str, type_zone: str,freq, hauteurbase, hauteurmobile, distance, city_size):
        self.type_modele = type_modele
        self.type_zone = type_zone
        self.freq = freq
        self.hauteurbase = hauteurbase
        self.hauteurmobile = hauteurmobile
        self.distance = distance
        self.city_size = city_size


    def path_loss(self):
        path_loss = None  # Valeur par défaut si aucun modèle ne correspond

        if self.type_modele == 'Okumura-Hata':

            OkumuraHata = Okumura_Hata(self.freq, self.hauteurbase, self.hauteurmobile, self.distance)
            if self.type_zone == 'Urbaine':
                path_loss = OkumuraHata.attenuation_moyenne()  # Assurez-vous que cette méthode est statique ou instanciée
            elif self.type_zone == "Suburbain":
                path_loss = OkumuraHata.attenuation_moyenne_suburbain()  # Idem
            else:
                raise ValueError(f"Zone inconnue : {self.type_zone}")
        elif self.type_modele == 'Cost231_Hata':

            Cost231Hata = Cost231_Hata(self.freq, self.distance, self.hauteurbase, self.hauteurmobile, self.city_size)
            path_loss = Cost231Hata.calculate_path_loss()  # Assurez-vous que cette méthode est statique ou instanciée
        else:
            raise ValueError(f"Modèle inconnu : {self.type_modele}")
        
        return path_loss
    
    def Rayon(self):
        # Calcule le rayon basé sur la perte de chemin
        path_loss = self.path_loss()
        rayon = math.exp((path_loss - 137) / 35.2)  # Formule donnée
        return rayon
    
    def Couverture(self):
        # Calcule la couverture en fonction du rayon
        rayon = self.Rayon()
        couverture = rayon**2 * math.pi
        return couverture
