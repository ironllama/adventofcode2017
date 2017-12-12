# Advent of Code 2017
# Day 3 - Part I
# Python


'''After racking my brain for an excruciating 30 minutes for an algorithm to determine location and not finding any
(my Maths-fu is not so advanced), I decided to brute force the coorindates for each number. The nice thing about using
coordinates in any grid-distance problem is that the distance can be determined by adding together the absolute values
of the X and Y cooridinates. In other words, on a Cartesian graph, for any arbitrary point coordinate on the graph, to
go back to (0,0) you are first taking X and bringing it back to the 0 value, and then taking the Y and bringing that
back to the 0 value. So total distance will always be just adding those two distances.

I use a layers value to track which layer (or coordinate space) each loop will process. Layers should look like:
    3 3 3 3 3 3 3
    3 2 2 2 2 2 3
    3 2 1 1 1 2 3
    3 2 1 0 1 2 3
    3 2 1 1 1 2 3
    3 2 2 2 2 2 3
    3 3 3 3 3 3 3

The coordinates for the above are:
    (-3, 3) (-2, 3) (-1, 3) (0, 3) (1, 3) (2, 3) (3, 3)
    (-3, 2) (-2, 2) (-1, 2) (0, 2) (1, 2) (2, 2) (3, 2)
    (-3, 1) (-2, 1) (-1, 1) (0, 1) (1, 1) (2, 1) (3, 1)
    (-3, 0) (-2, 0) (-1, 0) (0, 0) (1, 0) (2, 0) (3, 0)
    (-3, -1) (-2, -1) (-1, -1) (0, -1) (1, -1) (2, -1) (3, -1)
    (-3, -2) (-2, -2) (-1, -2) (0, -2) (1, -2) (2, -2) (3, -2)
    (-3, -3) (-2, -3) (-1, -3) (0, -3) (1, -3) (2, -3) (3, -3)

Note the pattern of increasing/decreasing X and then Y as you unroll the layers:
Layer 1: (1, 0) (1, 1) (0, 1) (-1, 1) (-1, 0) (-1, -1) (0, -1) (1, -1)
Layer 2: (2, -1) (2, 0) (2, 1) (2, 2) (1, 2) (0, 2) (-1, 2) (-2, 2) (-2, 1) (-2, 0) (-2, -1) (-2, -2) (-1, -2) (0, -2) (1, -2) (2, -2)
And so on...
'''
# targetNum = 12
# targetNum = 23
# targetNum = 1024
targetNum = 347991  # Number we're shooting for!


numGrid = [[0,0], [0,0]]  # List of Cartesian coordinates. Indices are the number. Seeded with center num 1.
currNum = 0  # Also tracking current number in question, since we're putting some stuff outside in a function
def addCoordinate(x, y):
    '''This function is a convenience function that adds the current X,Y coordinates into the numGrid list with
    the indices of the list matching the number in question. So, for example to find where the number 1024 is, you
    can look at numGrid[1024] and get the coordinates! This is actually not really necessary, one is really only
    interested when the current number being tested is the target number, but I thought it would be useful to store
    the coordinates to verify that the program was working.'''
    global currNum, numGrid  # Since we're changing these global variables.
    #print("Adding: [", currNum, "][", x, "][", y, "]")

    numGrid.append([x,y])

    if currNum == targetNum:
        #print(numGrid)
        print("Final Location: ", x, ", ", y, " Distance: ", (abs(x) + abs(y)))  # Print final coord and distance!
        exit()

    currNum += 1


# Initial setup for everything.
layer = 1  # This will keep track of which layer around the center (0,0) that we're on, so we know how far we can go.
currNum = 2  # Since we've already added 0 and 1 to the numGrid list, we're starting at 2!
x = 1  # The X coordinate for 2
y = 0  # The Y coordinate for 2.
addCoordinate(x, y)

# The loop going through all the numbers -- it's an infite loop that will be terminated when the addCoordinate()
# function calls exit(). It's VERY ugly and not a good way to end a proper program. But for a fun puzzle, meh.
while True:
    while y < layer:  # Since we always start at the lower right of a layer, first we go up to the layer limit.
        #print("A: y[", y, "] layer[", layer, "]")
        y += 1
        addCoordinate(x, y)
    while x > (layer * -1):  # Then we go left.
        x -= 1
        addCoordinate(x,y)
    while y > (layer * -1):  # Then we go down.
        y -= 1
        addCoordinate(x,y)
    while x < layer:  # Then we go right.
        x += 1
        addCoordinate(x,y)

    # After finishing a layer, we move into the next layer and keep going until we find our number!
    #print("Finished layer 1")
    layer += 1
    x += 1
    addCoordinate(x,y)
