# file: player.py
# the method turn() will be run until the end of the dungeon is reached or an
# error is encountered

#if __name__ == '__main__':
def turn(hero):
    # your code here
    print hero.optwalk()
    if hero.feel(hero.optwalk())==' ':
    	if hero.rhealth()<100:
    		hero.rest()
    	else:
    		hero.move(hero.optwalk())
    else:
    	hero.attack(hero.feel(hero.optwalk()))

