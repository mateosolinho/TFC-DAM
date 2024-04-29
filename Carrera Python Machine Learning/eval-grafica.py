import pandas as pd
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, roc_curve
from sklearn.model_selection import train_test_split

data_location = 'tweet_and_user_data.csv'

X_variables = ['followers', 'video']
y_variable_class = 'nlikes'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location, low_memory=False)

train, test = train_test_split(tweet_data, train_size=0.7, random_state=0)

# X_variables = ['followers', 'retweet', 'video', 'tweets', 'likes', 'following', 'media', 'verified', 'day', 'hour']

# plot_confusion_matrix(clas_rf_model, test[X_variables], test[y_variable_class], normalize='true', display_labels=['Fewer than 50 likes', 'More than 50 likes'])

# ==============

X_variables = ['followers', 'video']

plot_roc_curve(clas_nn_model, test[X_variables], test[y_variable_class])