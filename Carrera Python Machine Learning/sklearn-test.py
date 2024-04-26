from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

X_variables = ['followers', 'video']
Y_variable = 'nlikes'

model = LinearRegression()
model.fit(tweet_data[X_variables], tweet_data[Y_variable])
tweet_data['predictions_lin_reg'] = model.predict(tweet_data[X_variables])

model = DecisionTreeRegressor(random_state=0)
model.fit(tweet_data[X_variables], tweet_data[Y_variable])
tweet_data['predictions_lin_reg'] = model.predict(tweet_data[X_variables])

# Creamos un grafico simple para visualizar
columns = [Y_variable, 'predictions_lin_reg', 'predictions_dt_reg']
graph_data = pd.melt(tweet_data[columns], Y_variable)
graph = (
    pn.ggplot(graph_data, pn.aes(x='nlikes', y='value', color='variable')) 
    + pn.geom_point(alpha=0.4)
    + pn.scale_x_continuous(trans='log')
    + pn.scale_y_continuous(trans='log')
    + pn.ylab('prediction')

)

graph.draw();