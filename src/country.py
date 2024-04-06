from dash import dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

rf_data = pd.read_csv("data/preprocessing/rf_data.csv")

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


country_page = dbc.Container(
    [
        dbc.Col([risk_facts_graph])
    ]
)


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

    fig = px.bar(rff3, x='age_group', y='best', color='sex',
                 labels={'age_group': 'Age Group',
                         'best': 'TB Incidence (Estimate from WHO)'})

    fig.update_layout(
        margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    # Custom legend labels
    custom_labels = {'m': 'Male', 'f': 'Female'}

    for trace in fig.data:
        if trace.name in custom_labels:
            trace.name = custom_labels[trace.name]

    fig.update_layout(legend_title_text='Sex')

    return fig
