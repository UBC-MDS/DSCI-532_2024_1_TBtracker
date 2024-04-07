from dash import html, dcc, Input, Output, callback, no_update
import dash_bootstrap_components as dbc
from .country import country_page  # Import the app
import pandas as pd
import altair as alt
import dash_vega_components as dvc
import os


# Data
tb_data = pd.read_csv("data/preprocessing/tb_data.csv")

# Define the layout and callbacks for the main page
world_url = "https://vega.github.io/vega-datasets/data/world-110m.json"

title = html.H1("Global Tuberculosis Trends", style={"textAlign": "center"})

deploy_time = os.getenv('DEPLOY_DATETIME') #Set in render.com build step

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

slider_year = dcc.Dropdown(id="year", options=tb_data.year, value=2022)
global_tab_content = html.Div([title])
global_tab = dcc.Tab(label="Global Data", value="tab-1", children=[global_tab_content])
country_tab = dcc.Tab(label="Country-Specific", value="tab-2")
total_tab = dcc.Tabs(id="global-tab", value="tab-1", children=[global_tab, country_tab])


build_info = html.Div([
        html.H4("ABOUT"),
        html.P("TBTracker uses data from WHO's global tuberculosis platform to visualize incidence and mortality rates across \
                countries. Data was collected from the 2023 report, which includes data up to (but not including) 2023.", style={"font-size":"0.8em"}),
        html.P("App was created by Sandra Gross, Sean McKay, Hina Bandukwala, and Yiwei Zhang", style={"font-size":"0.8em"}),
        html.A("Github Repo", href="https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker", style={"font-size":"0.8em"}),
        html.P(f"Last build was { deploy_time if deploy_time else '2024-04-06'}", style={"font-size":"0.8em"})
])


main_page = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("FILTERS"),
                        dbc.Label("Scale"),
                        global_widgets_metric,
                        html.Br(),
                        dbc.Label("Metric"),
                        global_widgets_var,
                        html.Br(),
                        dbc.Label("Year"),
                        slider_year,
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        
                        build_info
                    ], md=2
                ),
                dbc.Col(
                    [dbc.Row(dbc.Col(geo_chart)), dbc.Row(dbc.Col(histogram))], md=10
                ),
            ]
        )
    ]
)


global_tab = dbc.Container([total_tab])

layout = dbc.Container([
    title,
    global_tab,
    dcc.Store(id='memory-output'),
    dbc.Container(id='tb-page')
])

# This has to be done in a separate callback than below
# Otherwise the rf-country-dropdown is not yet defined before we switch tabs
@callback(
    Output('rf-country-dropdown', 'value'),
    Input('memory-output', 'data')
)
def update_dropdown(data):
    return data


# Returns a no_update if selected country is not none otherwise we enter a callback loop
@callback(
    Output('global-tab', 'value'),
    Output('memory-output', 'data'),
    Input('geo_chart', 'signalData'),
    prevent_initial_call=True
)
def render_content(data):
    if "selected_country" in data and data["selected_country"]:
        return ["tab-2", str(data["selected_country"]["country"][0])]
    else:
        return [no_update, "Canada"]


@callback(
    Output('tb-page', 'children'),
    Input('global-tab', 'value'),
)
def render_content(tab):
    if tab == 'tab-1':
        return main_page
    elif tab == 'tab-2':
        return dbc.Container([
            country_page
        ])


@callback(
    Output("tb_histogram", "spec"),
    [
        Input("year", "value"),
        Input("radio-1", "value"),
        Input("radio-2", "value"),
    ],
)
def update_histogram(selected_year, selected_type, selected_value):
    filtered_df = tb_data[tb_data["year"] == selected_year]

    if selected_type == "absolute" and selected_value == "incidence":
        y_column = "incidence_total"

    elif selected_type == "relative" and selected_value == "incidence":
        y_column = "incidence_rate"

    elif selected_type == "absolute" and selected_value == "mortality":
        y_column = "mortality_total"

    elif selected_type == "relative" and selected_value == "mortality":
        y_column = "mortality_rate"

    else:
        y_column = "incidence_total"

    filtered_df = filtered_df.sort_values(
        by=y_column, ascending=False).head(30)

    title = f"Global tuberculosis trend in {selected_year}"
    fig = (
        alt.Chart(filtered_df, title=title, width="container")
        .mark_bar()
        .encode(
            x=alt.X("country", title="Country",
                    axis=alt.Axis(labels=False)).sort("-y"),
            y=alt.Y(
                y_column,
                title=(
                    f"{'Incidence' if selected_value == 'incidence' else 'Mortality'}",
                    f"{'Absolute' if selected_type == 'absolute' else 'Relative'}",
                ),
            ),
            tooltip=["country", y_column],
        )
    )

    return fig.to_dict()


@callback(
    Output("geo_chart", "spec"),
    [
        Input("year", "value"),
        Input("radio-1", "value"),
        Input("radio-2", "value"),
    ],
)
def update_geofigure(selected_year, selected_type, selected_value):
    filtered_df = tb_data[tb_data["year"] == selected_year]

    if selected_type == "absolute" and selected_value == "incidence":
        y_column = "incidence_total"

    elif selected_type == "relative" and selected_value == "incidence":
        y_column = "incidence_rate"

    elif selected_type == "absolute" and selected_value == "mortality":
        y_column = "mortality_total"

    elif selected_type == "relative" and selected_value == "mortality":
        y_column = "mortality_rate"

    else:
        y_column = "incidence_total"

    geo_chart = alt.Chart(alt.topo_feature(world_url, "countries"), height=400, width="container").mark_geoshape(
        stroke="#aaa", strokeWidth=0.25
    ).encode(
        color=alt.Color(f"{y_column}:Q",
                        title=f"{'Incidence' if selected_value == 'incidence' else 'Mortality'} {'Absolute' if selected_type == 'absolute' else 'Relative'}"),
        tooltip=["country:N", f"{y_column}:Q"]
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(filtered_df, 'iso_numeric', [y_column, "country"])
    ).add_params(
        alt.selection_point(fields=["country"], name="selected_country")
    ).project(scale=150)

    return geo_chart.to_dict()
