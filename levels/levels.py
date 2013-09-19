from map import Map

class level(Map):
    def level1(self):
        self.level = 1
        self.map = [['H',' ',' ',' ',' ','R'],[]]
        self.display()
        
    def level2(self):
        self.level = 2
        self.map = [['H',' ',' ','O',' ','R'],[]]
        self.display()
        
    def level3(self):
        self.level = 3
        self.map = [['H',' ','O',' ','O',' ','R'],[]]
        self.display()
        
    def level4(self):
        self.level = 4
        self.map = [[' ','H',' '],
                    [' ',' ',' '],
                    [' ',' ','R']]
        self.display()
        
    def level5(self):
        self.level = 5
        self.map = [['H','O',' '],
                    [' ','O',' '],
                    [' ',' ','R']]
        self.display()