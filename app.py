from dash import Dash, html, dcc, Input, Output, callback, no_update
import altair as alt
from vega_datasets import data
import dash_vega_components as dvc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


#Data 
tb_data = pd.read_csv("data/preprocessing/tb_data.csv")
rf_data = pd.read_csv("data/preprocessing/rf_data.csv")




country_list = tb_data["country"].unique()

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


world_url = "https://vega.github.io/vega-datasets/data/world-110m.json"

title = html.H1("Global Tuberculosis Trends", style={"textAlign": "center"})

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

geo_chart = dvc.Vega(id = "geo_chart", 
                     spec ={}, 
                     signalsToObserve=["selected_country"],
                     style={"width": "100%"})

histogram = dvc.Vega(
    id="tb_histogram",
    opt={"renderer": "svg", "actions": False},
    spec={},
    style={"width": "100%"}
)

slider_year = dcc.Dropdown(
        id='year', options=tb_data.year, value=2022)



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

main_page = dbc.Container([
    dbc.Row([
        dbc.Col([dbc.Label('Scale'),
                global_widgets_metric,
                dbc.Label('Metric'),
                global_widgets_var,
                dbc.Label('Year'),
                slider_year]),
        dbc.Col([
            dbc.Row(dbc.Col(geo_chart)),
            dbc.Row(dbc.Col(histogram))
        ], md=8)
    ])
])

country_page = dbc.Container(
    [
        dbc.Col([risk_facts_graph])
    ]
)

global_tab = dbc.Container([
    dcc.Tabs(
        id="global-tab",
        value="tab-1",
        children=[
        dcc.Tab(label='Global Data', value='tab-1'),
        dcc.Tab(label='Country-Specific', value='tab-2'),
    ]),
])

app.layout = dbc.Container([
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
        return [no_update, no_update] 



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

    geo_chart = alt.Chart(alt.topo_feature(world_url, "countries"), height = 400, width="container").mark_geoshape(
    stroke="#aaa", strokeWidth=0.25
).encode(
    color=alt.Color(f"{y_column}:Q",
                    title=f"{'Incidence' if selected_value == 'incidence' else 'Mortality'} {'Absolute' if selected_type == 'absolute' else 'Relative'}"),
    tooltip = ["country:N",f"{y_column}:Q"]
).transform_lookup(
    lookup='id',
    from_=alt.LookupData(filtered_df, 'iso_numeric', [y_column, "country"])
).add_params(
        alt.selection_point(fields=["country"], name="selected_country")
).project(scale=150)
    

    return geo_chart.to_dict()


@callback(
    Output('indicator-graphic', 'figure'),
    Input('rf-country-dropdown', 'value'),
    Input('rf-sex-dropdown', 'value'),
    Input('rf-age-dropdown', 'value'))
def update_graph(country_value, xaxis_sex, xaxis_age):
    rff = rf_data[rf_data['country'] == country_value]
    rff1 = rff.groupby(['age_group', 'sex'], as_index=False)['best'].sum()
    
    if xaxis_age == None:
        rff2 = rff1.copy()
    else:
        rff2 = rff1.loc[rff1["age_group"].isin(xaxis_age)]
    
    if xaxis_sex == None:
        rff3 = rff2.copy()
    else:
        rff3 = rff2.loc[rff2["sex"] == xaxis_sex]
    
    fig = px.bar(rff3, x = 'age_group', y = 'best', color='sex',
                 labels={'age_group': 'Age Group', 
                         'best':'TB Incidence (Estimate from WHO)'})

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    # Custom legend labels
    custom_labels = {'m': 'Male', 'f': 'Female'}

    for trace in fig.data:
        if trace.name in custom_labels:
            trace.name = custom_labels[trace.name]

    fig.update_layout(legend_title_text='Sex')

    return fig

if __name__ == "__main__":
    app.run_server(port=8000, host="127.0.0.1",
                   debug=True, dev_tools_hot_reload=True)
