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
        
    def attack(self, unit):
        return unit.take_damage(self.attack_power)
        
    def findPosition(self,lvl):
        x=0
        y=0
        for i in lvl.map:
            if 'H' in i:
                y=i.index('H')
                break
            else:
                x+=1
        return [x,y]    
    
    def monsterFeel(self,lvl):
        position = self.findPosition(self,lvl)
        try:
            if lvl.map[position[0],position[1]-1] == 'H':
                return [ position[0], position[1]-1 ]
            if lvl.map[position[0],position[1]+1] == 'H':
                return [ position[0],position[1]-1 ]
            if lvl.map[position[0]-1,position[1]] == 'H':
                return [position[0],position[1]-1]
            if lvl.map[position[0]+1,position[1]] == 'H':
                return [position[0],position[1]-1]
            
        except :
            return False
