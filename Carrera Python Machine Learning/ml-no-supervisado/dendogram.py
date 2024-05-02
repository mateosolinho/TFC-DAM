import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import AgglomerativeClustering
from sklearn.pipeline import Pipeline

data_location = 'tweet_and_user_data.csv'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location)

unique = ['id', 'conversation_id', 'retweet_id']
avg = ['nlikes', 'nreplies', 'nretweets']

gby = ['id_user', 'username_user', 'join_date', 'following', 'followers', 'likes', 'media', 'location', 'verified']

agg = {col : 'nunique' if col in unique else 'mean' for col in unique + avg}

tweet_data['location'] = tweet_data.location.fillna('')

user_stats = tweet_data.groupby(gby).agg(agg)

user_stats['has_retweets'] = user_stats.retweet_id > 0

agg_pipeline = Pipeline(
    [
        ('scaler', preprocessing.StandardScaler()),
        ('cluster', AgglomerativeClustering(5))
    ]
)
X_variables = ['followers', 'following', 'likes', 'media', 'num_days_created', 'verified', 'has_retweets']

predictions = agg_pipeline.fit_predict(user_stats[X_variables])
pd.DataFrame(predictions).value_counts()

def plot_dendrogram(model, **kwargs):

    children = model.children_

    distance = np.arange(children.shape[0])

    no_of_observations = np.arange(2, children.shape[0]+2)

    linkage_matrix = np.column_stack([children, distance, no_of_observations]).astype(float)

    dendrogram(linkage_matrix, **kwargs)

plt.figure(figsize=(12, 12))
plot_dendrogram(agg_pipeline['cluster'], labels=agg_pipeline['cluster'].labels_, truncate_mode='level', p=5)
plt.show()

