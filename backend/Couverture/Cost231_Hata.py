import math

class Cost231Hata:
    def __init__(self, frequency, distance, base_station_height, mobile_station_height, city_size='small'):
        self.frequency = frequency
        self.distance = distance
        self.base_station_height = base_station_height
        self.mobile_station_height = mobile_station_height
        self.city_size = city_size

    def calculate_path_loss(self):
        if self.city_size == 'large':
            if self.frequency > 200:
                a_hm = 3.2 * (math.log10(11.75 * self.mobile_station_height) ** 2) - 4.97
            else:
                a_hm = 8.29 * (math.log10(1.54 * self.mobile_station_height) ** 2) - 1.1
        else:
            a_hm = (1.1 * math.log10(self.frequency) - 0.7) * self.mobile_station_height - (1.56 * math.log10(self.frequency) - 0.8)

        path_loss = (46.3 + 33.9 * math.log10(self.frequency) - 13.82 * math.log10(self.base_station_height) 
                     - a_hm + (44.9 - 6.55 * math.log10(self.base_station_height)) * math.log10(self.distance) + 3)

        return path_loss