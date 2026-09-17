#! /usr/bin/env python3
# Author: Gsporle
# Version: 1.0
# Description: This is a Game of Tanks
"""
    GOT - Game of Tanks
"""
import sys

from app import tank

def main():
    # Create/Instantiate 3 Tank objects
    kim_tank = tank.Tank("german", "tiger")
    joe_tank = tank.Tank("american", "sherman")
    tony_tank = tank.Tank("british", "churchill")

    #and the game begins..
    kim_tank.accel(61)
    joe_tank.accel(34)

    tony_tank.rotate_left(289)
    tony_tank.accel(23)
    tony_tank.shoot()
    return None

#Namespace Trick
if __name__ == "__main__"
    main()
    sys.exit(0)

