class Map:
    def __init__(self):
        self.level = 0
        self.map = []
        
    def display(self):
        for i in xrange( len( self.map ) ):
            for j in xrange( len( self.map[i] ) ):
                print self.map[i][j],
            print ' '