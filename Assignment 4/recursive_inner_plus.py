# Daniel Johnston
# u0757256
# Assignment 4 (Advanced Function and Logic)

# Problem #2

# Write the a python program that, given an input list of any level of complexity/nestedness, 
# will return the inner most list plus 1. This is to be done with recursion. 
# Note: the input will contain only integers or lists. 

# global variable for easier reuse in other uses of the code
indexDepth = []
depthReachedTemp =[]

# defined method for list analysis and adding 1 to innermost item using recursion
def listNautilus(searchList):
    
    # initial setting of variables
    deepTreasureChest = []
    maxDepthReached = -1
    
    # clearing global list temp to prevent incorrect data being used
    global indexDepth, depthReachedTemp
    indexDepth = []
    depthReachedTemp =[]

    # beginning of recursion
    def deepDiveSearch(current, depth):
        nonlocal maxDepthReached, deepTreasureChest

        # sublist of lists
        sublists = [item for item in current if isinstance(item, list)]

        #if not deeper list record values and perform addition
        if not sublists:
            if depth > maxDepthReached:
                
                # updating max depth
                maxDepthReached = depth
                
                # collecting initial max depth values
                indexDepth.append(current) 

                # performing addition to found deeper values
                deepTreasureChest = [[x + 1 for x in current]]
                
                # collecting max depth
                depthReachedTemp.append(maxDepthReached+1)

            elif depth == maxDepthReached:
                
                # collecting max depth values
                indexDepth.append(current)

                # performing addition to found deeper values
                deepTreasureChest.append([x + 1 for x in current])
                
                # collecting max depth adding 1 to offset for 0 base
                depthReachedTemp.append(maxDepthReached+1)

            return

        # recursive call
        for sublist in sublists:
            deepDiveSearch(sublist, depth + 1)

    deepDiveSearch(searchList, 0)

    # returning updated list of values
    return deepTreasureChest

# function to print results and extra data to showcase the list and the innermost values prior to addition(easier reuse :) )
def printResults(inputListForAnalysis):
    separationLine = "!!ii!!ii!!ii!!ii!!ii!!ii!!ii!!ii!!ii!!ii!!"
    print(separationLine,"\n")
    print("Innermost/deepest values plus one:\n",listNautilus(inputListForAnalysis),
          "\n\nBased on innermost/deepest initial values:\n",indexDepth,"\nInnermost/Deepest level was:\n",depthReachedTemp,"\nFound in the provided initial list:\n",inputListForAnalysis,"\n")
    print(separationLine)


# creating a number of list conditions and then calling printresults method which inturn documents and calls recursive function to do the analysis.
printResults([1, [2, [3]], [4, [5]], [[6]]])

printResults([1, 2, 3, 4, [5, 6, 7, [8, 9]]])

printResults([[1, 2], [3, 4]])

printResults([1, 2,[3,4,[2,2,2,[5]],5],3, 4, [5, 6, 7, [8, 9]]])

printResults([1, [2, [3,45,[223]]], [4, [5]], [[6]]])

printResults([1, [2, [3,45]], [4, [5]]])

printResults([[[33,12],111],1223,[48,443,12,[72]]])