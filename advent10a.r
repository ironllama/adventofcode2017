# allFileStr = read.csv("advent10.in")
# allFileStr <- "129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108"  # Starting as string.
# puzzleList <- 0:254

allFileStr <- "3, 4, 1, 5"
puzzleList <- 0:4
skipSize <- 0

allFileStrList <- strsplit(allFileStr, ",")  # Spliting the string into a LIST.
allFileStrVect <- unlist(allFileStrList)  # Turn the list into a single VECTOR.
allFileIntVect <- as.integer(allFileStrVect)  # Cast the string list into numeric integers.

allFileIntVect
puzzleList
for (i in 1:length(allFileIntVect)) {
    numToGrab <- allFileIntVect[i]
    subVect <- puzzleList[i:(i + numToGrab - 1)]
    message("NUM_TO_GRAB:", numToGrab, " SUBVECT: ", subVect)
    skipSize <- skipSize + 1
}