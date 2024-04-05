from dash import Dash, html, dcc, Input, Output, callback
import altair as alt
from vega_datasets import data
import dash_vega_components as dvc
import dash_bootstrap_components as dbc
import pandas as pd

tb_data = pd.read_csv("data/preprocessing/tb_data.csv")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


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
                     style={"width": "100%"})

histogram = dvc.Vega(
    id="tb_histogram",
    opt={"renderer": "svg", "actions": False},
    spec={},
    style={"width": "100%"}
)

slider_year = dcc.Dropdown(
        id='year', options=tb_data.year, value=2022)



app.layout = dbc.Container([
    dbc.Row(dbc.Col(title)),
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
                    f"{'Incidence' if selected_value ==
                        'incidence' else 'Mortality'}",
                    f"{'Absolute' if selected_type ==
                        'absolute' else 'Relative'}",
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
).project(scale=150)

    return geo_chart.to_dict()


if __name__ == "__main__":
    app.run_server(port=8000, host="127.0.0.1",
                   debug=True, dev_tools_hot_reload=True)
