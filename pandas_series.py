# Pandas Exercises

import pandas as pd

# 1.) Use pandas to create a Series from the following data:

#1.a) Name the variable that holds the series fruits.

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

#1.b) Run .describe() on the series to see what describe returns for a series of strings.

fruits.describe()

# 1.c) Run the code necessary to produce only the unique fruit names.

fruits.unique()

# 1.d) Determine how many times each value occurs in the series.

unique_fruits = fruits.value_counts()
unique_fruits

# REVIEW
frequencies = fruits.value_counts()


# 1.e) Determine the most frequently occurring fruit name from the series.

most_frequent = unique_fruits.index[0]
most_frequent

# REVIEW
most_frequent_fruit = frequencies.max()
fruit = frequencies.idxmax()
print("most frequent furit is", fruit, "it has", most_frequent_fruit, 'occurances')


# 1.f) Determine the least frequently occurring fruit name from the series.

fruits.min()

# REVIEW
fruits.value_counts()[fruits.value_counts() == least_frequent]

least_frequent = fruits.value_counts().min()
frequencies = fruits.value_counts()
frequencies[frequencies == least_frequent]

# 1.g) Write the code to get the longest string from the fruits series.

fruits.str.len()
fruits[5]

# REVIEW
fruit_names = fruits.unique()
fruit_names = pd.Series(fruit_names)
length_of_string = fruit_names.str.len().max()
index_of_string = fruit_names.str.len().idxmax()
longest_string = fruit_names[index_of_string]
print("the longest string is", longest_string, "and it has", length_of_string, "letters")

# 1.h) Find the fruit(s) with 5 or more letters in the name.

five_or_more_letters = fruits.apply(lambda x: len(x) >= 5)
fruits[five_or_more_letters]

# 1.i) Capitalize all the fruit strings in the series.

fruits.str.capitalize()

# 1.j) Count the letter "a" in all the fruits (use string vectorization)

fruits.str.count('a')

# REVIEW
counts_of_a = fruit_names.str.count('a') # not good enough
list(zip(fruit_names, counts_of_a))



# 1.k) Output the number of vowels in each and every fruit.

fruits.str.count('a|e|i|o|u')

# 1.l) Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

has_an_o = (lambda x: x.count("o"))
fruits.apply(has_an_o)

# 1.m) Write the code to get only the fruits containing "berry" in the name

fruits.str.count('berry')

# 1.n) Write the code to get only the fruits containing "apple" in the name

fruits.str.count('apple')


# 1.o) Which fruit has the highest amount of vowels?

fruits.str.count('a|e|i|o|u')
fruits[5]


# 2.) Use pandas to create a Series from the following data:

dollars = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

# 2.a) What is the data type of the series?

type(dollars[0])

# 2.b) Use series operations to convert the series to a numeric data type.

unsigned = dollars.str.replace("$", "")
no_commas_unsigned = unsigned.str.replace(",", "")
no_commas_unsigned

no_commas_unsigned.astype('float')
no_commas_unsigned

dollars.str.replace("$", "").str.replace(",", "")
dollars

# 2.c) What is the maximum value? The minimum?



# 2.d) Bin the data into 4 equally sized intervals and show how many values fall into each bin.



# 2.e) Plot a histogram of the data. Be sure to include a title and axis labels.



# 3) Use pandas to create a Series from the following exam scores:

scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# 3. a) What is the minimum exam score? The max, mean, median?



# 3.b) Plot a histogram of the scores.



# 3.c) Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.



# 3.d) Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.
