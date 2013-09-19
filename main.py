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

import sys

from units import hero as hr
from levels import levels

def main():

    #check for loops in player.py
    f = open('player.py', 'r')
    content = f.read()

    if content.find('while') != -1 or content.find('for') != -1:
        print 'Loops found in the source'
        sys.exit()

    #load hero
    hero = hr.Hero()

    #load the map
    l = levels.level()
    l.level1()
    print hero.position(l)
    hero.walk("right",l)
    print hero.position(l)
    currentMonsterMap = l.map

    #load the monsters
    monsters =[]
    for a in currentMonsterMap:
        for b in range(0, len(a)):
            if a == 'v':
                currentMonsterMap[a][b] = units.Varke()
                monsters.append(currentMonsterMap[a][b])
            if a == 'V':
                currentMonsterMap[a][b] = units.VarkeBadass()
                monsters.append(currentMonsterMap[a][b])
            if a == 'm':
                currentMonsterMap[a][b] = units.Maru()
                monsters.append(currentMonsterMap[a][b])

    # read player.py
    import player




if __name__ == '__main__':
    main()
