def wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [6,9,12]

   whereas the expected correct answer is, [2,3,4]

   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   arg1_index=0
   while arg1_index < len(arg1):      
      print("While loop index =",arg1_index) # added print to show while loop
      arg_2_sum = 0
      for arg2_elements in arg2: 
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
         print("For loop element =",arg2_elements,", arg_2_sum =",arg_2_sum) # printing element and sum values 
      arg1[arg1_index]=arg_2_sum  
      arg1_index+=1
      print("\n") # separates the printed outputs to show execution grouping
   return arg1
arg1 = [1,2,3]
arg2 = [1,1,1]

# Question 1.a
# Using the print() function only, get the wrong_add_function to print out where
# it is making a mistake, given the expected output for ex, "we are making an error 
# in the loop", which you would put near the loop. 
# Structure the print() statement to show what the expected output ought to be
# via f-strings: ie "The correct answer is supposed to be: [...]".

argTmp = arg1.copy()

print("We are making an error in the innermost loop resulting in the following wrong answer:",wrong_add_function(arg1, arg2))

print(f"The correct answer should be: {argTmp[0]+arg2[0]},{argTmp[1]+arg2[1]},{argTmp[2]+arg2[2]}")

print("\n*****************************************************************************")
print("\nWrong add function analysis:\nThe code loops through arg2 twice, once in the for loop and once in the list comprehension (innermost section of the code).  The outer for loop repeats the calculation 3 times always overwriting the arg_2_sum value.  Also the arg2_elements variable isnt used inside the loop. as seen in the printed out lines above.")
print("\n*****************************************************************************\n")

#***********************************************************************
#***********************************************************************
#***********************************************************************
#***********************************************************************

def Simplified_correct_add_function(arg1,arg2):
   arg1_index=0
   argSum=[]

   while arg1_index < len(arg1):      # iterates through the list via while loop
      print("While loop index =",arg1_index)
      argSum.append(arg1[arg1_index]+arg2[arg1_index]) # uses new list to collect values from addition
      print(f"Arg 1 = {arg1[arg1_index]} and Arg 2 = {arg2[arg1_index]}")
      print(f"Arg sum = {argSum}")
      arg1_index+=1 # increments iteration
      print("\n") # separates the printed outputs to show execution grouping

   # without print statements**
   # while arg1_index < len(arg1): # iterates through the list via while loop
   #    argSum.append(arg1[arg1_index]+arg2[arg1_index]) # uses new list to collect values from addition
   #    arg1_index+=1 # increments iteration

   return argSum
arg1 = [1,2,3]
arg2 = [1,1,1]

print("(correct updated version below) Using my changed/simplified and corrected method we get the following:",Simplified_correct_add_function(arg1, arg2))

print("\n*****************************************************************************\n")

#***********************************************************************
#***********************************************************************
#***********************************************************************
#***********************************************************************

# Question 1.b
# Then, changing as little as possible, modify the function, using the same 
# general structure to output the correct answer. Call this new function 
# correct_add_function()

def correct_add_function(arg1,arg2):
   arg1_index=0
   argSum=[]

   while arg1_index < len(arg1):      
      for index, arg2_elements in enumerate(arg2):
         if index == arg1_index:
            arg1[arg1_index] = arg1[arg1_index] + arg2_elements # Replaced "arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])"
      arg1_index+=1
   return arg1

# Original for comparison***
        # def wrong_add_function(arg1,arg2):
        #    arg1_index=0

        #    while arg1_index < len(arg1):      
        #       arg_2_sum = 0
        #       for arg2_elements in arg2: 
        #          arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
        #       arg1[arg1_index]=arg_2_sum  
        #       arg1_index+=1
        #    return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

print("\n*****************************************************************************\n")
print("Using my corrected method we get the following:",correct_add_function(arg1, arg2))
print("\n*****************************************************************************\n")


#***********************************************************************
#***********************************************************************
#***********************************************************************
#***********************************************************************

print("\n*****************************************************************************\n")
print("PART 2")
print("\n*****************************************************************************\n")

def initial_wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [4,5,6]
   
   If the lists are lists of strings, concatenate them
   Example:
      > wrong_add_function(['1','2','3'],['1','1','1'])
      > ['1111','2111','3111']
   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1
arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

print(initial_wrong_add_function(arg_str_1,arg_str_2))

# Question 2.a
# Update the numeric section of the function with your changes from 1 for both 2.b and 2.c

def wrong_add_function(arg1,arg2):

   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            for index, arg2_elements in enumerate(arg2):
                if index == arg1_index:
                    arg1[arg1_index] = arg1[arg1_index] + arg2_elements
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1
arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

