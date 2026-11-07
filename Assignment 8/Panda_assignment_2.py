"""
Daniel Johnston (u0757256)
Question 1 (15 Points)
Compute the euclidean distance between series (points) p and q, without using a packaged formula.
Input
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


Question 2 (15 Points)
Change the order of columns of a dataframe. Interchange columns 'a' and 'c'.
Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))


Question 3 (15 Points)
Change the order of columns of a dataframe.  Create a generic function to interchange two columns, without hardcoding column names.
Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))


Question 4 (15 Points)
Format or suppress scientific notations in a pandas dataframe. Suppress scientific notations like ‘e-03’ in df and print upto 4 numbers after decimal.
Input
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
df
#>          random
#> 0  3.474280e-03
#> 1  3.951517e-05
#> 2  7.469702e-02
#> 3  5.541282e-28
Desired Output
#>    random
#> 0  0.0035
#> 1  0.0000
#> 2  0.0747
#> 3  0.0000


Question 5 (15 Points)
Create a new column that contains the row number of nearest column by euclidean distance. Create a new column such that, each row contains the row number of nearest row-record by euclidean distance.
Input
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
df
#     p   q   r   s
# a  57  77  13  62
# b  68   5  92  24
# c  74  40  18  37
# d  80  17  39  60
# e  93  48  85  33
# f  69  55   8  11
# g  39  23  88  53
# h  63  28  25  61
# i  18   4  73   7
# j  79  12  45  34
Desired Output
df
#    p   q   r   s nearest_row   dist
# a  57  77  13  62           i  116.0
# b  68   5  92  24           a  114.0
# c  74  40  18  37           i   91.0
# d  80  17  39  60           i   89.0
# e  93  48  85  33           i   92.0
# f  69  55   8  11           g  100.0
# g  39  23  88  53           f  100.0
# h  63  28  25  61           i   88.0
# i  18   4  73   7           a  116.0
# j  79  12  45  34           a   81.0


Question 6 (15 Points)

Correlation is a statistical technique that shows how two variables are related. Pandas dataframe.corr() method is used for creating the correlation matrix. It is used to find the pairwise correlation of all columns in the dataframe. Any na values are automatically excluded. For any non-numeric data type columns in the dataframe it is ignored.

Input
data = {'A': [45, 37, 0, 42, 50],
        'B': [38, 31, 1, 26, 90],
        'C': [10, 15, -10, 17, 100],
        'D': [60, 99, 15, 23, 56],
        'E': [76, 98, -0.03, 78, 90]
        }
"""

#Question 1 (15 Points)
#Compute the euclidean distance between series (points) p and q, without using a packaged formula.
import pandas as pd
import numpy as np

#Input
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# Euclidean calculation
distance = np.sqrt(((p - q) ** 2).sum())

print("Euclidean distance between p and q:",distance)

#Question 2 (15 Points)
#Change the order of columns of a dataframe. Interchange columns 'a' and 'c'.
#Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

print("Initial dataframe:\n",df)


# swapping columns
df = df[["c", "b", "a", "d", "e"]]

print("\nUpdated dataframe:\n",df)


#Question 3 (15 Points)
#Change the order of columns of a dataframe.  Create a generic function to interchange two columns, without hardcoding column names.
#Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

print("Initial dataframe:\n",df)

# Function takes in dataframe and the 2 columns to swap
def swapColumns(dataframe, col1Index, col2Index):

    # Copies the columns list
    columns = list(dataframe.columns)
    
    # Swap the columns
    columns[col1Index], columns[col2Index] = columns[col2Index], columns[col1Index]
    
    # Return the updated dataframe
    return dataframe[columns]

# printing out the updated dataframe using the function above
print("\nUpdated dataframe:\n",swapColumns(df, 4, 1))

#Question 4 (15 Points)
#Format or suppress scientific notations in a pandas dataframe. Suppress scientific notations like ‘e-03’ in df and print upto 4 numbers after decimal.
#Input
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])

print("Initial dataframe:\n",df)

# using round to set to 4 digits after decimal
print("\nUpdated dataframe:\n",df.round(4))


#Question 5 (15 Points)
#Create a new column that contains the row number of nearest column by euclidean distance. Create a new column such that, each row contains the row number of nearest row-record by euclidean distance.
#Input
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
#     p   q   r   s
# a  57  77  13  62
# b  68   5  92  24
# c  74  40  18  37
# d  80  17  39  60
# e  93  48  85  33
# f  69  55   8  11
# g  39  23  88  53
# h  63  28  25  61
# i  18   4  73   7
# j  79  12  45  34
#Desired Output

#    p   q   r   s nearest_row   dist
# a  57  77  13  62           i  116.0
# b  68   5  92  24           a  114.0
# c  74  40  18  37           i   91.0
# d  80  17  39  60           i   89.0
# e  93  48  85  33           i   92.0
# f  69  55   8  11           g  100.0
# g  39  23  88  53           f  100.0
# h  63  28  25  61           i   88.0
# i  18   4  73   7           a  116.0
# j  79  12  45  34           a   81.0

print("\nInitial dataframe:\n",df)

# preparing squared differences
diff = df.values[:, np.newaxis, :] - df.values[np.newaxis, :, :]
distMatrix = np.sqrt(np.sum(diff**2, axis=-1))

# Self distance calculation
np.fill_diagonal(distMatrix, np.inf)

# Assigning to the dataframe
df["nearest-row"] = df.index[np.argmin(distMatrix, axis=1)]
df["distance"] = np.round(np.min(distMatrix, axis=1), 0)

print("\nUpdated dataframe:\n",df)

#Question 6 (15 Points)

#Correlation is a statistical technique that shows how two variables are related. Pandas dataframe.corr() method is used for 
#creating the correlation matrix. It is used to find the pairwise correlation of all columns in the dataframe. 
#Any na values are automatically excluded. For any non-numeric data type columns in the dataframe it is ignored.

#Input
data = {'A': [45, 37, 0, 42, 50],
        'B': [38, 31, 1, 26, 90],
        'C': [10, 15, -10, 17, 100],
        'D': [60, 99, 15, 23, 56],
        'E': [76, 98, -0.03, 78, 90]
        }

# DataFrame creation
df = pd.DataFrame(data)

print("Initial dataframe:\n",df)

# Compute pairwise Pearson correlation
correlationMatrix = df.corr()
print("\nCreated correlation matrix\n",correlationMatrix)


