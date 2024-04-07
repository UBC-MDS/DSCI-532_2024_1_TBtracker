from dash.exceptions import PreventUpdate
from dash import dcc, Input, Output, callback, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

rf_data = pd.read_csv("data/preprocessing/rf_data.csv")
tb_data = pd.read_csv("data/preprocessing/tb_data.csv")

# Function to create line plots
country_dropdown = dcc.Dropdown(rf_data["country"].unique(), id="rf-country-dropdown")
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
risk_fac_graph_title = html.H4("TB Incidence by Demographic Group (2022)", style={"textAlign": "center"})
risk_fac_pie_title = html.H4("TB Incidence by Risk Factor (2022)", style={"textAlign": "center"})


def create_line_plot(df, x_column, y_columns, title, legend_names):
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
            y=0   # Vertically align to the bottom
        ),
        plot_bgcolor="white"
    )

    # Optionally remove the original column names from the hover data
    fig.update_traces(hovertemplate=None)

    return fig


country_page = dbc.Container(
    children=[
        dbc.Row([
            dbc.Col([title, html.H5("Select Country:")])
            ]),
        dbc.Row(
            [
                dbc.Col([country_dropdown], width=4, style={'padding-top': '1%'}),
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


@callback(
    Output('tb_mortality_incidence_plot', 'figure'),
    Output('tb_case_fatality_ratio_plot', 'figure'),
    Output('tb_hiv_coinfection_plot', 'figure'),
    Input('rf-country-dropdown', 'value')
)
def update_plots(selected_country):
    # Filter the data based on the selected country
    filtered_data = tb_data[tb_data['country'] == selected_country]

    # Mapping of original column names to human-readable names
    legends = {
        'e_mort_exc_tbhiv_num': 'Mortality',
        'e_inc_num': 'Incidence',
        'cfr': 'Case Fatality Ratio',
        'e_mort_tbhiv_num': 'TB-HIV Mortality',
        'e_inc_tbhiv_num': 'TB-HIV Incidence'
    }

    # Create the line plot for TB Mortality and Incidence
    mortality_incidence_fig = create_line_plot(
        filtered_data,
        'year',
        ['e_mort_exc_tbhiv_num', 'e_inc_num'],
        'TB Mortality and Incidence',
        [legends['e_mort_exc_tbhiv_num'], legends['e_inc_num']]
    )

    # Create the line plot for TB Case Fatality Ratio
    case_fatality_ratio_fig = create_line_plot(
        filtered_data,
        'year',
        ['cfr'],
        'TB Case Fatality Ratio',
        [legends['cfr']]
    )

    # Create the line plot for TB-HIV coinfection incidence and mortality
    hiv_coinfection_fig = create_line_plot(
        filtered_data,
        'year',
        ['e_mort_tbhiv_num', 'e_inc_tbhiv_num'],
        'TB-HIV Coinfection',
        [legends['e_mort_tbhiv_num'], legends['e_inc_tbhiv_num']]
    )

    return mortality_incidence_fig, case_fatality_ratio_fig, hiv_coinfection_fig

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

    fig = px.bar(
        rff3,
        x="age_group",
        y="best",
        color="sex",
        labels={
            "age_group": "Age Group",
            "best": "TB Incidence (2022 Estimate from WHO)",
        },
        template="plotly_white",
    )

    fig.update_layout(
        margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    # Custom legend labels
    custom_labels = {'m': 'Male', 'f': 'Female'}

    for trace in fig.data:
        if trace.name in custom_labels:
            trace.name = custom_labels[trace.name]

    fig.update_layout(legend_title_text='Sex')

    return fig


# Load the preprocessed data once at the start to avoid reloading it on each callback.
preprocessed_rf_data = pd.read_csv("data/preprocessing/rf_type_data.csv")


@callback(
    Output('rf-pie-chart', 'figure'),
    [
        Input('rf-country-dropdown', 'value'),
        Input('rf-sex-dropdown', 'value'),
        Input('rf-age-dropdown', 'value')
    ]
)
def update_pie_chart(country_value, sex_value, age_values):
    # If no country is selected, do not update the chart
    if not country_value:
        raise PreventUpdate

    # Filter the data for the selected country
    country_data = preprocessed_rf_data[preprocessed_rf_data['country']
                                        == country_value]

    columns_except_country = [col for col in country_data.columns if col != 'country']

    # Prepare the data for the pie chart
    risk_factors_sums = country_data[columns_except_country].sum()

    # Create a dictionary for human-readable risk factor names
    risk_factor_names = {
        'all': 'All',
        'alc': 'Alcohol Use',
        'dia': 'Diabetes',
        'hiv': 'HIV',
        'smk': 'Smoking',
        'und': 'Undernourishment'
    }

    # Prepare the data for the pie chart with human-readable names
    pie_data = pd.DataFrame({
        'Risk Factor': [risk_factor_names.get(x, x) for x in risk_factors_sums.index],
        'Count': risk_factors_sums.values
    })

    # Create the pie chart using the aggregated data
    fig = px.pie(
        pie_data,
        names='Risk Factor',
        values='Count'
    )

    # Customize the layout of the pie chart
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

    return fig


@callback(
    Output("page-title", "children"),
    Input("rf-country-dropdown", "value"),
)
def update_title(selected_country):
    if not selected_country:
        return "Global Tuberculosis Trends"
    else:
        return f"{selected_country}"
