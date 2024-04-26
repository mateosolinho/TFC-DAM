from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import pandas as pd
import plotnine as pn

X_variables = ['followers', 'video']
y_variable = 'nlikes'

data_location = 'tweet_and_user_data.csv'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location, low_memory=False)

linear_reg_pipeline = Pipeline (
    [
        ('linear_reg', LinearRegression())
    ]
)

linear_reg_pipeline.fit(tweet_data[X_variables], tweet_data[y_variable])
linear_reg_pipeline.predict(tweet_data[X_variables])[:10]