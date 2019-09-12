# Function Exercises

# 1) Define a function named is_two. 
# It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(arg):
    if arg == 2:
        return True
    else:
        return False

# 2) Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(x):
    if x in ["a","e","i","o","u"]:
        return True
    else:
        return False


# 3) Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(x):
    if is_vowel(x) == False:
        return True
    else:
        return False

is_consonant("apple")

# 4) Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def upper_first_letter(x):
    if is_consonant(x[0]) == True:
        return x.capitalize()
    else:
        return x

# 5) Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.