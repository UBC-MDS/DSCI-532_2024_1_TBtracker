from dash import dcc, html
import dash_bootstrap_components as dbc
from ..data import rf_data

# Function to create line plots
country_dropdown = dcc.Dropdown(
    rf_data["country"].unique(), id="rf-country-dropdown")
sex_dropdown = dcc.Dropdown(rf_data["sex"].unique(), id="rf-sex-dropdown")
age_dropdown = dcc.Dropdown(
    rf_data["age_group"].unique(), id="rf-age-dropdown", multi=True
)
mortality_incidence_plot = dcc.Graph(id="tb_mortality_incidence_plot", style={'height': '30vh'})
case_fatality_ratio_plot = dcc.Graph(id="tb_case_fatality_ratio_plot", style={'height': '30vh'})
hiv_coinfection_plot = dcc.Graph(id="tb_hiv_coinfection_plot", style={'height': '30vh'})
risk_fac_graph = dcc.Graph(id="indicator-graphic", style={'height': '35vh'})
risk_pie_chart = dcc.Graph(id="rf-pie-chart", style={'height': '35vh'})
title = html.H2(id="page-title", style={"textAlign": "center", "padding-top" : "1%"})
risk_fac_graph_title = html.H5(
    "TB Incidence by Demographic Group (2022)", style={"textAlign": "center"})
risk_fac_pie_title = html.H5("TB Incidence by Risk Factor (2022)", style={
                             "textAlign": "center"})


country_component = dbc.Container(
    children=[
        title,
        dbc.Row(
            [
                dbc.Col([dbc.Label("Select Country:")], width="auto"),
                dbc.Col([country_dropdown], width=3)
            ],
            justify="start"
        ),
        html.Hr(style={'color': 'black'}),
        dbc.Row(
            [
                dbc.Col([mortality_incidence_plot], width=4),
                dbc.Col([case_fatality_ratio_plot], width=4),
                dbc.Col([hiv_coinfection_plot], width=4),
            ],
            className="mb-4"
        ),
        dbc.Row([
            dbc.Col([risk_fac_graph_title]),
            dbc.Col([risk_fac_pie_title]),
        ]),
        dbc.Row(
            [
                dbc.Col([dbc.Label("Filters:")], width="auto"),
                dbc.Col(sex_dropdown, width=2),
                dbc.Col(age_dropdown, width=4),
            ], style={'padding-top': '1%'}
        ),
        dbc.Row(
            [
                dbc.Col(risk_fac_graph, width=7),
                dbc.Col(risk_pie_chart, width=5)
            ], style={'padding-top': '1%'}
        )
    ], fluid=True
)
