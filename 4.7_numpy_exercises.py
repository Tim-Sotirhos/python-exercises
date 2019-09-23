# import numpy library
import numpy as np

# assign a variable and create an array
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?

negative_numbers = a[a < 0]
negative_numbers
len(negative_numbers)

# How many positive numbers are there?

positive_numbers = a[a > 0]
positive_numbers
len(positive_numbers)

# How many even positive numbers are there?

even_numbers = a[a % 2 ==0]
even_positives = even_numbers[even_numbers > 0]
len(even_positives)

# If you were to add 3 to each data point, how many positive numbers would there be?

add_three = a + 3
add_three_positives = add_three[add_three > 0]
add_three_positives
len(add_three_positives)

# If you squared each number, what would the new mean and standard deviation be?

squared_numbers = a ** 2
squared_numbers
squared_numbers.mean()
squared_numbers.std()

# Adjust the data such that the center of the data is at 0.
# This is done by subtracting the mean from each data point.
# Center the data set.

a
mean_data = a.mean()
center_data = a - mean_data
center_data

# Calculate the z-score for each data point. Recall that the z-score is given by:
standard_deviation_a = a.std()
standard_deviation_a

z_score = (a - mean_data)/standard_deviation_a
z_score

# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = sum(a)
sum_of_a

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)
min_of_a

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)
max_of_a


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum(a) / len(a)
mean_of_a


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product = 1
for i in a:
    product = product * i

product_of_a = product
product_of_a

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = [i**2 for i in a]
squares_of_a

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = [i for i in a if i % 2 == 1]
odds_in_a

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = [i for i in a if i % 2 == 0]
evens_in_a


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
b = np.array(b)
# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_of_b = b.sum()
sum_of_b

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1]) 

min_of_b = b.min()
min_of_b

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = b.max()
max_of_b

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = b.mean()

mean_of_b
# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_of_b = np.prod(b)
product_of_b


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b = np.square(b)

squares_of_b

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = b[b % 2 == 1]
odds_in_b

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

evens_in_b = b[b % 2 == 0]
evens_in_b

# Exercise 9 - print out the shape of the array b.

b.shape

# Exercise 10 - transpose the array b.

b.transpose()

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b.reshape(6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b.reshape(6,1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
c = np.array(c)
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

np.min(c)

# Exercise 2 - Determine the standard deviation of c.

np.std(c)

# Exercise 3 - Determine the variance of c.

np.var(c)

# Exercise 4 - Print out the shape of the array c

c.shape

# Exercise 5 - Transpose c and print out transposed result.

np.transpose(c)
print(np.transpose(c))

# Exercise 6 - Multiply c by the c-Transposed and print the result.

transpose_c = c * np.transpose(c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

np.sum(transpose_c)

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

np.prod(transpose_c)

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)
# Exercise 1 - Find the sine of all the numbers in d

np.sin(d)

# Exercise 2 - Find the cosine of all the numbers in d

np.cos(d)

# Exercise 3 - Find the tangent of all the numbers in d

np.tan(d)

# Exercise 4 - Find all the negative numbers in d

negatives = d[d<0]
negatives

# Exercise 5 - Find all the positive numbers in d

positives = d[d>0]
positives

# Exercise 6 - Return an array of only the unique numbers in d.

unique_numbers = np.unique(d)

# Exercise 7 - Determine how many unique numbers there are in d.

len(unique_numbers)

# Exercise 8 - Print out the shape of d.

d.shape

# Exercise 9 - Transpose and then print out the shape of d.

traspose_d = np.transpose(d)
traspose_d.shape

# Exercise 10 - Reshape d into an array of 9 x 2

d_new_shape = d.reshape(9,2)
d_new_shape.shape
d_new_shape
