from dash import Dash, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import altair as alt
from vega_datasets import data


cars = data.cars()

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = dbc.Container([
    dvc.Vega(id='scatter', spec={}),
    dcc.Dropdown(id='x-col', options=cars.columns, value='Horsepower'),
])

# Server side callbacks/reactivity
@callback(
    Output('scatter', 'spec'),
    Input('x-col', 'value')
)
def create_chart(x_col):
    return(
        alt.Chart(cars).mark_point().encode(
            x=x_col,
            y='Miles_per_Gallon',
            tooltip='Origin'
        ).interactive().to_dict()
    )

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)