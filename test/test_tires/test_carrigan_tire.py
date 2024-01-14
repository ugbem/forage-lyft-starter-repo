import unittest

from tire.carrigan_tire import CarriganTires

class TestCarrigan_tires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear =[0.2,0.3,0.4,0.6]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_sercice)
    
    def test_need_service_false(self):
        tire_wear=[0.2,0.4,0.6,0.8]
        tires=CarriganTires(tire_wear)
        self.assertFalse(tires.needs_servicing())