from dash import dcc, Input, Output, callback, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

rf_data = pd.read_csv("data/preprocessing/rf_data.csv")
tb_data = pd.read_csv("data/preprocessing/tb_data.csv")

# Function to create line plots
country_dropwdown = dcc.Dropdown(rf_data["country"].unique(), id="rf-country-dropdown")
sex_dropdown = dcc.Dropdown(rf_data["sex"].unique(), id="rf-sex-dropdown")
age_dropdown = dcc.Dropdown(
    rf_data["age_group"].unique(), id="rf-age-dropdown", multi=True
)
mortality_incidence_plot = dcc.Graph(id="tb_mortality_incidence_plot")
case_fatality_ratio_plot = dcc.Graph(id="tb_case_fatality_ratio_plot")
hiv_coinfection_plot = dcc.Graph(id="tb_hiv_coinfection_plot")
risk_fac_graph = dcc.Graph(id="indicator-graphic")
title = html.H1("Global Tuberculosis Trends", style={"textAlign": "center"})


def create_line_plot(df, x_column, y_columns, title, legend_names):
    # Create a copy to not alter the original dataframe
    plot_df = df.copy()

    # Rename the columns for the legend
    for original_col, new_name in zip(y_columns, legend_names):
        plot_df[new_name] = plot_df[original_col]

    # Create the figure using the new column names for y-values
    fig = px.line(plot_df, x=x_column, y=legend_names, title=title)
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Count",
        legend=dict(
            title="Legend",
            title_font=dict(size=10),
            font=dict(size=8),
            x=1,  # Horizontally align to the right
            y=0,  # Vertically align to the bottom
        ),
        plot_bgcolor="white",
    )

    # Optionally remove the original column names from the hover data
    fig.update_traces(hovertemplate=None)

    return fig


country_page = dbc.Container(
    children=[
        dbc.Row([dbc.Col([title]), dbc.Col([title])]),
        dbc.Row(
            [
                dbc.Col([mortality_incidence_plot], width=4),
                dbc.Col([case_fatality_ratio_plot], width=4),
                dbc.Col([hiv_coinfection_plot], width=4),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(sex_dropdown, width=4),
                dbc.Col(age_dropdown, width=4),
            ]
        ),
        dbc.Row([risk_fac_graph]),
    ]
)


@callback(
    Output("tb_mortality_incidence_plot", "figure"),
    Output("tb_case_fatality_ratio_plot", "figure"),
    Output("tb_hiv_coinfection_plot", "figure"),
    Input("rf-country-dropdown", "value"),
)
def update_plots(selected_country):
    # Filter the data based on the selected country
    filtered_data = tb_data[tb_data["country"] == selected_country]

    # Mapping of original column names to human-readable names
    legends = {
        "e_mort_exc_tbhiv_num": "Mortality",
        "e_inc_num": "Incidence",
        "cfr": "Case Fatality Ratio",
        "e_mort_tbhiv_num": "TB-HIV Mortality",
        "e_inc_tbhiv_num": "TB-HIV Incidence",
    }

    # Create the line plot for TB Mortality and Incidence
    mortality_incidence_fig = create_line_plot(
        filtered_data,
        "year",
        ["e_mort_exc_tbhiv_num", "e_inc_num"],
        "TB Mortality and Incidence",
        [legends["e_mort_exc_tbhiv_num"], legends["e_inc_num"]],
    )

    # Create the line plot for TB Case Fatality Ratio
    case_fatality_ratio_fig = create_line_plot(
        filtered_data, "year", ["cfr"], "TB Case Fatality Ratio", [legends["cfr"]]
    )

    # Create the line plot for TB-HIV coinfection incidence and mortality
    hiv_coinfection_fig = create_line_plot(
        filtered_data,
        "year",
        ["e_mort_tbhiv_num", "e_inc_tbhiv_num"],
        "TB-HIV Coinfection",
        [legends["e_mort_tbhiv_num"], legends["e_inc_tbhiv_num"]],
    )

    return mortality_incidence_fig, case_fatality_ratio_fig, hiv_coinfection_fig


@callback(
    Output("indicator-graphic", "figure"),
    Input("rf-country-dropdown", "value"),
    Input("rf-sex-dropdown", "value"),
    Input("rf-age-dropdown", "value"),
)
def update_graph(country_value, xaxis_sex, xaxis_age):
    rff = rf_data[rf_data["country"] == country_value]
    rff1 = rff.groupby(["age_group", "sex"], as_index=False)["best"].sum()

    if xaxis_age == None:
        rff2 = rff1.copy()
    else:
        rff2 = rff1.loc[rff1["age_group"].isin(xaxis_age)]

    if xaxis_sex == None:
        rff3 = rff2.copy()
    else:
        rff3 = rff2.loc[rff2["sex"] == xaxis_sex]

    fig = px.bar(
        rff3,
        x="age_group",
        y="best",
        color="sex",
        labels={"age_group": "Age Group", "best": "TB Incidence (Estimate from WHO)"},
    )

    fig.update_layout(margin={"l": 40, "b": 40, "t": 10, "r": 0}, hovermode="closest")

    # Custom legend labels
    custom_labels = {"m": "Male", "f": "Female"}

    for trace in fig.data:
        if trace.name in custom_labels:
            trace.name = custom_labels[trace.name]

    fig.update_layout(legend_title_text="Sex")

    return fig
