#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      viren
#
# Created:     19/09/2013
# Copyright:   (c) viren 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import units/base

def main():
    f.read('player.txt')

    if f.find('while') or f.find('for'):
        print 'Loops found in the source'
        sys.exit()


if __name__ == '__main__':
    main()
