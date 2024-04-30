from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
import pandas as pd
import plotnine as pn

data_location = 'tweet_and_user_data.csv'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location)

train, test = train_test_split(tweet_data, train_size=0.7, random_state=0)

train = train.reset_index(drop=True)
test = test.reset_index(drop=True)

variables = ['language', 'location']

location_replace = SimpleImputer(strategy='constant',fill_value='UKNOWN')

location_replace.fit(train[variables])

location_replace.transform(train[variables])