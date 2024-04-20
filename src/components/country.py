from dash import dcc, html
import dash_bootstrap_components as dbc
from ..data import rf_data

country_dropdown = dcc.Dropdown(rf_data["country"].unique(), id="rf-country-dropdown")

custom_labels = {"m": "Male", "f": "Female"}
sex_options = [{'label': custom_labels.get(sex, f"Other ({sex})"), 
                'value': sex} for sex in rf_data['sex'].unique()]
sex_dropdown = dcc.Dropdown(
    options=sex_options, 
    id="rf-sex-dropdown",
    placeholder="Select Sex:")

age_options = [{'label': f"{age}", 'value': age} for age in rf_data['age_group'].unique()]
age_dropdown = dcc.Dropdown(
    options=age_options, 
    id="rf-age-dropdown", 
    multi=True,
    placeholder="Select Age Group(s):"
)

mortality_incidence_plot = dcc.Graph(
    id="tb_mortality_incidence_plot",
    style={"height": "35vh"},
    config={
        "displayModeBar": False,
    },
)
case_fatality_ratio_plot = dcc.Graph(
    id="tb_case_fatality_ratio_plot",
    style={"height": "35vh"},
    config={
        "displayModeBar": False,
    },
)
hiv_coinfection_plot = dcc.Graph(
    id="tb_hiv_coinfection_plot",
    style={"height": "35vh"},
    config={
        "displayModeBar": False,
    },
)
risk_fac_graph = dcc.Graph(id="indicator-graphic", style={"height": "30vh"})
risk_pie_chart = dcc.Graph(id="rf-pie-chart", style={"height": "30vh"})
title = html.H2(id="page-title", style={"textAlign": "left", "padding-top": "1%"})
risk_fac_graph_title = html.H5(
    "TB Incidence by Demographic Group (2022**)", style={"textAlign": "center"}
)
risk_fac_pie_title = html.H5(
    "TB Incidence by Risk Factor* (2022**)", style={"textAlign": "center"}
)

risk_fac_dislaimer_text = html.P(
    "*Risk Factors are estimates of TB Burden, and may not add up to 100%.",
    style={"text-align": "left", "font-size": "14px"},
)

year_2022_dislaimer_text = html.P(
    "**Data for risk factors and breakdown by demographic group is only available for 2022",
    style={"text-align": "center", "font-size": "14px"},
)

mort_inc_graph_title = html.H5(
    "TB Mortality and Incidence", style={"textAlign": "center"}
)
cfr_graph_title = html.H5("TB Case Fatality Ratio", style={"textAlign": "center"})
tb_hiv_graph_title = html.H5("TB-HIV Coinfection", style={"textAlign": "center"})

country_component = dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col([dbc.Label("Select Country:")], width="auto"),
                dbc.Col([country_dropdown], width=3),
                dbc.Col([None], width=1),
                dbc.Col([title], width=5),
            ],
            justify="start",
            style={"padding-top": "1%", "padding-bottom": "0.5%"},
        ),
        dbc.Row(
            [
                dbc.Col([mort_inc_graph_title]),
                dbc.Col([cfr_graph_title]),
                dbc.Col([tb_hiv_graph_title]),
            ],
            style={
                "background-color": "#CBC3E3",
                "border": "1px solid black",
                "padding-top": "0.5%",
            },
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        mortality_incidence_plot,
                    ],
                    width=4,
                ),
                dbc.Col([case_fatality_ratio_plot], width=4),
                dbc.Col([hiv_coinfection_plot], width=4),
            ]
        ),
        dbc.Row(
            [
                dbc.Col([risk_fac_graph_title]),
                dbc.Col([risk_fac_pie_title]),
            ],
            style={
                "background-color": "#CBC3E3",
                "border": "1px solid black",
                "padding-top": "0.5%",
            },
        ),
        dbc.Row(
            [
                dbc.Col([dbc.Label("Filters:")], width="auto"),
                dbc.Col(sex_dropdown, width=2),
                dbc.Col(age_dropdown, width=4),
                dbc.Col(None, width=1),
                dbc.Col(risk_fac_dislaimer_text, width=4)
            ],
            style={"padding-top": "1%"},
        ),
        dbc.Row(
            [dbc.Col(risk_fac_graph, width=7), dbc.Col(risk_pie_chart, width=5)],
            style={"padding-top": "1%"},
        ),
        dbc.Row(
            [dbc.Col(year_2022_dislaimer_text)],
            style={"padding-top": "1%", "textAlign": "center"}
        )
    ],
    fluid=True,
)
