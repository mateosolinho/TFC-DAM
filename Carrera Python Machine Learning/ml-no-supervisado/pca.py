from sklearn import preprocessing
from pca import pca
from sklearn import preprocessing
import pandas as pd

data_location = 'tweet_and_user_data.csv'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location)

variables = ['followers', 'following', 'likes', 'media', 'num_days_created']

unique = ['id', 'conversation_id', 'retweet_id']
avg = ['nlikes', 'nreplies', 'nretweets']

gby = ['id_user', 'username_user', 'join_date', 'following', 'followers', 'likes', 'media', 'location', 'verified']

agg = {col : 'nunique' if col in unique else 'mean' for col in unique + avg}

tweet_data['location'] = tweet_data.location.fillna('')

user_stats = tweet_data.groupby(gby).agg(agg)

model = pca(n_components=3)

scaler = preprocessing.StandardScaler()

results = model.fit_transform(scaler.fit_transform(user_stats[variables]))

fig, ax = model.biplot(n_feat=6, alpha_transparency=0.1, hotellingt2=True)
ax.set_xlim([-5, 12])
ax.set_ylim([-1, 12])
fig