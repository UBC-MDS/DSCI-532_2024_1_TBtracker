from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

import pandas as pd

app = Dash(__name__)

rf = pd.read_csv("data/raw/TB_burden_age_sex_2024-03-26.csv")
rf_pak = rf.loc[rf["country"] == 'Pakistan']

rf_pak2 = rf_pak.groupby(['age_group', 'sex'], as_index=False)['best'].sum()
rf_pak3 = rf_pak2.loc[(rf_pak2["sex"] != 'a') & (rf_pak2["age_group"] != 'all')]

rf_pak3 = rf_pak3[~rf_pak3['age_group'].isin(['0-14', '15plus', '18plus'])].copy()
order_age = ['0-4', '5-14', '15-24', '25-34', '35-44', '45-54', '55-64', '65plus']
rf_pak3['age_group'] = pd.Categorical(rf_pak3['age_group'], categories=order_age, ordered=True)
rf_pak3 = rf_pak3.sort_values('age_group')


app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                rf_pak3['age_group'].unique(),
                id='xaxis-column'
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

    ]),

    dcc.Graph(id='indicator-graphic'),

])


@callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'))
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    #dff = df[df['Year'] == year_value]

    fig = px.box(x=rf_pak3[rf_pak3['age_group'] == xaxis_column_name]['Value'],
                     y=rf_pak3[rf_pak3['Best'] == yaxis_column_name]['Value'],
                     hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')

    return fig


if __name__ == '__main__':
    app.run(debug=True)