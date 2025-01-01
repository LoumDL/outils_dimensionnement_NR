import math

class Free_space_attenuation:
    """
    Classe représentant l'atténuation dans l'espace libre, basée sur la distance et la fréquence.
    """

    def __init__(self, distance, frequency):
        """
        Initialise les paramètres nécessaires pour calculer l'atténuation dans l'espace libre.
        
        :param distance: Distance entre l'émetteur et le récepteur en mètres.
        :param frequency: Fréquence de transmission en Hz.
        """
        self.distance = distance  # Distance entre l'émetteur et le récepteur
        self.frequency = frequency  # Fréquence de transmission en Hz
    
    def free_path_loss(self):
        """
        Calcule l'atténuation du signal dans l'espace libre en utilisant la formule de la perte de propagation libre.
        
        La formule utilisée est : L = 20*log10(4*pi*d/λ), où :
            - d est la distance entre l'émetteur et le récepteur,
            - λ est la longueur d'onde, qui est égale à c/f, avec c = 300 000 000 m/s (vitesse de la lumière),
            - f est la fréquence en Hz.
        
        :return: L'atténuation du signal (path loss) en décibels (dB).
        """
        # Calcul de la longueur d'onde en mètres (lambda)
        lamda = 300000000 / self.frequency  # Vitesse de la lumière divisée par la fréquence

        # Calcul de l'atténuation du signal dans l'espace libre
        # La formule est L = 20*log10(4*pi*d/λ)
        return 20 * math.log10(4 * math.pi * self.distance / lamda)  # Retourne l'atténuation en dB
