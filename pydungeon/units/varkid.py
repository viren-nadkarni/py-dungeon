import base_unit

class varkid(base_unit.BaseUnit):
    def __init__(self):
        self.health = max_health = 60
        self.attack_power = 15
        
    def __str__(self):
    	return 'v'

    def rhealth(self):
        return self.health
