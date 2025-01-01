import math
from Okumura_Hata import Okumura_Hata
from Cost231_Hata import Cost231_Hata

class Couverture:
    
    def __init__(self, type_modele, type_zone):
        self.type_modele = type_modele
        self.type_zone = type_zone

    def path_loss(self):
        path_loss = None  # Valeur par défaut si aucun modèle ne correspond

        if self.type_modele == 'Okumura-Hata':
            if self.type_zone == 'Urbaine':
                path_loss = Okumura_Hata.attenuation_moyenne()
            elif self.type_zone == "suburbain":
                path_loss = Okumura_Hata.attenuation_moyenne_suburbain()
            else:
                raise ValueError(f"Zone inconnue : {self.type_zone}")
        elif self.type_modele == 'Cost231_Hata':
            path_loss = Cost231_Hata.calculate_path_loss()
        else:
            raise ValueError(f"Modèle inconnu : {self.type_modele}")
        
        return path_loss
    
    def Rayon(self):

        path_loss = self.path_loss()
        rayon = math.exp((path_loss - 137) / 35.2)
        return rayon
    
    def Couverture():
        
        return self.Rayon()**2 * math.pi
