# Pandas Exercises

import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import numpy as np


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

fruits.str.len().idxmax()
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

sum(fruits.str.count('a|e|i|o|u'))

# REVIEW    

def count_vowels(word):
    vowels = 'aeiou'
    count = 0
    for letter in word.lower():
        count += letter in vowels
    return count

sum(fruits.apply(count_vowels))

# 1.l) Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

has_an_o = (lambda x: x.count("o"))
fruits.apply(has_an_o)

# REVIEW
fruits[fruits.apply(lambda x: x.count('o') >= 2)]

# 1.m) Write the code to get only the fruits containing "berry" in the name

fruits.str.count('berry')

# REVIEW
fruits[fruits.apply(lambda x: 'berry" in x)]
fruits.str.contains("berry")
fruits[fruits.str.contains("berry")]

# 1.n) Write the code to get only the fruits containing "apple" in the name

fruits.str.count('apple')

# REVIEW
fruits[fruits.apply(lambda x: 'apple" in x)]

# 1.o) Which fruit has the highest amount of vowels?

print(fruits.str.count('a|e|i|o|u').idxmax())
fruits[5]

# REVIEW

fruits[fruits.apply(count_vowels.idxmax())]

# 2.) Use pandas to create a Series from the following data:

dollars = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

# 2.a) What is the data type of the series?

type(dollars[0])

# 2.b) Use series operations to convert the series to a numeric data type.

unsigned = dollars.str.replace("$", "")
no_commas_unsigned = unsigned.str.replace(",", "")
no_commas_unsigned

dollars = no_commas_unsigned.astype('float')
dollars

# 2.c) What is the maximum value? The minimum?

min_value = dollars.min()
min_value

max_value = dollars.max()
max_value

# 2.d) Bin the data into 4 equally sized intervals and show how many values fall into each bin.

bins = pd.cut(dollars, 4)
bins

# 2.e) Plot a histogram of the data. Be sure to include a title and axis labels.

dollars.plot.hist(color = 'firebrick')
plt.title('Histogram')
plt.xlabel('Dollar Values')
plt.ylabel('Frequency')

# 3) Use pandas to create a Series from the following exam scores:

scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# 3. a) What is the minimum exam score? The max, mean, median?

scores.sort_values()
scores.count()

min_score = scores.min()
min_score

max_score = scores.max()
max_score

mean_score = scores.mean()
mean_score

median_score = scores.median()
median_score

# 3.b) Plot a histogram of the scores.

scores.plot.hist(color = 'firebrick')

# 3.c) Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.

def letter_grades(x):
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    elif x >= 70:
        return "C"
    elif x >= 60:
        return "D"
    else:
        return "F"

scores.apply(letter_grades)

# 3.d) Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.

highest_grade = max_score
curve = 100 - max_score
curve_grades = (lambda x: x + curve)
scores.apply(curve_grades)

# 4.) Use pandas to create a Series from the following string:

# 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'

string = ("hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy")
def split(word):
    return [c for c in word]
        
new_list = split(string)
type(new_list)
string_series = pd.Series(new_list)
type(string_series)
string_series

# 4.a) What is the most frequently occuring letter? Least frequently occuring?

string_series.value_counts().idxmax()

most_frequent_letter = string_series.value_counts().idxmax()
print(most_frequent_letter)

least_frequent_letter = string_series.value_counts().idxmin()
print(least_frequent_letter)

# 4.b) How many vowels are in the list?

def vowel(arg):
    vowels = 'aeiou'
    count = 0  
    for c in arg:
        count += c in vowels
    return count

# REVIEW

def count_vowels(word):
    vowels = 'aeiou'
    count = 0
    for letter in word.lower():
        count += letter in vowels
    return count

# REVIEW
sum(string_series.str.count('a|e|i|o|u'))

# REVIEW
sum(string_series.apply(count_vowels))

# 4.c) How many consonants are in the list?

string_series.count() - sum(string_series.apply(count_vowels))

# 4.c) Create a series that has all of the same letters, but uppercased

string_series.str.upper()

# 4.d) Create a bar plot of the frequencies of the 6 most frequently occuring letters.

string_series.value_counts().head(6).plot.bar(title = "Six Most Popular Letters")
plt.xlabel("letters")
plt.ylabel("frequency")

# Pandas Dataframes Exercies

# 1.) Copy the code from the lesson to create a dataframe full of student grades.

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})


type(df)

# 1.a) Create a column named passing_english that indicates whether each student has a passing grade in reading.

df.english >= 70
passing_english = df['passing_english'] = df.english > 70
df

# 1.b) Sort the english grades by the passing_english column. How are duplicates handled?

df.sort_values(by='passing_english')
# Duplicates are handled by listing them in descending order by name.

# 1.c) Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first,
# and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. 
# (Hint: you can pass a list to the .sort_values method)

sort_name_passing_english = df.sort_values(by=['passing_english', 'name'])
sort_name_passing_english

# 1.d) Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.

sort_passing_english_grade = df.sort_values(by=['passing_english', 'english'])
sort_passing_english_grade

# 1.e) Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

overall_grade = df['overall_grade'] = (df.math + df.english + df.reading) / 3
overall_grade
df