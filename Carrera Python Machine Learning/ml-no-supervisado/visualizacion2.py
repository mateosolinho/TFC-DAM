from sklearn import metrics, preprocessing
import plotnine as pn
from sklearn.cluster import KMeans, MiniBatchKMeans
import pandas as pd
from sklearn.pipeline import Pipeline

data_location = 'tweet_and_user_data.csv'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location)

X_variables = ['followers', 'following', 'likes', 'media', 'num_days_created']

unique = ['id', 'conversation_id', 'retweet_id']
avg = ['nlikes', 'nreplies', 'nretweets']

gby = ['id_user', 'username_user', 'join_date', 'following', 'followers', 'likes', 'media', 'location', 'verified']

agg = {col : 'nunique' if col in unique else 'mean' for col in unique + avg}

tweet_data['location'] = tweet_data.location.fillna('')

user_stats = tweet_data.groupby(gby).agg(agg)

model = MiniBatchKMeans(n_clusters=10, batch_size=100, random_state=0)
model.fit(user_stats[X_variables])
user_stats['predictions_kmeans_minibatch'] = model.predict(user_stats[X_variables])

user_stats.predictions_kmeans_minibatch.value_counts()

kmeans_pipeline = Pipeline(
    [
        ('scaler', preprocessing.StandardScaler()),
        ('cluster', KMeans(n_clusters=5, random_state=0))
    ]
)

kmeans_pipeline.fit(user_stats[X_variables])
predictions = kmeans_pipeline.predict(user_stats[X_variables])
pd.DataFrame(predictions).value_counts()

metrics.silhouette_score(kmeans_pipeline['scaler'].transform(user_stats[X_variables]), predictions)

user_stats['predictions_kmeans_3'] = user_stats.predictions_kmeans_3.astype(str)

graph = (
    pn.ggplot(user_stats, pn.aes(x='followers', y='following', color='predictions_kmeans_5_scaler'))
    + pn.geom_point()
    + pn.scale_x_continuous(trans='log')
    + pn.scale_y_continuous(trans='log')
)

graph.draw();

