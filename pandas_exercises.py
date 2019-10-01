import pandas as pd
from pydataset import data
import numpy as np

mpg = data('mpg')
data('mpg', show_doc=True)
mpg

# 1) Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:

# 1.a) On average, which manufacturer has the best miles per gallon?

best_average_mileage = mpg['average_mpg'] = (mpg.cty + mpg.hwy)/2
mpg
mpg.groupby('manufacturer').average_mpg.agg('mean').sort_values(ascending = False).head(1)

# 1.b) How many different manufacturers are there?

len(mpg[['manufacturer']].groupby('manufacturer').agg('count'))
len(mpg.manufacturer.unique())

# 1.c) How many different models are there?

len(mpg[['model']].groupby('model').agg('count'))
len(mpg.model.unique())

# 1.d) Do automatic or manual cars have better miles per gallon?

automatic = mpg[mpg.trans.str.contains('auto')]
manual = mpg[mpg.trans.str.contains('manual')]
auto_avg_mpg = automatic.mean()
manual_avg_mpg = manual.mean()

# 2.) Joining and Merging

'''
Copy the users and roles dataframes from the examples above. 
What do you think a right join would look like? An outer join? 
What happens if you drop the foreign keys from the dataframes and try to merge them?
'''

# Copy the users and roles dataframes. 
# What do you think a right join would look like? 
# An outer join? What happens if you drop the foreign keys from the dataframes and try to merge them?

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

# Copy Roles Dataframe
roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

# Merge Left

pd.merge(
    users.rename(columns={'id': 'user_id', 'name': 'username'}),
    roles.rename(columns={'name': 'role_name'}),
    left_on="role_id", right_on="id", how="left")

# Merge Right

pd.merge(
    users.rename(columns={"id": "user_id", "name": "user_name"}),
    roles.rename(columns={"name": "role_name"}),
    left_on = "role_id", right_on = "id", how="right")

# Merge Inner

pd.merge(
    users.rename(columns={"id": 'user_id', 'name': 'user_name'}),
    roles.rename(columns={"name": 'role_name'}),
    left_on="role_id", right_on="id", how='inner')

# Merge Outer

pd.merge(
    users.rename(columns={"id": 'user_id', 'name': 'user_name'}),
    roles.rename(columns={"name": 'role_name'}),
    left_on="role_id", right_on="id", how='outer')

# 3.) Getting data from SQL databases

# 3.a ) Create a function named get_db_url. 
# It should accept a username, hostname, password, and database name and return a url formatted like in the examples in this lesson.

import pandas as pd

def get_db_url(user, password, host, database_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    return url

from env import host, user, password

url = get_db_url(user,password, host, "employees")
url

# 3.b ) Use your function to obtain a connection to the employees database.

employees_df = pd.read_sql('SELECT * FROM employees', url)

# 3.c) Once you have successfully run a query:

employees_df.head(25)

# 3.d) Intentionally make a typo in the database url. What kind of error message do you see?

'''
OperationalError:
'''

# 3.e) Intentionally make an error in your SQL query. What does the error message look like?

'''
ProgrammingError:
'''

# 3.f) Read the employees and titles tables into two separate dataframes

employees_df

titles_df = pd.read_sql('SELECT * FROM titles', url)
titles_df
titles_df.head(25)

# 3.g) Visualize the number of employees with each title.
current_titles = pd.read_sql('SELECT title, count(title) FROM titles WHERE to_date = "9999-01-01" group by title', url)

current_titles = titles_df.groupby("title").count()
current_titles = current_titles.reset_index()
current_titles.plot(x ='title', y='emp_no', kind = 'bar')

# 3.h) Join the employees and titles dataframes together.

employees_titles = pd.merge(employees_df, titles_df, left_on="emp_no", right_on="emp_no",how='left')
employees_titles.head()

# 3.i) Visualize how frequently employees change titles.

# Groupby emp_no and count number of titles
new_df = employees_titles.groupby('emp_no').count()
new_df.head()

# Reset datafram index
new_df = new_df.reset_index()
new_df.head()

# Multi column dataframe
new_df = new_df[["title", "emp_no"]]
new_df.head()

# Count number of times titles have changed
titles_count = new_df.groupby('title').count()
titles_count = titles_count.reset_index()

# Visualization
new_df.plot(x = 'title', y = 'emp_no', kind = 'bar')

# 3.j) For each title, find the hire date of the employee that was hired most recently with that title.

employees_titles.groupby('title').hire_date.max()

# 3.k) Write the code necessary to create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL and python/pandas code)

department_titiles = pd.read_sql('SELECT * FROM departments JOIN dept_emp using(dept_no) JOIN titles using(emp_no) WHERE titles.to_date > now() and dept_emp.to_date > now()',url)
department_titiles.head()

# Crosstab of titles per department
number_of_titles = pd.crosstab(department_titiles.title, department_titiles.dept_name)

# 4.) Use your get_db_url function to help you explore the data from the chipotle database. Use the data to answer the following questions:

import pandas as pd

def get_db_url(user, password, host, database_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    return url

from env import host, user, password

url = get_db_url(user,password, host, "chipotle")
url

chipotle_df = pd.read_sql('SELECT * FROM orders', url)


# 4.a) What is the total price for each order?

chipotle_df['price'] = chipotle_df['item_price'].str.replace('$',' ').str.strip().str.replace(',','_').astype(float)
chipotle_df.groupby('order_id')['price'].sum()

# 4.b) What are the most popular 3 items?

chipotle_df.groupby('item_name')["price"].count().sort_values().tail(3)

# 4.c) Which item has produced the most revenue?

chipotle_df.groupby('item_name')['price'].sum().idxmax()