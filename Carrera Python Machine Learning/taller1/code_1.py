import statsmodels.api as sm
import pandas as pd 
import plotnine as pn
import sklearn
import numpy as np


data_location = 'tweet_and_user_data.csv'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location)

train, test = sklearn.model_selection.train_test_split(tweet_data, train_size=0.7, random_state=0)

train = train.reset_index(drop=True)
test = test.reset_index(drop=True)

train['video'] = train.video.astype(bool)

target = 'is_popular'

results = []
renames = {0 : 'recall', 1 : 'precision', 2 : 'threshold'}
for i in range(1, 6):
    result = pd.DataFrame(sklearn.metrics.precision_recall_curve(test[target], test[f'predictions_{i}'])).transpose().rename(columns=renames)
    result['prediction_number'] = str(i)
    results.append(result)
    
results = pd.concat(results) 

results['threshold'] = results.threshold.round(3)

results = results.groupby(['prediction_number', 'threshold']).head(1)

results['recall_diff'] = results.groupby('prediction_number').recall.diff()
results['precision_diff'] = results.groupby('prediction_number').precision.diff()

c = (results.recall_diff >= 0)
graph = (
    pn.ggplot(results[c], pn.aes(x='recall', y='precision', color='prediction_number'))
    + pn.geom_line(size=1.4)
)

graph.draw();