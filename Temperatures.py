import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input()) # the number of temperatures to analyse
TEMPS = raw_input() # the N temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
if N>0:
    TEMPS_arr = TEMPS.split()
    closestZero = 5526
    print >> sys.stderr, type(TEMPS_arr), TEMPS_arr
    for i in TEMPS_arr:
        #print i, type(i)
        temp = int(i)
        temp_abs = math.fabs(temp)
        check = math.fabs(closestZero)
        print >> sys.stderr, temp, math.fabs(temp), check
        if (check>temp_abs) or ((check==temp_abs) and (temp>0)):
            closestZero = temp
            print >> sys.stderr, closestZero
        else:
            print >> sys.stderr, "No add"
    print closestZero
        
        
else:
    print "0"
