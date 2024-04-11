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
mortality_incidence_plot = dcc.Graph(id="tb_mortality_incidence_plot")
case_fatality_ratio_plot = dcc.Graph(id="tb_case_fatality_ratio_plot")
hiv_coinfection_plot = dcc.Graph(id="tb_hiv_coinfection_plot")
risk_fac_graph = dcc.Graph(id="indicator-graphic")
risk_pie_chart = dcc.Graph(id="rf-pie-chart")
title = html.H1(id="page-title", style={"textAlign": "center"})
risk_fac_graph_title = html.H4(
    "TB Incidence by Demographic Group (2022)", style={"textAlign": "center"})
risk_fac_pie_title = html.H4("TB Incidence by Risk Factor (2022)", style={
                             "textAlign": "center"})


country_component = dbc.Container(
    children=[
        dbc.Row([
            dbc.Col([title, html.H5("Select Country:")])
        ]),
        dbc.Row(
            [
                dbc.Col([country_dropdown], width=4,
                        style={'padding-top': '1%'}),
            ],
            justify="start",
        ),
        dbc.Row(
            [
                dbc.Col([mortality_incidence_plot], width=4),
                dbc.Col([case_fatality_ratio_plot], width=4),
                dbc.Col([hiv_coinfection_plot], width=4),
            ],
            className="mb-4",
        ),
        html.Br(),
        dbc.Row([
            dbc.Col([risk_fac_graph_title, html.H5("Filters:")]),
            dbc.Col([risk_fac_pie_title]),
        ]),
        dbc.Row(
            [
                dbc.Col(sex_dropdown, width=2),
                dbc.Col(age_dropdown, width=4),
            ], style={'padding-top': '1%'}
        ),
        dbc.Row(
            [
                dbc.Col(risk_fac_graph, width=7),
                dbc.Col(risk_pie_chart, width=5)
            ]
        )
    ], fluid=True
)
