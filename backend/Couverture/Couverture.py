import math
from Okumura_Hata import Okumura_Hata
from Cost231_Hata import Cost231_Hata

class Couverture:
    """
    Classe représentant la couverture d'un réseau de télécommunications en fonction du modèle de propagation
    utilisé, du type de zone, de la fréquence, de la hauteur des stations et de la distance entre elles.
    """

    def __init__(self, type_modele: str, type_zone: str, freq, hauteurbase, hauteurmobile, distance, city_size):
        """
        Initialise les paramètres nécessaires pour calculer la couverture du réseau.
        
        :param type_modele: Modèle de propagation utilisé ('Okumura-Hata' ou 'Cost231_Hata').
        :param type_zone: Type de zone ('Urbaine' ou 'Suburbain').
        :param freq: Fréquence de transmission en Hz.
        :param hauteurbase: Hauteur de la station de base en mètres.
        :param hauteurmobile: Hauteur de la station mobile en mètres.
        :param distance: Distance entre la station de base et la station mobile en kilomètres.
        :param city_size: Taille de la ville ('petite' ou 'grande') pour le modèle Cost231_Hata.
        """
        self.type_modele = type_modele  # Type de modèle de propagation (Okumura-Hata ou Cost231_Hata)
        self.type_zone = type_zone  # Type de zone (urbaine ou suburbain)
        self.freq = freq  # Fréquence de transmission
        self.hauteurbase = hauteurbase  # Hauteur de la station de base
        self.hauteurmobile = hauteurmobile  # Hauteur de la station mobile
        self.distance = distance  # Distance entre les stations
        self.city_size = city_size  # Taille de la ville (petite ou grande pour Cost231_Hata)

    def path_loss(self):
        """
        Calcule la perte de signal (path loss) en fonction du modèle de propagation et du type de zone.
        
        :return: La perte de signal (path loss) en dB.
        """
        path_loss = None  # Valeur par défaut si aucun modèle ne correspond

        # Cas du modèle Okumura-Hata
        if self.type_modele == 'Okumura-Hata':
            OkumuraHata = Okumura_Hata(self.freq, self.hauteurbase, self.hauteurmobile, self.distance)  # Instanciation de la classe Okumura_Hata
            if self.type_zone == 'Urbaine':
                path_loss = OkumuraHata.attenuation_moyenne()  # Appel de la méthode pour l'atténuation en zone urbaine
            elif self.type_zone == "Suburbain":
                path_loss = OkumuraHata.attenuation_moyenne_suburbain()  # Appel de la méthode pour l'atténuation en zone suburbain
            else:
                raise ValueError(f"Zone inconnue : {self.type_zone}")  # Gestion des zones non reconnues
        # Cas du modèle Cost231_Hata
        elif self.type_modele == 'Cost231_Hata':
            Cost231Hata = Cost231_Hata(self.freq, self.distance, self.hauteurbase, self.hauteurmobile, self.city_size)  # Instanciation de la classe Cost231_Hata
            path_loss = Cost231Hata.calculate_path_loss()  # Calcul de la perte de signal avec Cost231_Hata
        else:
            raise ValueError(f"Modèle inconnu : {self.type_modele}")  # Gestion des modèles non reconnus
        
        return path_loss  # Retourne la perte de signal calculée
    
    def Rayon(self):
        """
        Calcule le rayon de couverture en fonction de la perte de signal.
        
        :return: Le rayon de couverture en kilomètres.
        """
        path_loss = self.path_loss()  # Récupère la perte de signal calculée précédemment
        rayon = math.exp((path_loss - 137) / 35.2)  # Utilisation de la formule pour calculer le rayon de couverture
        return rayon  # Retourne le rayon calculé
    
    def Couverture(self):
        """
        Calcule la surface de couverture en fonction du rayon.
        
        :return: La surface de couverture en kilomètres carrés.
        """
        rayon = self.Rayon()  # Récupère le rayon de couverture calculé précédemment
        couverture = rayon**2 * math.pi  # Calcul de la surface de couverture en km² (forme circulaire)
        return couverture  # Retourne la surface de couverture calculée
