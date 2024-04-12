from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import os
from ..data import tb_data

# Define the layout for the world_map page

title_p1 = html.H1("Global", style={"textAlign": "left", "padding-top" : "2%"})
title_p2 = html.H1("TB Trends", style={"textAlign": "left"})

deploy_time = os.getenv('DEPLOY_DATETIME')  # Set in render.com build step

global_widgets_metric = dcc.RadioItems(
    id="radio-1",
    options=[
        {"label": "Absolute Numbers", "value": "absolute"},
        {"label": "Relative Numbers", "value": "relative"},
    ],
    value="absolute",
    labelStyle={"display": "block"},
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

geo_chart = dvc.Vega(id="geo_chart",
                     spec={},
                     signalsToObserve=["selected_country"],
                     style={"width": "100%"})

histogram = dvc.Vega(
    id="tb_histogram",
    opt={"renderer": "svg", "actions": False},
    spec={},
    style={"width": "100%"}
)

dropdown_year = dcc.Dropdown(id="year", options=tb_data.year, value=2022)

global_tab = dbc.Tab(label="Global Data", tab_id="tab-1",
                     active_tab_style={'background-color': '#cee3eb'}, tab_style={'background-color': '#dfebed'})

country_tab = dbc.Tab(label="Country-Specific", tab_id="tab-2",
                      active_tab_style={'background-color': '#cee3eb'}, tab_style={'background-color': '#dfebed'})

total_tab = dbc.Tabs(id="global-tab", active_tab="tab-1", children=[global_tab, country_tab],
                     style={"padding": "10px"})


about_info = html.Div([
    html.H4("ABOUT", style={'padding-top': '10%', 'text-align': 'center'}),
    html.P("TBTracker uses data from WHO's global tuberculosis platform to visualize incidence and mortality rates across \
                countries. Data was collected from the 2023 report, which includes data up to (but not including) 2023.", style={"font-size": "0.8em"}),
    html.P("App was created by Sandra Gross, Sean McKay, Hina Bandukwala, and Yiwei Zhang",
           style={"font-size": "0.8em"}),
])


build_info = html.Div([
    html.A("Github Repo", href="https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker",
           style={"font-size": "0.8em"}),
    html.P(f"Last build was { deploy_time if deploy_time else '2024-04-06'}",
           style={"font-size": "0.8em"})
])


learn_more_btn = dbc.Button("Learn More", color="primary", style={"font-size" : "0.8em"}, id="learn-more-open")

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
                    dbc.Button(
                        "Close", id="learn-more-close", className="ms-auto", n_clicks=0
                    )
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
                        html.Hr(style={'color': 'black', }),
                        dbc.Label("Metric", className = "filter-label"),
                        global_widgets_var,
                        html.Br(),
                        dbc.Label("Scale", className = "filter-label"),
                        global_widgets_metric,
                        html.Br(),
                        dbc.Label("Year", className = "filter-label"),
                        dropdown_year,
                        html.Br(),
                        html.Br(),
                        about_info,
                        build_info,
                        dbc.Row([learn_more_btn], style={"padding-bottom" : "5%", 'padding-left' : '10%', 'padding-right' : '10%'}),
                    ], md=2, style={'background-color': '#CBC3E3'}
                ),
                dbc.Col(
                    [dbc.Row(dbc.Col(geo_chart)), dbc.Row(dbc.Col(histogram))], md=10
                ),
            ]
        )
    ], fluid=True
)

global_layout = dbc.Container(
    [total_tab, dcc.Store(id="memory-output"),
     dbc.Container(id="tb-page", fluid=True)],
    fluid=True
)
