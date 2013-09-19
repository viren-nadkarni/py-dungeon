#-------------------------------------------------------------------------------
# Name:        /units/varkey.py
# Purpose:
#
# Author:      viren
#
# Created:     19/09/2013
# Copyright:   (c) viren 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import base_unit

class Varkey(base_unit.BaseUnit):
    def __init__(self):
        self.health = max_health = 60
        self.attack_power = 15
    def __str__(self):
    	return 'v'

    def rhealth(self):
        return self.health
    
    
    