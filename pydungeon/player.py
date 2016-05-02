# file: player.py
# the method turn() will be run until the end of the dungeon is reached or an
# error is encountered

# the hero is represented by object 'hero'
# hero can perform several actions such as movement, attacking etc.
# actions can be performed by running
#    hero.move('left')
# read the readme for all actions

def turn(hero):
    # your code here
    if hero.feel( hero.optwalk() ) == ' ':
        if hero.rhealth() < 100:
            hero.rest()
        else:
            hero.move(hero.optwalk())
    else:
        hero.attack(hero.feel(hero.optwalk()))
