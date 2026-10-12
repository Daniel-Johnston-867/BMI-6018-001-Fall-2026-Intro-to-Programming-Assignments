# Daniel Johnston
# u0757256
# Assignment 4 (Advanced Function and Logic)

# Problem #1

# Write a python program that, given an input list of any level of complexity/nestedness, 
# will return the inner most list plus 1. This is to be done with a while loop.
# Note: the input will contain only integers or lists. 

#*************************************************************************************************
#*************************************************************************************************

# global variables for easier reuse in other uses of the code
indexDepth = []
inputListTemp = []

# defined method for list analysis and adding 1 to innermost item
def listExtrapolator(input_list):
    levelTracking = [input_list]
    
    # clearing global list temp to prevent incorrect data being used
    global inputListTemp
    inputListTemp = input_list

    # clearing global index variable prior to iteration to prevent incorrect data being used
    global indexDepth
    indexDepth = []

    # while loop set to while true to iterate through all subsets to collect all of the list depth and to analyze the list(s)
    while True:
        levelAlt = []
        
        # iterating through the list parts
        for currentItem in levelTracking:
            for item in currentItem:
                # checking if item in list is a list or not
                if isinstance(item, list):
                    levelAlt.append(item)

        # innermost list check
        if not levelAlt:
            indexDepth.append(levelTracking)
            return [[x + 1 for x in item] for item in levelTracking]

        levelTracking = levelAlt


# function to print results and extra data to showcase the list and the innermost values prior to addition(easier reuse :) )
def printResults(inputList1):
    print("***********************************************************************\n")
    print("Innermost/deepest values plus one =",listExtrapolator(inputList1),
          "\n\nBased on innermost/deepest initial values",indexDepth,"\nFound in the provided initial list",inputListTemp,"\n")
    print("***********************************************************************")


# creating a number of list conditions and then calling printresults method which inturn documents and calls listExtrapolator method to do the analysis.
printResults([1, 2, 3, 4, [5, 6, 7, [8, 9]]])

printResults([1, [2, [3]], [4, [5]], [[6]]])

printResults([[1, 2], [3, 4]])

printResults([1, [2, [3]], [4, [5]], [[6],[2,3,4,[1]]]])

printResults([1, 2,[3,4,[2,2,2,[5]],5],3, 4, [5, 6, 7, [8, 9]]])

printResults([[[23,555],232],1234,3321,1000])

printResults([[[23,555],232],1234,[1, [2, [3]], [4, [5]], [[6],[2,3,4,[1,45,923]],[1, [2, [3]], [4, [5]], [[6,[45,76]]]]]],3321,[1, 2,[3,4,[2,2,2,[5]],5],3, 4, [5, 6, 7, [8, 9]]],1000])