import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# lightX: the X position of the light of power
# lightY: the Y position of the light of power
# initialTX: Thor's starting X position
# initialTY: Thor's starting Y position
lightX, lightY, initialTX, initialTY = [int(i) for i in raw_input().split()]

# game loop
while 1:
    remainingTurns = int(raw_input())
    if lightX!=initialTX and lightY!=initialTY:
        if initialTX>lightX and initialTY>lightY:
            print "NW"
            initialTX = initialTX-1
            initialTY = initialTY-1
        elif initialTX>lightX and initialTY<lightY:
            print "SW"
            initialTX = initialTX-1
            initialTY = initialTY+1
        elif initialTX<lightX and initialTY>lightY:
            print "NE"
            initialTX = initialTX+1
            initialTY = initialTY-1
        elif initialTX<lightX and initialTY<lightY:
            print "SE"
            initialTX = initialTX+1
            initialTY = initialTY+1
    else:
        if lightX == initialTX:
            if lightY < initialTY:
                print "N"
                initialTY = initialTY - 1
            else:
                print "S"
                initialTY = initialTY + 1
        elif lightY == initialTY:
            if lightX < initialTX:
                print "W"
                initialTX = initialTX - 1
            else:
                print "E"
                initialTX = initialTX + 1
    # Write an action using print
    # To debug: 
    print >> sys.stderr, "Debug messages..."
    
    #print "SE" # A single line providing the move to be made: N NE E SE S SW W or NW
