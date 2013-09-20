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
        if not m.attack(hero):
                   print 'Hero dies :('

    def attack(self, unit):
        print str(unit),' is damaged by ',str(self.attack_power)
        return unit.take_damage(self.attack_power)

    def findPosition(self,lvl):
        x=0
        y=0
        z=0
        v=str(self)
        for i in lvl.map:
            z=0
            for j in xrange(0,len(lvl.map[0])):
                if str(lvl.map[x][j])==str(self):
                    y=j
                    z=1
                    break
            if z==0:
                x+=1
        return [x,y]

    def monsterFeel(self,lvl,unit='H'):
            position = self.findPosition(lvl)
            if position[1]!=0:
                if lvl.map[position[0]][position[1]-1] == 'H':
                    return [ position[0], position[1]-1 ]
            if position[1]!=(len(lvl.map[0])-1):
                if lvl.map[position[0]][position[1]+1] == 'H':
                    return [ position[0],position[1]-1 ]
            if len(lvl.map)!=1:
                if position[0]!=0:
                    if lvl.map[position[0]-1][position[1]] == 'H':
                        return [position[0],position[1]-1]
                if position[0]!=(len(lvl.map[0])-1):
                    if lvl.map[position[0]+1][position[1]] == 'H':
                        return [position[0],position[1]-1]
            return True

