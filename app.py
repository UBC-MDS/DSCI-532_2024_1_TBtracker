from dash import Dash, html, dcc, Input, Output, callback
import altair as alt
from vega_datasets import data
import dash_vega_components as dvc
import dash_bootstrap_components as dbc
import pandas as pd

tb_data = pd.read_csv("data/preprocessing/tb_data.csv")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


source = alt.topo_feature(data.world_110m.url, 'countries')
chart = alt.Chart(source, width= 700, height=300).mark_geoshape(
    fill='white',
    stroke='black',
)


app.layout = dbc.Container([
    html.H1("Global Tuberculosis Trends",  style ={'textAlign': 'center'}),
       dbc.Row([
        dbc.Col(
            dcc.RadioItems(
                id='radio-1',
                options=[
                    {'label': 'Absolute Numbers', 'value': 'absolute'},
                    {'label': 'Relative Numbers', 'value': 'relative'}
                ],
                value = "absolute",
                labelStyle={'display': 'block'}
            ),
            width=3  # Set width to 6 (half of the row) for each column
        ),
        dbc.Col(
            dcc.RadioItems(
                id='radio-2',
                options=[
                    {'label': 'Incidence Rate', 'value': 'incidence'},
                    {'label': 'Mortality Rate', 'value': 'mortality'}
                ],
                value = "incidence",
                labelStyle={'display': 'block'}
            ),
            width=3 # Set width to 6 (half of the row) for each column
        ),
    ]),
    dbc.Row(
            [
                dbc.Col(dvc.Vega(spec=chart.to_dict()), width=6),
                dbc.Col(dvc.Vega(id= "tb_histogram", opt={"renderer": "svg", "actions": False}, spec={}), width = 6),
            ]
        ),
   # dvc.Vega(spec=chart.to_dict(), style={'margin-left': 'auto', 'margin-right': '0'}),
    #dvc.Vega(id= "tb_histogram", opt={"renderer": "svg", "actions": False}, spec={}),
    html.Label('Year'),
    dcc.Slider(
        min=2000, 
        max=2022, 
        value=2022, 
        step = 1,
        marks={str(year): str(year) for year in range(2000, 2023)},
        id='year-slider'
    )
])

@callback(
    Output('tb_histogram', 'spec'),
    [Input('year-slider', 'value'), Input('radio-1', 'value'), Input('radio-2', 'value')]
)
def update_figure(selected_year, selected_type, selected_value):
    filtered_df = tb_data[tb_data['year'] == selected_year]

    if (selected_type == "absolute" and selected_value == "incidence"):
        y_column = "incidence_total" 
        
    elif (selected_type == "relative" and selected_value == "incidence"):
        y_column = "incidence_rate"

    elif (selected_type == "absolute" and selected_value == "mortality"):
        y_column = "mortality_total"

    elif (selected_type == "relative" and selected_value == "mortality"):
        y_column = "mortality_rate"

    else:
        y_column = 'incidence_total'

    filtered_df = filtered_df.sort_values(by=y_column, ascending=False).head(30)

    title = f"Global tuberculosis trend in {selected_year}"
    fig = alt.Chart(filtered_df, title=title).mark_bar().encode(
        x=alt.X("country", title="Country", axis=alt.Axis(labels=False)).sort('-y'),
        y=alt.Y(y_column, title=(f"{'Incidence' if selected_value == 'incidence' else 'Mortality'} "
         f"({'Absolute' if selected_type == 'absolute' else 'Relative'})")),
        tooltip=["country", y_column]
    ).properties(
        width=400
    ).interactive()

    return fig.to_dict()




if __name__ == '__main__':
    app.run_server(port=8000, host='127.0.0.1', debug = True, dev_tools_hot_reload = True)