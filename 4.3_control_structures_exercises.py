# Conditional Basics
# a. prompt the user for a day of the week, print out whether the day is Monday or not.

is_it_monday = input("What is the day of the week? ")

if is_it_monday in ["monday", "Monday"]:
    print("Today is Monday")
else:
    print("Sorry maybe tomorrow")

# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend.

is_it_a_weekend = input("What day is it? ")

if is_it_a_weekend == "Saturday" or is_it_a_weekend == "saturday":
    print("It's a weekend!")
elif is_it_a_weekend == "Sunday" or is_it_a_weekend == "sunday":
    print("It's a weekend!")
else:
    print("Maybe soon it will be a weekend")

# Or

is_weekend = input("Enter a day of the week: ")

if is_weekend.lower() == "saturday" or is_weekend.lower() == "sunday":
    print(f'Correct today is a weekend')
else:
    print(f'Sorry too bad')
    
# c. create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

number_of_hours_worked = 36
hourly_rate = 15
total_weekly_pay = number_of_hours_worked * hourly_rate
print(total_weekly_pay)

def weekly_pay(hours, rate):
    if hours < 40:
        return hours * rate
    if hours > 40:
        return (hours - 40) * .5 * rate + (hours * rate)
        
print(weekly_pay(41,15))

# Or

hours = 41
rate = 20

if hours < 41:
    paycheck = hours * rate
    print(paycheck)
else:
    paycheck = (hours - 40) * 1.5 * rate + 40 * rate
    print(paycheck)

# Loop Basics

# A. While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1

#Create a while loop that will count by 2's starting with 0 and ending at 100.
# Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.

i = 2
while i <= 100_000_000:
    print(i)
    i += i**2

# Write a loop that uses print to create the output shown below.

i = 100
while i >= 5:
    print(i)
    i += -5

# B. For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

number = input("Enter a number 1 through 10: ")

number = int(number)

for i in range(1,11):
    print(str(i) + "*" + str(number) + "=" + str(i * number))

# Create a for loop that uses print to create the output shown below.

for number in range(1,10):
    print(str(number) * number)

# C. break and continue

# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input.
# (Hint: use the isdigit method on strings to determine this).
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.

while True:
    numb = input("Enter an odd number between 1 and 50: ")
    print("\n")
    
    if numb.isdigit() and int(numb) % 2 == 1 and int(numb) < 50:
       break

print("Number to skip is: " + str(numb))
print("\n")

for num in range(1, 50, 2):
    if num == int(numb):
        print("Nope! Skipping number: " + str(numb))
        continue
    print("Here is an odd number: " + str(num))

# D. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, 
# so you'll need to convert this to a numeric type.)

number = input("Enter a positive number: ")

if number.isdigit() == False or int(number) < 0:
    print("Not a positive number, try again")
else:
    number = int(number)
    for i in range(0, number + 1):
        print(i)

# Or

while True:
    pos_num = input("Enter a positive number: ")
    if pos_num.isdigit() and int(pos_num) > 0:
        break

for num in range(0, int(pos_num) + 1):
    print(num)

# E. Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.

number = input("Enter a positive number: ")

if number.isdigit() == False or int(number) < 0:
    print("Not a positive number, try again")
else:
    number = int(number)
    for i in range(number,0,-1):
        print(i)

# Or

while True:
    pos_num = input("Enter a positive number: ")
    if pos_num.isdigit() and int(pos_num) > 0:
        break

for num in range(int(pos_num), 0, -1):
    print(num)

# Fizzbuzz

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# 4) Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

make_a_powers_table = True

while make_a_powers_table:
    powers = input("Enter an integer: ")
    print("\n")
    print(f'Here is your table!')
    print("\n")
    print("number | squared | cubed")
    print("-" * 6 + " | " + "-" * 7 + " | " + "-" * 5)
    for num in range(1, int(powers) + 1):
        print(str(num) + " " * 6 + "| ", end="")
        print(str(num**2) + " " * 6 + " |", end="")
        print(" "+str(num**3))
    make_a_powers_table = input("Would you like to continue? (Y/N)") == "Y"

# Or

make_a_table = True

while make_a_table:
    number = int(input("Enter an interger: "))
    print("\n")
    print("Here is your table!")
    print("\n")
    print("number | squared | cubed")
    print("______ | _______ | ______")
    for i in range(1,number+1):
        first = str(i)
        square = str(i ** 2)
        cube = str(i ** 3)
        print(first + " " * (7-len(first)) + "| ", end="")
        print(square + " " * (8-len(square)) + "| ", end="")
        print(cube)
    make_a_table = input("Would you like to continue? (Y/N)") == "Y"

# 5) Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

grades = True

while grades:
    grade = input("Enter a numerical grade from 0 to 100: ")
    grade = int(grade)

    if grade >= 88:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 67:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")
    grades = input(f'Would you like to enter another grade? ("Y/N"):') == "Y"

# 6) Create a list of dictionaries where each dictionary represents a book that you have read.
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.
# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

books = [{"title": "As A Man Thinketh", "author": "James Allen", "genre": "Self Reflect"},
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "genre": "Financial"},
    {"title": "The Richest Man in Babylon", "author": "George S. Clason", "genre": "Historical"}]

for book in books:
    print("title: {}".format(book["title"]))


genre = input("Which Genre? ")
for book in books:
    if book["genre"] == genre:
        print(book["title"])

