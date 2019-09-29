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

# 1.e) Determine the most frequently occurring fruit name from the series.

most_frequent = unique_fruits.idxmax()
most_frequent

# 1.f) Determine the least frequently occurring fruit name from the series.

least_frequent = fruits.value_counts().min()
unique_fruits
unique_fruits[unique_fruits == least_frequent]

# 1.g) Write the code to get the longest string from the fruits series.

fruit_names = fruits.unique()
fruit_names_series = pd.Series(fruit_names)
length_of_string = fruit_names_series.str.len().max()
index_of_string = fruit_names_series.str.len().idxmax()
longest_string = fruits[index_of_string]

# 1.h) Find the fruit(s) with 5 or more letters in the name.

five_or_more_letters = fruits.apply(lambda x: len(x) >= 5)
fruits[five_or_more_letters]

# 1.i) Capitalize all the fruit strings in the series.

fruits.str.capitalize()

# 1.j) Count the letter "a" in all the fruits (use string vectorization)

count_letter_a = fruits.str.count('a')
list(zip(fruit_names,count_letter_a))

# 1.k) Output the number of vowels in each and every fruit.

sum(fruits.str.count('a|e|i|o|u'))

# 1.l) Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

fruits[fruits.apply(lambda x: x.count('o') >= 2)]

# 1.m) Write the code to get only the fruits containing "berry" in the name

fruits[fruits.str.contains('berry')]

# 1.n) Write the code to get only the fruits containing "apple" in the name

fruits[fruits.str.contains('apple')]

# 1.o) Which fruit has the highest amount of vowels?

fruits[fruits.str.count('a|e|i|o|u').idxmax()]

# 2.) Use pandas to create a Series from the following data:

dollars = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

# 2.a) What is the data type of the series?

type(dollars[0])

# 2.b) Use series operations to convert the series to a numeric data type.

no_special_character = dollars.str.replace("$", "").str.replace(',', "")

dollars = no_special_character.astype('float')

# 2.c) What is the maximum value? The minimum?

max_value = dollars.max()
min_value = dollars.min()

# 2.d) Bin the data into 4 equally sized intervals and show how many values fall into each bin.

sort_values = dollars.sort_values()
bins = pd.cut(sort_values, 4)

# 2.e) Plot a histogram of the data. Be sure to include a title and axis labels.

dollars.plot.hist(color = 'firebrick')
plt.title('Histogram of Values')
plt.xlabel('Dollar Values')
plt.ylabel('Frequency')

# 3) Use pandas to create a Series from the following exam scores:

scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# 3. a) What is the minimum exam score? The max, mean, median?

scores.describe()

min_score = scores.min()

max_score = scores.max()

mean_score = scores.mean()

median_score = scores.median()

# 3.b) Plot a histogram of the scores.

scores.plot.hist(color = 'firebrick')
plt.title('Histogram of Scores')
plt.xlabel('Scores')
plt.ylabel('Frequency')

# 3.c) Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.

scores.apply(lambda x: 'A' if x > 89 else ('B' if x > 79 else ('C' if x > 69 else ('D' if x > 59 else 'F'))))

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

# 2.)Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

mpg = data('mpg')
data('mpg', show_doc=True)

# 2.a) How many rows and columns are there?

mpg.shape
# 234 rows and 11 columns/variables

# 2.b) What are the data types of each column?

mpg.dtypes

# 2.c) Summarize the dataframe with .info and .describe

mpg.info()
mpg.describe()

# 2.d) Rename the cty column to city.

mpg.rename(columns={'cty': "city"}, inplace=True)

# 2.e) Rename the hwy column to highway.

mpg.rename(columns={'hwy': "highway"}, inplace = True)

#2.f) Do any cars have better city mileage than highway mileage?
mpg
def better_city(arg):
    return mpg.city > mpg.highway

better_city(mpg)
mpg[better_city(mpg)]

#REVIEW
better_mileage = mpg['city']> mpg["highway"]
mpg[better_mileage]

# 2.g) Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.

mileage_diff = mpg.assign(mileage_difference = mpg.highway - mpg.city)
mpg
type(mileage_diff)

#REVIEW
mpg['mileage_difference'] = mpg.highway-mpg.city
mpg
# 2.h) Which car (or cars) has the highest mileage difference?

mileage_diff.sort_values(by = 'mileage_difference', ascending = False).head(2)

#REVIEW
mpg.sort_values(by = 'mileage_difference',ascending= False).head()
mpg
# 2.i) Which compact class car has the lowest highway mileage? The best?

best_compact_highway = mpg.sort_values(["highway", "class"], ascending = [False, True]).head(1)
best_compact_highway

worst_compact_highway = mpg.sort_values(["highway", "class"]), ascending = [True, True]
worst_compact_highway


#REVIEW
print(mpg[mpg['class'] == 'compact'].sort_values(by="highway", ascending=True).head(1))
print(mpg[mpg['class'] == 'compact'].sort_values(by="highway",ascending=True).tail(1))

# 2.j) Create a column named average_mileage that is the mean of the city and highway mileage.

mpg["average_mileage"] = (mpg.city + mpg.highway)/2
mpg

#REVIEW
mpg['average_mileage']= mpg[['highway','city']].apply(np.mean,axis=1)
mpg
# 2.k) Which dodge car has the best average mileage? The worst?

mpg[mpg['manufacturer'] == 'dodge'].sort_values(by='average_mileage', ascending=False).head(1)
mpg[mpg['manufacturer'] == 'dodge'].sort_values(by='average_mileage', ascending=False).tail(1)

# 3.)Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

mammals=data('Mammals')
data('Mammals',show_doc = True)
mammals.head()
mammals

# 3.a) How many rows and columns are there?

mammals.shape

# 3.b) What are the data types?

mammals.dtypes

# 3.c) Summarize the dataframe with .info and .describe

mammals.info()
mammals.describe()

# 3.d) What is the the weight of the fastest animal?

mammals[['weight','speed']].sort_values(by='speed', ascending = False).head(1)

# 3.e) What is the overal percentage of specials?

sum(mammals.specials == True)/len(mammals) * 100
(mammals.specials == True).mean()*100

# 3.f) How many animals are hoppers that are above the median speed? What percentage is this?

num_animals = sum((mammals.hoppers == True) & (mammals.speed > mammals.speed.median()))
print(num_animals)
print(round(num_animals/len(mammals)*100,2))