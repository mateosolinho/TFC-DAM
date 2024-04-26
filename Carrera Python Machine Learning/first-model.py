from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import plotnine as pn

data_location = 'tweet_and_user_data.csv'

pd.options.display.max_columns = 500

tweet_data = pd.read_csv(data_location, low_memory=False)

X_variables = ['followers', 'video']
y_variable = 'nlikes'

model = LinearRegression()
model.fit(tweet_data[X_variables], tweet_data[y_variable])
tweet_data['predictions_lin_reg'] = model.predict(tweet_data[X_variables])

model = DecisionTreeRegressor(random_state=0)
model.fit(tweet_data[X_variables], tweet_data[y_variable])
tweet_data['predictions_dt_reg'] = model.predict(tweet_data[X_variables])

# Creamos un gráfico simple para visualizar
columns = [y_variable, 'predictions_lin_reg', 'predictions_dt_reg']
graph_data = pd.melt(tweet_data[columns], id_vars=[y_variable], value_vars=['predictions_lin_reg', 'predictions_dt_reg'])  # Se añade id_vars

graph = (
    pn.ggplot(graph_data, pn.aes(x=y_variable, y='value', color='variable')) 
    + pn.geom_point(alpha=0.4)
    + pn.scale_x_continuous(trans='log')
    + pn.scale_y_continuous(trans='log')
    + pn.ylab('prediction')
)

graph.draw()