from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import os
from ..data import tb_data

# Define the layout for the world_map page

title = html.H1("Global Tuberculosis Trends", style={"textAlign": "left", "padding-top" : "2%"})

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


build_info = html.Div([
    html.H4("ABOUT", style={'padding-top': '10%'}),
    html.P("TBTracker uses data from WHO's global tuberculosis platform to visualize incidence and mortality rates across \
                countries. Data was collected from the 2023 report, which includes data up to (but not including) 2023.", style={"font-size": "0.8em"}),
    html.P("App was created by Sandra Gross, Sean McKay, Hina Bandukwala, and Yiwei Zhang",
           style={"font-size": "0.8em"}),
    html.A("Github Repo", href="https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker",
           style={"font-size": "0.8em"}),
    html.P(f"Last build was { deploy_time if deploy_time else '2024-04-06'}",
           style={"font-size": "0.8em"})
])


world_component = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        title,
                        html.Hr(style={'color': 'black'}),
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
                        html.Br(),
                        build_info
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
