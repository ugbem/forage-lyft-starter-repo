from tire.tires import Tire

class CarriganTires(Tire):
    def __init__(self,tire_wear):
        self.tire_wear=tire_wear

    def needs_sercice(self):
        for tire in self.tire_wear:
            if tire >= 0.9:
                return True
        return False
