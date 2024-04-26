import pandas as pd
import plotnine as pn

X_variables = ['followers', 'video']
Y_variable = 'nlikes'

data_location = 'tweet_and_user_data.csv'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location, low_memory=False)

tweet_data.shape

tweet_data.head()

print(tweet_data.shape)