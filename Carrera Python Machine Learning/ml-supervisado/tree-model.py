from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import pandas as pd

data_location = 'tweet_and_user_data.csv'

X_variables = ['followers', 'video']
y_variable_class = 'nlikes'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location)

train, test = train_test_split(tweet_data, train_size=0.7, random_state=0)

clas_tree_model_reduced = DecisionTreeClassifier(max_depth=3)
clas_tree_model_reduced.fit(train[X_variables], train[y_variable_class]);

plt.figure(figsize=(12, 12))
tree.plot_tree(clas_tree_model_reduced, fontsize=10)
plt.show()