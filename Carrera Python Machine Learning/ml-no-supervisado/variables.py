import pandas as pd
import plotnine as pn
from sklearn import metrics
from sklearn.cluster import KMeans

data_location = 'tweet_and_user_data.csv'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location)

unique = ['id', 'conversation_id', 'retweet_id']

avg = ['nlikes', 'nreplies', 'nretweets']

gby = ['id_user', 'username_user', 'join_date', 'following', 'followers', 'likes', 'media', 'location', 'verified']

agg = {col : 'nunique' if col in unique else 'mean' for col in unique + avg}

user_stats = tweet_data.groupby(gby).agg(agg)

potential_variables = [col for col in user_stats if user_stats[col].dtypes in [int, float, bool] and col not in ['id_user']]

user_stats[potential_variables].describe()

graph_data = pd.melt(user_stats[potential_variables].corr().round(2).reset_index(), 'index')
graph = (
    pn.ggplot(graph_data, pn.aes(x='index', y='variable', fill='value', label='value'))
    + pn.geom_tile()
    + pn.geom_text()
    + pn.theme(figure_size=(8, 8), axis_text_x=pn.element_text(angle=90))
    + pn.xlab('') + pn.ylab('')
)

graph.draw();