import sys
class Map:
    def __init__(self):
        self.level = 0
        self.map = []

    def display(self):
        a=0
        while a<len(self.map[0]):
            sys.stdout.write('----')
            a=a+1
        sys.stdout.write("-\n")

        for i in xrange( len( self.map ) ):
            sys.stdout.write('| ')
            for j in xrange( len( self.map[i] ) ):
                sys.stdout.write(str(self.map[i][j])+' | ')
            sys.stdout.write("\n")
            a=0

            while a<len(self.map[0]):
                sys.stdout.write('----')
                a=a+1
            sys.stdout.write("-\n")