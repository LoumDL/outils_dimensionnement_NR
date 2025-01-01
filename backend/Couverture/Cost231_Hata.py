import math

class Cost231_Hata:
    """
    Classe représentant le modèle de perte de propagation Cost231-Hata utilisé pour calculer la perte de signal
    en fonction des paramètres tels que la fréquence, la distance et les hauteurs des stations de base et mobiles.
    """
    
    def __init__(self, frequency, distance, base_station_height, mobile_station_height, city_size='small'):
        """
        Initialisation de la classe Cost231_Hata avec les paramètres nécessaires.
        
        :param frequency: Fréquence de la transmission en MHz.
        :param distance: Distance entre la station de base et la station mobile en kilomètres.
        :param base_station_height: Hauteur de la station de base en mètres.
        :param mobile_station_height: Hauteur de la station mobile en mètres.
        :param city_size: Taille de la ville, peut être 'small' ou 'large' (par défaut 'small').
        """
        self.frequency = frequency  # Fréquence de la transmission en MHz
        self.distance = distance  # Distance entre les stations en km
        self.base_station_height = base_station_height  # Hauteur de la station de base en mètres
        self.mobile_station_height = mobile_station_height  # Hauteur de la station mobile en mètres
        self.city_size = city_size  # Taille de la ville (petite ou grande)

    def calculate_path_loss(self):
        """
        Calcule la perte de signal (path loss) en utilisant le modèle Cost231-Hata.
        Ce modèle est basé sur les caractéristiques de la ville (taille), la fréquence, 
        la hauteur des stations et la distance.
        
        :return: La perte de signal (path loss) en dB.
        """
        
        # Calcul de a_hm en fonction de la taille de la ville et de la fréquence
        if self.city_size == 'large':
            if self.frequency > 200:
                # Formule pour une ville de grande taille avec une fréquence > 200 MHz
                a_hm = 3.2 * (math.log10(11.75 * self.mobile_station_height) ** 2) - 4.97
            else:
                # Formule pour une ville de grande taille avec une fréquence <= 200 MHz
                a_hm = 8.29 * (math.log10(1.54 * self.mobile_station_height) ** 2) - 1.1
        else:
            # Formule pour une ville de petite taille
            a_hm = (1.1 * math.log10(self.frequency) - 0.7) * self.mobile_station_height - (1.56 * math.log10(self.frequency) - 0.8)

        # Calcul final de la perte de signal (path loss)
        path_loss = (46.3 + 33.9 * math.log10(self.frequency) - 13.82 * math.log10(self.base_station_height) 
                     - a_hm + (44.9 - 6.55 * math.log10(self.base_station_height)) * math.log10(self.distance) + 3)

        return path_loss  # Retourne la perte de signal en dB
