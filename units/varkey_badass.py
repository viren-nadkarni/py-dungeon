#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      viren
#
# Created:     19/09/2013
# Copyright:   (c) viren 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import base_unit


class VarkeyBadass(base_unit.BaseUnit):
    def __init__(self):
        self.health = max_health = 120
        self.attack_power = 15
    def __str__(self):
    	return 'V'

    def rhealth(self):
        return self.health
    
    
    