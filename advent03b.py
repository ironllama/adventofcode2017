# Advent of Code 2017
# Day 3 - Part II
# Python


'''This one was definitely going to be brute-force for me. Knowing it from the get-go and not seeing any patterns to take
advantage of, I decided to generate the grid as I went. The tricky thing was to determine how large to actually make the
grid using list of lists, with the outer list being the Y values and the inner list being the X. Also, it was getting late
and I was getting sleepy. So, I just decided to wing it and if the program ended up with a list index out of bounds, I'd
just increase the size of the array in code. (Otherwise the program would have to regenerate a new, larger list and then
copy over all the values, with the center readjusted to the size of the new list. Not fun.)
'''
# targetNum = 12
# targetNum = 23
# targetNum = 1024
targetNum = 347991  # Number we're shooting for!

# Initial setup for everything.

totalLayers = 11 

# Initialize the grid to 0's
overallGrid = []
for i in range(totalLayers):
    innerArray = [0]*totalLayers
    overallGrid.append(innerArray)


# Convenience function to actually print out the grid (list of lists)
def prettyPrintGrid():
    # Print out the grid, in pretty format.
    for i in range(totalLayers - 1, 0, -1):
        for j in range(totalLayers):
            #print("(", j, ", ", i , ")", end=' ')
            print(str(overallGrid[j][i]), end='\t')
        print()


# Function that checks all the surrounding values and adds them up to determine the current coordinate's value.
def figureItOut(x, y):
    global overallGrid  # Since we're using and changing this value.

    east = overallGrid[x + 1][y]
    northeast = overallGrid[x + 1][y + 1]
    north = overallGrid[x][y + 1]
    northwest = overallGrid[x - 1][y + 1]
    west = overallGrid[x - 1][y]
    southwest = overallGrid[x - 1][y -1]
    south = overallGrid[x][y - 1]
    southeast = overallGrid[x + 1][y - 1]
    overallGrid[x][y] = east + northeast + north + northwest + west + southwest + south + southeast
    # print("[", x, "][", y, "]: [", overallGrid[x][y], "]")

    if overallGrid[x][y] > targetNum:
        prettyPrintGrid()
        print("FOUND: ", overallGrid[x][y])
        exit()


# Code for moving the way we want to move through the grid!
center = int(totalLayers/2)
currLayer = 1
overallGrid[center][center] = 1

x = center + 1  # The X coordinate for second 1
y = center  # The Y coordinate for second 1.
figureItOut(x, y)

# The loop going through all the numbers -- it's an infite loop that will be terminated when the figureItOut()
# function calls exit(). It's VERY ugly and not a good way to end a proper program. But for a fun puzzle, meh.
while True:
    # After drawing out what I wanted to happen, I found that currLayer * 2 is the size of one layer.
    for i in range((currLayer * 2) - 1):  # Always start at the lower right of a layer. Already have first block, so -1. Go up.
        #print("A: y[", y, "] currLayer[", currLayer, "]")
        y += 1
        figureItOut(x, y)
    for i in range(currLayer * 2):  # Then we go left.
        x -= 1
        figureItOut(x,y)
    for i in range(currLayer * 2):  # Then we go down.
        y -= 1
        figureItOut(x,y)
    for i in range((currLayer * 2) + 1):  # Then we go right. Also adding in the first block of the next layer.
        x += 1
        figureItOut(x,y)

    # After finishing a currLayer, we move into the next currLayer and keep going until we find our number!
    #print("Finished Layer [", currLayer, "]")
    currLayer += 1
