# file: player.py
# the method turn() will be run until the end of the dungeon is reached or an
# error is encountered

# the hero is represented by object 'hero'
# hero can perform several actions such as movement, attacking etc.
# actions can be performed by saying
#    hero.move('left')
# other possible actions are:
#    hero.rest()              -> restores 10% of the health
#    hero.feel(direction)     -> returns what is there in 'direction'
#    hero.move(direction)     -> move in 'direction'
#        direction can be 'left', 'right', 'up', 'down'
#    hero.optmove()           -> returns the direction the hero should move to 
#                                reach the rope
# note that loops are not allowed

def turn(hero):
    # your code here
    if hero.feel( hero.optwalk() ) == ' ':
    	if hero.rhealth() < 100:
    		hero.rest()
    	else:
    		hero.move(hero.optwalk())
    else:
    	hero.attack(hero.feel(hero.optwalk()))


## LEVEL 4
## After ages of captivity, Hero thanks you for your help in bringing him this
## far.
## But now, because the developers of this game want to show off, Hero must
## face the horrors of TWO DIMENSIONS!


## LEVEL 5
## What's this? The spiders have taken their time to regenerate and become
## stronger! Can Hero brave through NOT ONE but TWO Big Varkid Spiders?!

## LEVEL 2
## That almost seemed too easy..
## OH NO! It was a set up. Hero is now faced with the varkid spider! Is this the
## end?

## LEVEL 3
## Too close. Thank goodness Hero Bhai had your help.
## GOOD LORD! The varkid spider has brought along her sinister friend, Mr. Monster!
## Can out brave hero fend against them BOTH?

## LEVEL 4
## After ages of captivity, Hero thanks you for your help in bringing him this
## far.
## But now, because the developers of this game want to show off, Hero must
## face the horrors of TWO DIMENSIONS!
