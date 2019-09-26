import pandas as pd
from pydataset import data
import numpy as np

mpg = data('mpg')
data('mpg', show_doc=True)
mpg

# 1) Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:

# 1.a) On average, which manufacturer has the best miles per gallon?

mpg[["manufacturer"]].agg

mpg['average_mpg'] = (mpg.cty + mpg.hwy)/2
mpg
mpg.groupby("manufacturer").mean()
average_miles_per_gallon = mpg.groupby("manufacturer").mean()
average_miles_per_gallon.sort_values(by='average_mpg', ascending = False)


# 1.b) How many different manufacturers are there?



# 1.c) How many different models are there?



# 1.d) Do automatic or manual cars have better miles per gallon?