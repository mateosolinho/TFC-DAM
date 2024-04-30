from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import plotnine as pn
from sklearn.model_selection import train_test_split

data_location = 'tweet_and_user_data.csv'

X_variables = ['followers', 'retweet', 'video', 'tweets', 'likes', 'following', 'media', 'verified', 'day', 'hour']
y_variable_class = 'nlikes'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location)

train, test = train_test_split(tweet_data, train_size=0.7, random_state=0)

model_to_calibrate = RandomForestClassifier(random_state=0)
calibrated_model = CalibratedClassifierCV(model_to_calibrate)
calibrated_model.fit(train[X_variables], train[y_variable_class])
test['predictions_rf_clas_proba_calibrated'] = calibrated_model.predict_proba(test[X_variables])[:,1]
# test['predictions_rf_clas_proba_uncalibrated'] = clas_rf_model.predict_proba(test[X_variables])[:,1]

graph = (
    pn.ggplot(test) 
    + pn.geom_histogram(pn.aes(x='predictions_rf_clas_proba_uncalibrated'), fill='red', alpha=0.3)
    + pn.geom_histogram(pn.aes(x='predictions_rf_clas_proba_calibrated'), fill='blue', alpha=0.3)
)

graph.draw();