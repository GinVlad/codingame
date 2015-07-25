import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while 1:
    spaceX, spaceY = [int(i) for i in raw_input().split()]
    top = 0
    shoot = 0
    for i in xrange(8):
        mountainH = int(raw_input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        print >> sys.stderr, "MountainH: ", mountainH
        if (mountainH >= top):
            top = mountainH
            shoot = i
    
    print >> sys.stderr, "MountainH: ", mountainH, "Top: ", top, "Shoot: ", shoot, "SpaceX: ", spaceX, "SpaceY: ", spaceY
    
    if spaceX==shoot:
        print "FIRE"
    else:
        print "HOLD"
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    #print "HOLD" # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).
