from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

rf_data = pd.read_csv("data/preprocessing/rf_data.csv")

risk_facts_graph = dbc.Container([
    dbc.Container([
        dcc.Dropdown(
            rf_data['country'].unique(),
            id='rf-country-dropdown'
        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    dbc.Container([
        dcc.Dropdown(
            rf_data['sex'].unique(),
            id='rf-sex-dropdown',

        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    dbc.Container([
        dcc.Dropdown(
            rf_data['age_group'].unique(),
            id='rf-age-dropdown',
            multi=True

        )
    ], style={'width': '48%', 'display': 'inline-block'}),

    dcc.Graph(id='indicator-graphic'),
])


country_page = dbc.Container(
    [
        dbc.Col([risk_facts_graph])
    ]
)

# # This has to be done in a separate callback than below
# # Otherwise the rf-country-dropdown is not yet defined before we switch tabs
# @callback(
#     Output('rf-country-dropdown', 'value'),
#     Input('memory-output', 'data')
# )
# def update_dropdown(data):
#     return data
