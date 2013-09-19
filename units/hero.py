import base_unit
import sys
class Hero(base_unit.BaseUnit):
    def __init__(self, lvl):
        self.lvl = lvl
        self.max_health = 100
        self.attack_power = 25
        self.health = 100

    def rest():
        if health < max_health and health + max_health/10 < max_health:
            health += max_health/10

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
                    if self.lvl.map[position[0]][position[1]-1]=='R':
                        self.rope()
                    return self.lvl.map[position[0]][position[1]-1]
                elif dir=='right':
                    if self.lvl.map[position[0]][position[1]+1]=='R':
                        self.rope()
                    return self.lvl.map[position[0]][position[1]+1]
                if len(self.lvl.map)!=1:
                    if dir=='up':
                        if self.lvl.map[position[0]-1][position[1]]=='R':
                            self.rope()
                        return self.lvl.map[position[0]-1][position[1]]
                    elif dir=='down':
                        if self.lvl.map[position[0]+1][position[1]]=='R':
                            self.rope()
                        return self.lvl.map[position[0]+1][position[1]]
                sys.exit()
    def rope(self):
        position=self.heroPosition()
        if position[0]<=(len(self.lvl.map)-1) and position[1]<=(len(self.lvl.map[0])-1):
            print "LEVEL COMPLETE!"
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
                print "There is no escape!"
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