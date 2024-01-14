from tire.tires import Tire

class OctpprimeTires(Tire):
    def __init__(self,tire_wear):
        self.tire_wear=tire_wear
    
    def needs_sercice(self):
        return sum(self.tire_wear) >= 3.0