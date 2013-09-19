import base_unit

class Hero(base_unit.BaseUnit):
    def __init__(self):
        self.max_health = 100
        self.attack_power = 25
        self.health = 100

    def rest():
        if health < max_health and health + max_health/10 < max_health:
            health += max_health/10
    
    def position(self,lvl):
        x=0
        y=0
        for i in lvl.map:
            if 'H' in i:
                y=i.index('H')
                break
            else:
                x+=1
        return [x,y]
            
    def feel(self,dir,lvl):
            pstn=self.position(lvl)
            if(dir=='left'):
                return lvl.map[pstn[0]][pstn[1]-1]
            elif dir=='right':
                return lvl.map[pstn[0]][pstn[1]+1]
            elif dir=='up':
                return lvl.map[pstn[0]-1][pstn[1]]
            elif dir=='down':
                return lvl.map[pstn[0]+1][pstn[1]]
              
    def walk(self,dir,lvl):
            pstn=self.position(lvl)
            if self.feel(dir,lvl) ==' ':
                lvl.map[pstn[0]][pstn[1]]=' '
                if(dir=='left'):
                    lvl.map[pstn[0]][pstn[1]-1]='H'
                elif dir=='right':
                    lvl.map[pstn[0]][pstn[1]+1]='H'
                elif dir=='up':
                    lvl.map[pstn[0]-1][pstn[1]]='H'
                elif dir=='down':
                    lvl.map[pstn[0]+1][pstn[1]]='H'