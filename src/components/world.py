from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import os
from ..data import tb_data

# Define the layout for the world_map page

# Cards
card_global_stats = dbc.Card(
    dbc.CardBody([html.Div(id="stats-content", style={"textAlign": "center"})]),
    color="light",
    style={
        "margin-top": "10%",
        "margin": "5%",
        "border": "1px solid lightgray",
        "borderRadius": "20px",
    },
)

title_p1 = html.H1("Global", style={"textAlign": "left", "padding-top": "2%"})
title_p2 = html.H1("TB Trends", style={"textAlign": "left"})

deploy_time = os.getenv("DEPLOY_DATETIME")  # Set in render.com build step

global_widgets_metric = html.Div(
    [
        dcc.RadioItems(
            id="radio-1",
            options=[
                {"label": "Absolute Numbers", "value": "absolute"},
                {"label": "Relative Numbers", "value": "relative"},
            ],
            value="absolute",
            labelStyle={"display": "block"},
        ),
        # Add the explanation as a separate text element aligned with "Relative Numbers"
        html.Div(
            "(Proportional to pop size)",
            style={
                "marginLeft": "10px",  # Align with the radio item text
                "fontSize": "smaller",  # Smaller font size for the subtext
                "color": "#6c757d",  # A muted color for the subtext
            },
            id="relative-numbers-description",
        ),
    ]
)

global_widgets_var = dcc.RadioItems(
    id="radio-2",
    options=[
        {"label": "Incidence", "value": "incidence"},
        {"label": "Mortality", "value": "mortality"},
    ],
    value="incidence",
    labelStyle={"display": "block"},
)

geo_chart = dvc.Vega(
    id="geo_chart",
    spec={},
    signalsToObserve=["selected_country"],
    style={"width": "99%"},
)

dropdown_year = dcc.Dropdown(id="year", options=tb_data.year.unique(), value=2022)

global_tab = dbc.Tab(
    label="Global Data",
    tab_id="tab-1",
    active_tab_style={"background-color": "#cee3eb"},
    tab_style={"background-color": "#dfebed"},
)

country_tab = dbc.Tab(
    label="Country-Specific",
    tab_id="tab-2",
    active_tab_style={"background-color": "#cee3eb"},
    tab_style={"background-color": "#dfebed"},
)

total_tab = dbc.Tabs(
    id="global-tab",
    active_tab="tab-1",
    children=[global_tab, country_tab],
    style={"padding": "10px"},
)


about_info = html.Div(
    [
        html.H4("ABOUT", style={"padding-top": "1%", "text-align": "center"}),
        html.P(
            "Welcome to TBTracker! This dashboard offers a comprehensive visualization of global Tuberculosis (TB) estimates from WHO.",
            style={"font-size": "0.8em"},
        ),
        html.P(
            "App was created by Sandra Gross, Sean McKay, Hina Bandukwala, and Yiwei Zhang",
            style={"font-size": "0.8em"},
        ),
    ]
)


build_info = html.Div(
    [
        html.A(
            "Github Repo",
            href="https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker",
            style={"font-size": "0.8em"},
        ),
        html.P(
            f"Last build was { deploy_time if deploy_time else '2024-04-06'}",
            style={"font-size": "0.8em"},
        ),
    ]
)


learn_more_btn = dbc.Button(
    "Learn More", color="primary", style={"font-size": "0.8em"}, id="learn-more-open"
)

learn_more_text = "We're students from the UBC Master of Data Science program, \
    and we've developed The Global Tuberculosis Tracker as a resource for easy access to global TB trends. \
    This tool is designed for NGOs, policymakers, and public health organizations to streamline the analysis of TB incidence, \
    its trends, and associated risk factors through straightforward visualizations. \
    By leveraging data from the WHO, our application supports well-informed decision-making in the battle against TB, \
    emphasizing the disease's progression and its association with risk factors such as HIV. \
    Our objective is to equip stakeholders with precise data to aid strategic planning and intervention efforts."

learn_more_popup = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("About the Project")),
        dbc.ModalBody(learn_more_text),
        dbc.ModalFooter(
            dbc.Button("Close", id="learn-more-close", className="ms-auto", n_clicks=0)
        ),
    ],
    id="modal",
    is_open=False,
)


world_component = dbc.Container(
    [
        dbc.Row(
            [
                learn_more_popup,
                dbc.Col(
                    [
                        dbc.Row([title_p1]),
                        dbc.Row([title_p2]),
                        html.Hr(
                            style={
                                "color": "black",
                            }
                        ),
                        dbc.Label("Metric", className="filter-label"),
                        global_widgets_var,
                        html.Br(),
                        dbc.Label("Scale", className="filter-label"),
                        global_widgets_metric,
                        html.Br(),
                        dbc.Label("Year", className="filter-label"),
                        dropdown_year,
                        html.Br(),
                        html.Br(),
                        about_info,
                        dbc.Row(
                            [learn_more_btn],
                            style={
                                "padding-bottom": "5%",
                                "padding-left": "10%",
                                "padding-right": "10%",
                            },
                        ),
                        build_info
                    ],
                    md=2,
                    style={"background-color": "#CBC3E3"},
                ),
                dbc.Col(
                    [
                        geo_chart,
                        dbc.Row(
                            [
                                html.P(
                                    "* Hover to view summary; click to view details.",
                                    style={"text-align": "center", "font-size": "14px"},
                                )
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    card_global_stats,
                                    width={"size": 3, "offset": 0},
                                    style={
                                        "position": "absolute",
                                        "bottom": 180,
                                        "left": 0,
                                    },
                                ),
                            ],
                            className="position-relative",
                        ),
                    ],
                    md=10,
                ),
            ]
        ),
    ],
    fluid=True,
)

global_layout = dbc.Container(
    [total_tab, dcc.Store(id="memory-output"), dbc.Container(id="tb-page", fluid=True)],
    fluid=True,
)
