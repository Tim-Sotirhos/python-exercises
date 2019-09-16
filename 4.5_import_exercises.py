# 1)Import each function in a different way:

# import the module and refer to the function with the . syntax

import function_exercises

function_exercises.is_two(3)
function_exercises.is_vowel("b")
function_exercises.is_consonant("e")

# use from to import the function directly

from function_exercises import is_two
from function_exercises import is_vowel
from function_exercises import is_consonant

is_vowel("b")

# use from and give the function a different name

import function_exercises as fe

fe.is_two(9)
fe.is_vowel("i")
fe.is_consonant("h")

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

from itertools import product

letters = "abc"
numbers = 1,2,3

result = product(letters, numbers)
for each in result:
    print(each)

# How many different ways can you combine two of the letters from "abcd"?

from itertools import combinations

print(list(combinations("abcd", 2)))

import json

with open("profiles.json", "r") as data:
    profiles = json.load(data)
print(profiles)

print(profiles[0].keys())
print(profiles[0].values())

# Total number of users

users = len(profiles)
print(users)

# Number of active users
count = 0
for profile in profiles:
    if profile["isActive"] == True:
        count += 1
        print(profile["isActive"])
print(count)
# Or

active_users = [profile for profile in profiles if profile["isActive"]]
num_active_users = len(active_users)
num_active_users

# Number of inactive users

inactive_users = [profile for profile in profiles if not profile["isActive"]]
num_inactive_users = len(inactive_users)
num_inactive_users

# Grand total of balances for all users

balance_amount = []
for x in data:
    if x["balance"]
    balance_amount.append(x["balance"])
    print(sum(balance_amount))

balance = [xsum(x["balance"])]
    

# Average balance per user

profile["balance"] for profile in profiles]

def handle_balance(s):
    return float(s[1:].replace(',', ""))

balances = [handle_balance(profile['balance']) for profile in profiles]

sum(balances)

# User with the lowest balance

user_with_the_lowest_balance = profiles[0]

for user in profiles[1:]:
    if handle_balance(user['balance']) < handle_balance(user_with_the_lowest_balance['balance']):
        user_with_the_lowest_balance = user

user_with_the_lowest_balance

# User with the highest balance

user_with_the_highest_balance = profiles[0]

for user in profiles[1:]:
    if handle_balance(user['balance']) > handle_balance(user_with_the_highest_balance['balance']):
        user_with_the_highest_balance = user

user_with_the_highest_balance

# Most common favorite fruit

from collections import Counter
Counter([profile['favoriteFruit'] for profile in profiles])

# Least most common favorite fruit

fruit_counts = {}
for profile in profiles:
    fruit = profile['favoriteFruit']
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1

fruit_counts.items()

# Total number of unread messages for all users

greetings = [profile['greeting'] for profile in profiles]

def extract_digits(s):
    return int(''.join([c for c in s if c.isdigit()]))

[extract_digits(greeting) for greeting in greetings]

n_unread_messages = [extract_digits(greeting) for greeting in greetings]

sum(n_unread_messages)