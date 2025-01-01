import math

class Free_space_attenuation:

    def __init__(self,distance, frequency):
        self.distance = distance
        self.frequency = frequency
    
    def free_path_loss(self):
        lamda = 300000000/self.frequency

        return 20*math.log10(4*math.pi*self.distance/lamda)
        