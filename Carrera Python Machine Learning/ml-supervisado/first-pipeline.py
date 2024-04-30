from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import plotnine as pn
import pandas as pd

data_location = 'tweet_and_user_data.csv'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location)

train, test = train_test_split(tweet_data, train_size=0.7, random_state=0)

numeric_variables = ['following', 'followers']
numeric_pipeline = Pipeline(
    [
        ('scaler', StandardScaler())
    ]
)

categoric_variables = ['language']
languages = ['en', 'es']
categoric_pipeline = Pipeline(
    [
        ('encoder', OneHotEncoder(categories=[languages], handle_unknown='ignore'))
    ]
)

# Tenemos que juntar nuestros Pipelines aqui con un sintaxis similar al Pipeline normal
preprocessing = ColumnTransformer(
    [
        ('numeric', numeric_pipeline, numeric_variables),
        ('categorical', categoric_pipeline, categoric_variables)
    ]
)

full_pipeline = Pipeline(
    [
        ('preprocessing', preprocessing),
        ('regression', LinearRegression())
    ]
)

X_variables = numeric_variables + categoric_variables
y_variable = 'nlikes'

full_pipeline.fit(train[X_variables], train[y_variable])

test['prediction'] = full_pipeline.predict(test[X_variables])

graph = (
    pn.ggplot(test, pn.aes(x='nlikes', y='prediction')) 
    + pn.geom_point()
    + pn.scale_x_continuous(trans='log')
    + pn.scale_y_continuous(trans='log')
)

graph.draw();