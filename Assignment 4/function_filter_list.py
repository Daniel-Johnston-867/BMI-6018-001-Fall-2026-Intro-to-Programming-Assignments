# Daniel Johnston
# u0757256
# Assignment 4 (Advanced Function and Logic)

# Problem #3

# Write a Python program that defines a standard function to filter a list of numbers. 
# The function should accept two arguments:

#     A list of numbers
#     A user-defined threshold value

# The function should return a new list containing only the numbers that are less than 
# or equal to the specified threshold. Values greater than the threshold should be excluded.

# filter function definition
def numFilterFunc(numList, thresholdNum):
    
    # result list declaration
    rList = []

    # Iteration through list and compare value to threshold value
    for numItem in numList:

        # if less then or equal add to result list else ignore
        if numItem <= thresholdNum:
            rList.append(numItem)

    # return result list
    return rList

def printResults(inList,checkPoint):
    print("V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V\n")
    print("Filtered list of",len(numFilterFunc(inList,checkPoint)),"entries with values less than or equal to the threshold value:\n",numFilterFunc(inList,checkPoint),
          "\n\nBased on threshold:",checkPoint,"\nAnd using the",len(inList),"entries in initial list:\n",inList,"\n")
    print("V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V^V")

# calling my print function to write results and begin filtering the list via numFilterFunc
# print results uses the input of the list input first followed by the threshold value
printResults([1, 15, 38, 35, 112, 27, 250,320],100)

printResults([8, 6, 7, 5, 3, 0, 9,7,34,12],5)

printResults([2,4,6,8,10],7)

printResults([1000, 123, 452, 8000, 1121, 7967, 20,15,4566,123,332,500],500)

printResults([563, 895, 12228, 3078, 21442, 712, 2320,1234,4321],2000)

printResults([1, 2, 3, 4, 15, 66, 212],4)

printResults([610, 765, 1348, 322, 122, 887, 220,456,122,321,231,554,234],300)

printResults([32,45,676,34,23,14,27,99,345,123,123,44,232,609,123,445,6557,12,333,27,23,45,43,22,78,97,44,322,12,444,67,890,23,444,343,57,56],100)

