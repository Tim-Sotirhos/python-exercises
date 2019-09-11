# What data type would best represent:

type(99.9) # Float
type("False") # Str
type(False) # Bool
type('0') # Str
type(0) # Int
type(True) # Bool
type('True') # Str
type([{}]) # List
type({'a':[]}) # Dict

# What data type would best represent:

# A term or phrase typed into a search box?

String

# If a user is logged in?

Boolean

# A discount amount to apply to a user's shopping cart?

Float

# Whether or not a coupon code is valid?

Boolean

# An email address typed into a registration form?

String

# The price of a product?

Integer

# A Matrix?

Dictionary 

# The email addresses collected from a registration form?

List

# Information about applicants to Codeup's data science program?

Dictionary

#For each of the following code blocks, 
# read the expression and predict what the result of evaluating it would be, 
# then execute the expression in your Python REPL.


'1' + 2
# predict error because adding 2 diff data types

6 % 4
# predict remainder 2

type(6 % 4)
# predict integer

type(type(6 % 4))
# predict type or integer

'3 + 4 is ' + 3 + 4
# predict error diff data types

0 < 0
# predict True

'False' == False
# predict False one is a bool the other is a string

True == 'True'
# predict False one is a bool the other is a string

5 >= -5
# predict True

True or "42"
# predict True because of the True OR

!True && !False
# predict error command not found

6 % 55 < 4 and 1 == 1
# predict False both conditions are not True or False

'codeup' == 'codeup' and 'codeup' == 'Codeup'
# predict False because of the last capital??

4 >= 0 and 1 !== '1'
# predict error because of extra equal sign operator on 2nd condition

6 % 3 == 0
# predict True

5 % 2 != 0
# predict True

[1] + 2
# predict error

[1] + [2]
# predict new list with [1, 2]

[1] * 2
# predict list to be multiply by 2

[1] * [2]
# predict error

[] + [] == []
# predict True 

{} + {}
# predict error ??

# The little mermaid (for 3 days), Brother Bear (for 5 days, they love it),
#  and Hercules (1 day, you don't know yet if they're going to like it).
# If price for a movie per day is 3 dollars, how much will you have to pay?

daily_rental_rate = 3
# Movies
little_mermaid_days = 3
brother_bear_days = 5
hercules_days = 1

total_rental_cost = (little_mermaid_days + brother_bear_days + hercules_days) * daily_rental_rate

print(total_rental_cost)

# Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google = 400
amazon = 380
facebook = 350
hours_worked_google = 10
hours_worked_amazon = 4
hours_worked_facebook = 6

total_compensation = (google*hours_worked_google)+(amazon*hours_worked_amazon)+(facebook*hours_worked_facebook)

print(total_compensation)

# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

available_seats = 1
schedule_conflict = False
if available_seats > 0 and schedule_conflict == False:
    allowed_to_enroll = True
else:
    allowed_to_enroll = False
print(allowed_to_enroll)

# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a specific amount of products.

num_of_items = 2
offer_expired = False
premium_member = True

if premium_member == True or (num_of_items > 2 and offer_expired == False):
    product_discounted = True
else:
    product_discounted = False

print(product_discounted)

# Use the following code to follow the instructions below:
username = 'codeup'
password = 'notastrongpassword'

# the password must be at least 5 characters

password_character_requirement = len(password) > 5
print(password_character_requirement)

# the username must be no more than 20 characters

password_max_character = len(password) <= 20
print(password_max_character)

# the password must not be the same as the username

password_cannot_be_username = password != username
print(password_cannot_be_username)

# bonus neither the username or password can start or end with whitespace

no_leading_or_ending_whitespace = username[0] != ' ' and username[-1] != ' ' and password[0] != ' ' and password[-1] != ' '
print(no_leading_or_ending_whitespace)