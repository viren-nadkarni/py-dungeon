import sys
import os
import time

from units import varkid, varkid_badass, maru
from units import hero as hr
from levels import levels

opt = 0
profiles = []
hero = None

def main():
    print '''
        H -> Hero
        v -> Small varkid spider
        V -> Big varkid spider
        m -> Monster!
        R -> Rope (end of the level)

        '''

    #load the map
    l = levels.level()
    print 'TURN 1'

    #check for loops in player.py
    f = open('player.py', 'r')
    content = f.read()
##
##    if content.find('while') != -1 or content.find('for') != -1:
##        print 'The player can have only one move per turn of player.py\nLoops are not allowed'
##        sys.exit()

    #check if hero already created
    try:
        hero
    except:
        #if not, then create it
##        print 'What is the name of the brave warrior?'
##        playerName = str( raw_input('') )
        playerName = 'Hero Name'
        hero = hr.Hero(l, playerName)

    #select the level
    levelToLoad = int((open('savefile', 'r')).read())
    hero.currentLevel = levelToLoad

    if levelToLoad > 5:
        print 'The hero has escaped the dungeon!'
        print 'ALL LEVELS COMPLETE'
        sys.exit()
    if levelToLoad == 1:
        l.level1()
    elif levelToLoad == 2:
        l.level2()
    elif levelToLoad == 3:
        l.level3()
    elif levelToLoad == 4:
        l.level4()
    elif levelToLoad == 5:
        l.level5()
    currentMonsterMap = l.map

    #load the monsters
    monsters =[]
    i = 0
    for a in currentMonsterMap:
        for b in range(0, len(a)):
            if a[b] == 'v':
                currentMonsterMap[i][b] = varkid.varkid()
                monsters.append(currentMonsterMap[i][b])
            if a[b] == 'V':
                currentMonsterMap[i][b] = varkid_badass.varkidBadass()
                monsters.append(currentMonsterMap[i][b])
            if a[b] == 'm':
                currentMonsterMap[i][b] = maru.Maru()
                monsters.append(currentMonsterMap[i][b])
        i+=1

    # read player.py
    import player


    print '=' * 80
    # eval loop
    counter = 2
    while True:
        print 'TURN ' + str(counter)
        counter += 1

        for m in monsters:
           h = m.monsterFeel(l)
           if h == False or h == True:
                pass
           else:
                if not m.attack(hero):
                    print 'Hero is dead'
                    sys.exit()
                if m.rhealth() <= 0:
                    print str(m),' died'
                    position = m.findPosition(l)
                    currentMonsterMap[position[0]][position[1]] = ' '
                    monsters.remove(m)
                    break
        print "HEALTH:", hero.rhealth()
        player.turn(hero)

        # update map
        l.display()
        print ''
        print '=' * 80
        time.sleep(1)

if __name__ == '__main__':
    main()

