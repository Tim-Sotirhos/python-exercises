# Function Exercises

# 1) Define a function named is_two. 
# It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(arg):
    if arg == 2 or arg == '2':
        return True

# or 
    return arg in [2, '2', 'two']

# 2) Define a function named is_vowel. 
# It should return True if the passed string is a vowel, 
# False otherwise.

def is_vowel(arg):
    if len(arg) > 1:
        return False
    arg = arg.lower()
    if arg in ["a","e","i","o","u"]:
        return True

# 3) Define a function named is_consonant.
# It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(arg):
    if is_vowel(arg) == False:
        return True

# 4) Define a function that accepts a string that is a word.
# The function should capitalize the first letter of the word if the word starts with a consonant.

def upper_first_letter(arg):
    if is_consonant(arg[0]) == True:
        return arg.capitalize()
    else:
        return arg

# Or
def upper__first__letter(arg):
    return arg.capitalize() if is_consonant(arg[0]) else arg

# 5) Define a function named calculate_tip.
# It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip, bill):
    tip = type(float)
    return (bill * tip)

calculate_tip(.2,100)

# Or
def calculate__tip(percent_tip, bill_amount):
    amount_to_tip = percent_tip * bill_amount
    return amount_to_tip

calculate__tip(.2, 100)

# 6) Define a function named apply_discount.
# It should accept an original price, 
# and a discount percentage, 
# and return the price after the discount is applied.

def apply_discount(original_price, discount_percentage):
    if discount_percentage > 0 and discount_percentage < 1:
        return original_price * (1 - discount_percentage)

# Or
def apply__discount(original_price, discount_percentage):    
    discount_amount = original_price * discount_percentage
    return original_price - discount_amount

apply__discount(100, .3)

# 7) Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, 
# and return a number as output.

def handle_commas(number):
    return float(number.replace(",", ""))

# 8) Define a function named get_letter_grade. 
# It should accept a number and 
# return the letter grade associated with that number (A-F).

def get_letter_grade(grade):
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade <= 89:
        return "B"
    elif 70 <= grade <= 79:
        return "C"
    elif 60 <= grade <= 69:
        return "D"
    else:
        return "F"

# Or
grades = {
    'A': range(94, 101),
    'B': range(87, 94),
    'C': range(80, 87),
    'D': range(70, 80),
    'F': range(0, 70),
}
def get_letter_grade(n):
    for grade_letter, grade_range in grades.items():
        if round(n) in grade_range:
            return grade_letter
    return "error: don't know how to get a letter grade for %s" % n
get_letter_grade(80)

# 9) Define a function named remove_vowels 
# that accepts a string and 
# returns a string with all the vowels removed.

def remove_vowels(word):
    no_vowel = ""
    for x in word.lower():
        if x in "a,e,i,o,u":
            no_vowel = word.replace(x,"")
    return no_vowel

# 10) Define a function named normalize_name. 
# It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores

def normalize_name(arg):
    arg = str(arg).lower().strip().replace(" ", "_")
    return "".join(e for e in arg if e.isalnum())
normalize_name("first name")
 
# Or
def remove_special_characters(arg):
    return ''.join([c for c in arg if c.isalpha() or c == ' '])
def normalize_name(arg):
    return remove_special_characters(arg).lower().strip().replace(' ', '_')
normalize_name(" % Completed")

#1 11) Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
cumsum([1, 1, 1]) returns [1, 2, 3]
cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumsum(arg):
    new_list = []
    cumsum = 0
    for a in arg:
        new_list.append(a + cumsum)
        cumsum += a
    return new_list
    
cumsum([1,2,3,4])