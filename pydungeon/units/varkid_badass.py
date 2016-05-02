import base_unit

class varkidBadass(base_unit.BaseUnit):
    def __init__(self):
        self.health = max_health = 120
        self.attack_power = 15
    
    def __str__(self):
    	return 'V'

    def rhealth(self):
        return self.health
