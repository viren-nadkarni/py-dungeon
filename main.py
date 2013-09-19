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
import os
import pickle

from units import hero as hr
from levels import levels

def main():
    profiles = os.listdir('./profiles/')
##
##    if len(profiles) != 0:
##        print 'Saved sessions found:'
##        print '[0] New session'
##        for x in range(0, len(profiles) ):
##            print '[' + str(x + 1) + '] ' + profiles[x].name
##
##        opt = input('')
##
##        if opt > 0:
##            pickle.load( open('./profiles/' + profiles[opt].name, 'wb') )
##        else:
##            #init hero
##            hero = hr.Hero()

    #check for loops in player.py
    f = open('player.py', 'r')
    content = f.read()

    if content.find('while') != -1 or content.find('for') != -1:
        print 'Loops are not allowed in player.py'
        sys.exit()

    #load the map
    l = levels.level()
    l.level1()
    currentMonsterMap = l.map

    hero = hr.Hero(l)

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

    # eval loop
    while True:
        for m in monsters:
            h = m.monsterFeel(l)
            if len(h) != 0:
                if not m.attack(hero):
                    print 'Hero is dead'
                    sys.exit()

        player.turn(hero)
        # update map
        l.display()
        hero.rope()






    #pickle.dump( hero, open('./profiles/' + profiles[opt].name, 'wb') )



if __name__ == '__main__':
    main()

