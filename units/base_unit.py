#-------------------------------------------------------------------------------
# Name:        /units/base.py
# Purpose:
#
# Author:      viren
#
# Created:     19/09/2013
# Copyright:   (c) viren 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class BaseUnit:
    health = int()
    attack_power = int()
    max_health = int()

    def take_damage(self, points):
        # function return bool False if unit dies
        # returns bool True by default

        self.health -= points
        if self.health <= 0:
            return False
        return True
        
    def attack(self,unit):
        unit.take_damage(attack_power)
        return attack_power
