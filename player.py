# file: player.py
# the method turn() will be run until the end of the dungeon is reached or an
# error is encountered

#if __name__ == '__main__':
def turn(hero):
    # your code here
    if hero.feel('right')==' ':
    	hero.move('right')
    else:
    	hero.attack(hero.feel('right'))

