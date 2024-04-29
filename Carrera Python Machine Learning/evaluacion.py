from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

data_location = 'tweet_and_user_data.csv'

X_variables = ['followers', 'video']
y_variable_class = 'nlikes'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location)

train, test = train_test_split(tweet_data, train_size=0.7, random_state=0)

for prediction in [col for col in test if '_clas' in col or 'log_reg' in col]:
    if 'proba' not in prediction:
        acc = accuracy_score(test[y_variable_class], test[prediction])
        print(f'For {prediction} we scored {acc:.0%}')