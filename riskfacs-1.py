from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

import pandas as pd

app = Dash(__name__)

rf = pd.read_csv("data/raw/TB_burden_age_sex_2024-03-26.csv")
rf = rf.loc[(rf["sex"] != 'a') & (rf["age_group"] != 'all')]
rf = rf[~rf['age_group'].isin(['0-14', '15plus', '18plus'])].copy()
order_age = ['0-4', '5-14', '15-24', '25-34', '35-44', '45-54', '55-64', '65plus']
rf['age_group'] = pd.Categorical(rf['age_group'], categories=order_age, ordered=True)
rf = rf.sort_values('age_group')


app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                rf['country'].unique(),
                id='country_value'
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                rf['sex'].unique(),
                id='xaxis_sex',

            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                rf['age_group'].unique(),
                id='xaxis_age',
                multi=True
            
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

    
    dcc.Graph(id='indicator-graphic'),

])
])

@callback(
    Output('indicator-graphic', 'figure'),
    Input('country_value', 'value'),
    Input('xaxis_sex', 'value'),
    Input('xaxis_age', 'value'))
def update_graph(country_value, xaxis_sex, xaxis_age):
    rff = rf[rf['country'] == country_value]
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


if __name__ == '__main__':
    app.run(debug=True)