print(wrong_add_function(arg_str_1,arg_str_2))


#***********************************************************************
#***********************************************************************
#***********************************************************************
#***********************************************************************

# Question 2.b
# Without modifying the string section code itself or the input directly, 
# write a try, except block that catches the issue with the input below and 
# returns an error message to the user, in case users give invalid inputs,
# (for example an input of ["5","2", 5])
# : "Your input argument [1 or 2] at element [n]
# is not of the expected type. Please change this and rerun. Name this function 
# exception_add_function()

def exception_add_function(arg1,arg2):
    try:
       #numeric section
       if sum([type(i)==int for i in arg1])==len(arg1) and \
          sum([type(i)==int for i in arg2])==len(arg2):
             arg1_index=0
             while arg1_index < len(arg1):
                for index, arg2_elements in enumerate(arg2):
                    if index == arg1_index:
                        arg1[arg1_index] = arg1[arg1_index] + arg2_elements
                arg1_index+=1
             return arg1
       #string section
       elif sum([type(i)==str for i in arg1])==len(arg1) and \
          sum([type(i)==str for i in arg2])==len(arg2):
             arg1_index=0
             while arg1_index < len(arg1):
                arg_2_sum = ''
                for arg2_elements in arg2:
                   arg_2_sum += arg2_elements
                arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
                arg1_index+=1
             return arg1
       else:
            raise TypeError

    except TypeError:
        typeExpected = type(arg1[0]) if arg1 else int

        for item, element in enumerate(arg1):
            if type(element) != typeExpected:
                return f"Your input in argument 1 at index #{item+1} is not of the expected type ({typeExpected}). Please change this and rerun. \nArgument 1 = {arg1}" # added 1 to item to offset from 0 base

        for item, element in enumerate(arg2):
            if type(element) != typeExpected:
                return f"Your input in argument 2 at index #{item+1} is not of the expected type ({typeExpected}). Please change this and rerun. \nArgument 2 = {arg2}" # added 1 to item to offset from 0 base


arg_str_1=['1','2','3']
arg_str_2=['1','1',1]

print(exception_add_function(arg_str_1,arg_str_2),"\n")

arg_str_1=['1','2','3']
arg_str_2=['1','1','1']

print(exception_add_function(arg_str_1,arg_str_2),"\n")

arg_str_1=['1',2,'3']
arg_str_2=['1','1','1']

print(exception_add_function(arg_str_1,arg_str_2),"\n")

arg_str_1=[1,2,3]
arg_str_2=['1',1,1]

print(exception_add_function(arg_str_1,arg_str_2),"\n")

arg_str_1=[1,2,'3']
arg_str_2=[1,1,1]

print(exception_add_function(arg_str_1,arg_str_2),"\n")

arg_str_1=[1,2,3]
arg_str_2=[1,1,1]

print(exception_add_function(arg_str_1,arg_str_2),"\n")


#***********************************************************************
#***********************************************************************
#***********************************************************************
#***********************************************************************

# Question 2.c
# Without modifying the string section code itself or the input directly, 
# write a try, except block that catches the issue with the input below and 
# gets it to process via the string section. IE, do not, outside the function,
# change the values of arg_str_1 or arg_str_2. Name this function 
# correction_add_function(), i.e you will not be updating the wrong_add_function,
# you will simply handle the error of wrong inputs in a seperate function, you want
# the wrong_add_function to output its current result you are only bolstering the 
# function for edge cases .


def wrong_add_function(arg1,arg2):

   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            for index, arg2_elements in enumerate(arg2):
                if index == arg1_index:
                    arg1[arg1_index] = arg1[arg1_index] + arg2_elements
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1


def correction_add_function(arg1, arg2):
    try:
        testingFunction = wrong_add_function(arg1, arg2)
    
        if testingFunction is None:
            print("\nOne or more of the arguments contained at least 1 mismatched type.\nConverting all elements to strings to continue.")
            raise TypeError
        
    except TypeError:
        newArg1 = [str(item) for item in arg1]
        newArg2 = [str(item) for item in arg2]
        return wrong_add_function(newArg1, newArg2)


arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

print(correction_add_function(arg_str_1,arg_str_2))

arg_str_1=['10',20,'30']
arg_str_2=['10','10', '10']

print(correction_add_function(arg_str_1,arg_str_2))

arg_str_1=['6',7,'8']
arg_str_2=[5,'5', '5']

print(correction_add_function(arg_str_1,arg_str_2))