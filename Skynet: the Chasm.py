import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(raw_input()) # the length of the road before the gap.
gap = int(raw_input()) # the length of the gap.
platform = int(raw_input()) # the length of the landing platform.

# game loop
while 1:
    speed = int(raw_input()) # the motorbike's speed.
    coordX = int(raw_input()) # the position on the road of the motorbike.
    print >> sys.stderr, road, gap, platform, speed, coordX
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    if coordX == road-1:
        print "JUMP"
    elif coordX > road or speed > gap+1:
        print "SLOW"
    elif speed < gap+1:
        print "SPEED"
    else:
        print "WAIT"
    #print "SPEED" # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
