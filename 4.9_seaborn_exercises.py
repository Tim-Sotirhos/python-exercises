# Seaborn Exercises

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
from pydataset import data

# A) Use the iris database to answer the following quesitons:

iris = data('iris')
iris.sample()

iris.rename(columns = {"Sepal.Length": "Sepal_Length", "Sepal.Width": "Sepal_Width", "Petal.Length": "Petal_Length", "Petal.Width": "Petal_Width"}, inplace = True)

# B) What does the distribution of petal lengths look like?

sns.distplot(iris.Petal_Length)

# C) Is there a correlation between petal length and petal width?

sns.heatmap(iris.corr(), annot = True, cmap = 'OrRd')

sns.relplot(data = iris, x = "Petal_Length", y = "Petal_Width")

# D) Would it be reasonable to predict species based on sepal width and sepal length?

iris.head()
sns.relplot(data = iris, x = "Sepal_Width", y = "Sepal_Length", hue = "Species")
plt.title('Species by Septal')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

# E) Which features would be best used to predict species?

sns.relplot(data = iris, x = "Petal_Length", y = "Petal_Width", hue = "Species")
plt.title('Species by Petal')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

sns.pairplot(data = iris, hue = 'Species')

# 1.) Use seaborn's load_dataset function to load the anscombe data set. 
# Use pandas to group the data by the dataset column, 
# and calculate summary statistics for each dataset. What do you notice?

dataset = sns.load_dataset('anscombe')
dataset.tail()
dataset['dataset'].value_counts()

dataset.groupby(['dataset']).agg(['mean', 'max', 'min'])
dataset.groupby(['dataset']).describe()

sns.relplot(data = anscombe, x = 'x', y = 'y')

'''
I notice more variation with the "y" variable.
'''

# 2.)Load the InsectSprays dataset and read it's documentation. 
# Create a boxplot that shows the effectiveness of the different insect sprays.

data('InsectSprays', show_doc = True)
insect = data('InsectSprays')
insect.describe()
insect.info()
insect.sort_bvalue_counts('spray')
insect.groupby("spray").count()

sns.boxplot(data = insect, y = "count", x = "spray")

# 3.) Load the swiss dataset and read it's documentation. 
# Create visualizations to answer the following questions:

swiss = data('swiss')
data('swiss', show_doc = True)
swiss.describe()
swiss.sort_values('Catholic')

# 3.a) Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. (Choose a cutoff point for what constitutes catholic)

swiss.Catholic.median()
swiss['is_catholic'] = swiss.Catholic > 37
swiss.index

corr = swiss.corr()

sns.boxplot(data = swiss, y = 'Fertility', x = 'is_catholic')

# 3.b) Does whether or not a province is Catholic influence fertility?

sns.heatmap(swiss.corr(), annot=True, cmap='OrRd')

'''
No, a Catholic province does not influence fertility.
'''

#3.c) What measure correlates most strongly with fertility?

'''
Education has the strongest correlation with fertility.
'''

# 4.) Using the chipotle dataset from the previous exercise, 
# create a bar chart that shows the 4 most popular items and the revenue produced by each.

def get_db_url(user, password, host, database_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{database_name}'
    return url

from env import host, user, password

url = get_db_url(user,password, host, "chipotle")
url

chipotle_df = pd.read_sql('SELECT * FROM orders', url)
chipotle_df.head()

chipotle_df['price'] = chipotle_df['item_price'].str.replace('$',' ').str.strip().str.replace(',','_').astype(float)

# Sort top 4 items sold
top_four_items = chipotle_df.groupby('item_name')["price"].count().sort_values().tail(4)

# Sort top 4 items' revenue
top_four_revenue = chipotle_df.groupby('item_name')['price'].sum().sort_values().tail(4)
type(top_four_revenue)

# Create empty dataframe
bar_graph = pd.DataFrame()
type(bar_graph)

# add index and values
bar_graph['top_items'] = top_four_items.index
bar_graph['top_revenue'] = top_four_revenue.values
print(bar_graph)

sns.barplot(x="top_items", y="top_revenue", data=bar_graph)

# Submitted after review on 10/02/19 "better way to solve chipotle"
orders.item_price = orders.item_price.str.replace('$', '').astype('float')

four_most_popular = (orders.groupby('item_name')
 .sum()
 .drop(columns='order_id')
 .rename(columns={'quantity': 'units_sold', 'item_price': 'revenue'})
 .sort_values(by='units_sold', ascending=False)
 .head(4)
 .reset_index()
)

# storing the results of each step in a separate variable

item_sums = orders.groupby('item_name').sum()
item_sums.drop(columns='order_id', inplace=True)
item_sums.rename(columns={'quantity': 'units_sold', 'item_price': 'revenue'}, inplace=True)
sorted_item_sums = item_sums.sort_values(by='units_sold', ascending=False)
top_four_items = sorted_item_sums.head(4)


sns.barplot(data=four_most_popular, y='item_name', x='revenue')
plt.ylabel('')
plt.xticks()

# 5.) Load the sleepstudy data and read it's documentation. 
# Use seaborn to create a line chart of all the individual subject's reaction times and a more prominant line showing the average change in reaction time.

sleep = data('sleepstudy')
data('sleep', show_doc = True)
sleep.info()
sleep.tail(20)
sleep.describe()

sns.set_style('darkgrid')
sns.set_context(font_scale = 1, rc = {"grid.linewidth": 1, "axes.linewidth": 1, "ytick.major.width": 1, "xtick.major.width": 1, "lines.linewidth": 1})
palette = sns.color_palette("deep", 18)
sns.lineplot(x = 'Days', y = 'Reaction', hue = 'Subject', data = sleep, palette = palette)
sns.set_context(rc = {"lines.linewidth": 4})
sns.lineplot(x = 'Days', y = 'Reaction', data = sleep, ci = None)