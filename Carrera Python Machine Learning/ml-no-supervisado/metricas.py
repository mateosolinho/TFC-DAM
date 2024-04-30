import pandas as pd
import plotnine as pn
from sklearn import metrics
from sklearn.cluster import KMeans

data_location = 'tweet_and_user_data.csv'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location)

X_variables = ['followers', 'following', 'likes', 'media']

unique = ['id', 'conversation_id', 'retweet_id']

avg = ['nlikes', 'nreplies', 'nretweets']

gby = ['id_user', 'username_user', 'join_date', 'following', 'followers', 'likes', 'media', 'location', 'verified']

agg = {col : 'nunique' if col in unique else 'mean' for col in unique + avg}

user_stats = tweet_data.groupby(gby).agg(agg)

results = []
for n_clusters in range(3, 15):
    model = KMeans(n_clusters=n_clusters, random_state=0)
    model.fit(user_stats[X_variables])
    results.append({'num_clusters' : n_clusters, 'inertia' : model.inertia_})
    
results = pd.DataFrame(results)

graph = pn.ggplot(results, pn.aes(x='num_clusters', y='inertia')) + pn.geom_point() + pn.geom_line()
graph.draw();