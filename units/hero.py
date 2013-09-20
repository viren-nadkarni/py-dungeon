import base_unit
import sys
import pickle

class Hero(base_unit.BaseUnit):
    def __init__(self, lvl, name):
        self.heroName = name
        self.currentLevel = 1

        self.lvl = lvl
        self.max_health = 100
        self.attack_power = 25
        self.health = 100

    def rest(self):
            self.health += self.max_health/10
            if self.health>self.max_health:
                self.health=self.max_health

    def heroPosition(self):
        x=0
        y=0
        for i in self.lvl.map:
            if 'H' in i:
                y=i.index('H')
                break
            else:
                x+=1
        return [x,y]

    def feel(self,dir):
                position=self.heroPosition()
                if(dir=='left'):
                    if position[1]!=0:
                        if self.lvl.map[position[0]][position[1]-1]=='R':
                            self.rope()
                        return self.lvl.map[position[0]][position[1]-1]
                    else:
                        return self.feel('up')
                elif dir=='right':
                    if position[1]+1!=len(self.lvl.map[0]):
                        if self.lvl.map[position[0]][position[1]+1]=='R':
                            self.rope()
                        return self.lvl.map[position[0]][position[1]+1]
                    else:
                        return self.feel('down')
                if len(self.lvl.map)!=1:
                    if dir=='up':
                        if position[0]!=0:
                            if self.lvl.map[position[0]-1][position[1]]=='R':
                                self.rope()
                            return self.lvl.map[position[0]-1][position[1]]
                        else:
                            return self.feel('left')
                    elif dir=='down':
                        if position[0]!=len(self.lvl.map[0]):
                            if self.lvl.map[position[0]+1][position[1]]=='R':
                                self.rope()
                            return self.lvl.map[position[0]+1][position[1]]
                        else:
                            return self.feel('right')

    def rope(self):
        position=self.heroPosition()
        if position[0] <= (len(self.lvl.map)-1) and position[1] <= (len(self.lvl.map[0])-1):

            print "The hero reaches the rope!\nOn to the next level!"
            self.currentLevel += 1

            saveAndExit()
            sys.exit()

    def move(self,dir):
            position=self.heroPosition()
            try:
                if self.feel(dir) ==' ':
                    self.lvl.map[position[0]][position[1]]=' '
                    if(dir=='left'):
                        self.lvl.map[position[0]][position[1]-1]='H'
                    elif dir=='right':
                        self.lvl.map[position[0]][position[1]+1]='H'
                    elif dir=='up':
                        self.lvl.map[position[0]-1][position[1]]='H'
                    elif dir=='down':
                        self.lvl.map[position[0]+1][position[1]]='H'
                elif self.feel(dir) == 'R':
                    self.rope()
            except IndexError:
                print "The hero hits the wall"
                sys.exit()

    def rhealth(self):
        return self.health

    def __str__(self):
        return "H"

    def optwalk(self):
        x=0
        y=0
        for i in self.lvl.map:
            if 'R' in i:
                y=i.index('R')
                break
            else:
                 x+=1
        rPos=[x,y]

        #hero position (already a fucntion..)
        x=0
        y=0
        for i in self.lvl.map:
            if 'H' in i:
                y=i.index('H')
            break
        else:
            x+=1
        hpos=[x,y]

        opt_len=abs(rPos[0]-hpos[0])+abs(rPos[1]-hpos[1])
        opt_dir="cur"

        #the optimization heuristic
        try:
            if abs(rPos[0]-hpos[0])+abs(rPos[1]-(hpos[1]+1))<opt_len:
                opt_len=abs(rPos[0]-hpos[0])+abs(rPos[1]-(hpos[1]+1))
                opt_dir="right"
        except:
            pass

        if abs(rPos[0]-hpos[0])+abs(rPos[1]-(hpos[1]-1))<opt_len:
            opt_len=abs(rPos[0]-hpos[0])+abs(rPos[1]-(hpos[1]-1))
            opt_dir="left"

        if abs(rPos[0]-(hpos[0]-1))+abs(rPos[1]-hpos[1])<opt_len:
            opt_len=abs(rPos[0]-(hpos[0]-1))+abs(rPos[1]-hpos[1])
            opt_dir="up"

        try:
            if abs(rPos[0]-(hpos[0]+1))+abs(rPos[1]-hpos[1])<opt_len:
                opt_len=abs(rPos[0]-(hpos[0]+1))+abs(rPos[1]-hpos[1])
                opt_dir="down"
        except:
            pass

        return opt_dir