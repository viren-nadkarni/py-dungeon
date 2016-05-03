# PyDungeon
PyDungeon is a game which makes learning Python and Artificial Intelligence fun.

You play as a hero trapped in a dungeon. The hero must kill all the monsters and reach the rope, which marks the end of the dungeon level. To control the actions of the hero, you must write a python script.

PyDungeon was conceived at the Techyon 2013 hackathon with [@flamesalchemist](http://github.com/sahilc) and [@vanarp96](http://github.com/vanarp96).

### Getting Started
To install PyDungeon,

```
apt install python-pygame
git clone git://github.com/viren-nadkarni/py-dungeon.git
cd py-dungeon
python setup.py install
```

Put your python code in `player.py` before running `main.py`

PyDungeon is somewhat turn-based. The method `turn()` is called and so are those of the monsters present in the level alternatively. 

The hero is represented by object `hero`. It can perform following actions, defined as its member methods:

* `hero.move('left')` Move in the direction specified. Allowed directions are `left`, `right`, `up` and `down`.
* `hero.rest()` Restores 10% of the hero's health
* `hero.feel(direction)` Returns what is there in given direction
* `hero.move(direction)` Move in given direction
* `hero.optmove()` returns the direction the hero should move to reach the rope
* `hero.attack(target)` Attack a target; target should be `H`, `v`, `V`, `m` or `R`

Note that loops are not allowed in `player.py`

An example dungeon

    -----------------------------
    | H |   | v |   | m |   | R | 
    -----------------------------
    
    H - hero (hitpoints = 100, attack = 25)
    v - varkid spider (hitpoints = 60, attack = 15)
    V - badass varkid (hitpoints = 120, attack = 15)
    m - maru monster (hitpoints = 30, attack = 15)
    R - rope; marks the end of level

PyDungeon has an experiment graphical mode. Use `-g` flag to launch it.
