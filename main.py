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
from units import varkey,varkey_badass,maru
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
    l.level5()
    currentMonsterMap = l.map

    hero = hr.Hero(l)

    #load the monsters
    monsters =[]
    i=0
    for a in currentMonsterMap:
        for b in range(0, len(a)):
            if a[b] == 'v':
                currentMonsterMap[i][b] = varkey.Varkey()
                monsters.append(currentMonsterMap[i][b])
            if a[b] == 'V':
                currentMonsterMap[i][b] = varkey_badass.VarkeyBadass()
                monsters.append(currentMonsterMap[i][b])
            if a[b] == 'm':
                currentMonsterMap[i][b] = maru.Maru()
                monsters.append(currentMonsterMap[i][b])
        i+=1
    # read player.py
    import player
    # eval loop
    while True:
        for m in monsters:
           h = m.monsterFeel(l)
           print m.findPosition(l)
           if h==False or h==True:
                pass
           else:
                if not m.attack(hero):
                   print 'Hero is dead'
                   sys.exit()
                if m.rhealth()<=0:
                    print str(m),' died'
                    position = m.findPosition(l)
                    currentMonsterMap[position[0]][position[1]]=' '
                    monsters.remove(m)
                    break
        print hero.rhealth()
        player.turn(hero)
        # update map
        l.display()
        print "\n\n"
    






    #pickle.dump( hero, open('./profiles/' + profiles[opt].name, 'wb') )



if __name__ == '__main__':
    main()

