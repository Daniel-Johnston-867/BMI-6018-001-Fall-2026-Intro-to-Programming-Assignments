"""
*************************************
 Daniel Johnston U0757256
 NumPy Assignment
*************************************

1. Import numpy as np and print the version number. (5 Points)

2. Create a 1D array of numbers from 0 to 9. Desired output:
    #> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) (10 Points)

3. Import a dataset with numbers and texts keeping the text intact in python numpy.
    Use the iris dataset available from Iris dataset. (20 Points)

4. Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset.
    Use the iris dataset available from Iris dataset. (20 Points)

5. From the array a, replace all values greater than 30 to 30 and less than 10 to 10.
"""


# question 1

import numpy as np
print("Question 1\n")
print("Version of NumPy:",np.__version__)

# question 2

array_1 = np.array(range(10))

print("\nQuestion 2\n")
print("#> array(",array_1,")")

# question 3

webLink = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# delimiter = item separator, dtype of object allows a way to store mixed data types
irisData = np.genfromtxt(webLink, delimiter=',',dtype='object')

print("\nQuestion 3\n")
print("Iris DataSet from website:\n",webLink,"\n\nIris DataSet contents:\n",irisData)

# question 4

# 4th column = petalwidth
petalWidth = irisData[:, 3]

print("\nQuestion 4\n")
print("Column #4 Contents:\n", petalWidth)
print("********************************************\n\n")

# converting to float array for easier searching
floatArray = petalWidth.astype(float)

print("Column #4 Contents as float array:\n", floatArray)
print("********************************************\n\n")

valGreaterCheck = np.argmax(floatArray > 1.0)

print("Found first instance of greater then 1.0 at instance:",valGreaterCheck,"\nWith the value being:", floatArray[valGreaterCheck])

# question 5

np.random.seed(100)
a = np.random.uniform(1,50, 20)

print("\nQuestion 5\n")
print("Initial array a:\n",a)

copyOfA = a.copy()

# using clip to update the data
updatedA = np.clip(a, 10, 30)

# running update as boolean
copyOfA[copyOfA>30]=30
copyOfA[copyOfA<10]=10

print("\nUpdated array values of a:\n",updatedA)

print("\nUsing a boolean method to update array a:\n",copyOfA)