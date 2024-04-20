from dash import Input, Output, State, callback, no_update, html
from dash.exceptions import PreventUpdate
from .components.country import country_component
from .components.world import world_component
from .utils import world_url, create_line_plot

from .data import tb_data, rf_data, preprocessed_rf_data, world_shp


import pandas as pd
import altair as alt
import plotly.express as px
from functools import lru_cache


@callback(
    Output("stats-content", "children"),
    [
        Input("year", "value"),
        Input("radio-1", "value"),
        Input("radio-2", "value"),
    ],
)
def update_card(selected_year, selected_type, selected_value):
    (
        global_stat,
        diff_previous_text,
        diff_next_text,
        diff_previous_color,
        diff_next_color,
        global_stats_value,
    ) = update_global_stats(selected_year, selected_type, selected_value)

    return [
        html.H5(
            global_stats_value, className="card-title", style={"textAlign": "center"}
        ),
        html.P(global_stat, style={"fontSize": "35px", "fontWeight": "bold"}),
        html.P(
            f"YoN: {diff_previous_text}",
            style={"fontSize": "15px", "color": diff_previous_color},
        ),
        html.P(
            f"NoY: {diff_next_text}",
            style={"fontSize": "15px", "color": diff_next_color},
        ),
    ]


@lru_cache
def update_global_stats(selected_year, selected_type, selected_value):
    y_column_mapping = {
        ("absolute", "incidence"): "incidence_total",
        ("relative", "incidence"): "incidence_total",
        ("absolute", "mortality"): "mortality_total",
        ("relative", "mortality"): "mortality_total",
    }
    y_column = y_column_mapping.get((selected_type, selected_value), "incidence_total")

    tb_data["year_dt"] = pd.to_datetime(tb_data["year"], format='%Y')
    selected_year_dt = pd.Timestamp(str(selected_year))
    previous_year_dt = selected_year_dt - pd.DateOffset(years=1)
    next_year_dt = selected_year_dt + pd.DateOffset(years=1)

    if selected_type == "relative":
        global_stat = (tb_data.loc[tb_data["year"] == selected_year][y_column].sum() / tb_data.loc[tb_data["year"] == selected_year]["e_pop_num"].sum()) * 100 
    else:
        global_stat = tb_data.loc[tb_data["year"] == selected_year, y_column].sum()


    diff_previous = diff_next = None  # Default values for differences
    diff_previous_color = diff_next_color = 'black'  # Default text color

    if selected_year != 2000:
        if selected_type == "absolute":
            global_stat_previous = tb_data.loc[tb_data["year_dt"] == previous_year_dt, y_column].sum()
            if global_stat_previous:
                diff_previous = ((global_stat - global_stat_previous) / global_stat_previous) * 100
                diff_previous_color = "blue" if diff_previous > 0 else "red"
        else:
            global_stat_previous = (tb_data.loc[tb_data["year_dt"] == previous_year_dt, y_column].sum() / tb_data.loc[tb_data["year_dt"] == previous_year_dt, 'e_pop_num'].sum()) * 100
            if global_stat_previous:
                diff_previous = global_stat - global_stat_previous
                diff_previous_color = "blue" if diff_previous > 0 else "red"
    
    if selected_year != 2022:
        if selected_type == "absolute":
            global_stat_next = tb_data.loc[tb_data["year_dt"] == next_year_dt, y_column].sum()
            if global_stat_next:
                diff_next = ((global_stat - global_stat_next) / global_stat_next) * 100 
                diff_next_color = "blue" if diff_next > 0 else "red"
        else:
            global_stat_next = (tb_data.loc[tb_data["year_dt"] == next_year_dt, y_column].sum() / tb_data.loc[tb_data["year_dt"] == next_year_dt, 'e_pop_num'].sum()) * 100
            if global_stat_next:
                diff_next = global_stat - global_stat_next
                diff_next_color = "blue" if diff_next > 0 else "red"

    if selected_type == "absolute":
        # ,.0f will include a comma as the thousands separator
        global_stat = f"{global_stat:,.0f}"
        diff_previous_text = f"{diff_previous:+.1f}%" if diff_previous is not None else "data not available"
        diff_next_text = f"{diff_next:+.1f}%" if diff_next is not None else "data not available"
    else:
        global_stat = f"{global_stat:.5f}%"
        diff_previous_text = f"{diff_previous:+.5f}%" if diff_previous is not None else "data not available"
        diff_next_text = f"{diff_next:+.5f}%" if diff_next is not None else "data not available"

    return (
        global_stat,
        diff_previous_text,
        diff_next_text,
        diff_previous_color,
        diff_next_color,
        f"Global TB {selected_value.capitalize()}",
    )


# This has to be done in a separate callback than below
# Otherwise the rf-country-dropdown is not yet defined before we switch tabs


@callback(Output("rf-country-dropdown", "value"), Input("memory-output", "data"))
def update_dropdown(data):
    return data


# Returns a no_update if selected country is not none otherwise we enter a callback loop
@callback(
    Output("global-tab", "active_tab"),
    Output("memory-output", "data"),
    Input("geo_chart", "signalData"),
    prevent_initial_call=True,
)
def render_content(data):
    if data is not None and "selected_country" in data and data["selected_country"] and "country" in data["selected_country"] \
    and len(data["selected_country"]["country"]) > 0 :
        return ["tab-2", str(data["selected_country"]["country"][0])]
    else:
        return [no_update, "Canada"]


@callback(
    Output("tb-page", "children"),
    Input("global-tab", "active_tab"),
)
def render_content(tab):
    if tab == "tab-1":
        return world_component
    elif tab == "tab-2":
        return country_component


@callback(
    Output("tb_histogram", "spec"),
    [
        Input("year", "value"),
        Input("radio-1", "value"),
        Input("radio-2", "value"),
    ],
)
@callback(
    Output("geo_chart", "spec"),
    [
        Input("year", "value"),
        Input("radio-1", "value"),
        Input("radio-2", "value"),
    ],
)
def update_geofigure(selected_year, selected_type, selected_value):
    hover = alt.selection_point(on="mouseover", fields=["country"], empty=False)
    highlight = alt.selection_point(on="mouseover", fields=["country"])

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

    click = alt.selection_point(fields=["country"], name="selected_country")
    opacity = alt.condition(highlight, alt.value(0.8), alt.value(0.5))

    geo_chart = (
        alt.Chart(
            alt.topo_feature(world_url, "countries"), height=700, width="container"
        )
        .mark_geoshape(stroke="#aaa", strokeWidth=0.25, cursor="pointer")
        .encode(
            color=alt.Color(
                f"{y_column}:Q",
                title=f"{'Absolute' if selected_type == 'absolute' else 'Relative'} {'Incidence' if selected_value == 'incidence' else 'Mortality'}",
                scale=alt.Scale(scheme="plasma", type='log' if selected_type == 'absolute' else 'linear'),
                legend=alt.Legend(orient="none", titleAnchor="middle"),
            ),
            tooltip=[
                alt.Tooltip("country:N", title="Country"),
                alt.Tooltip(
                    field=y_column,
                    type="quantitative",
                    title=f"{'Relative' if selected_type == 'relative' else 'Absolute'} {'Incidence' if selected_value == 'incidence' else 'Mortality'}",
                    format=".1%" if selected_type == "relative" else "",
                )
            ],
            opacity=opacity,
            stroke=alt.condition(hover, alt.value("#03161C"), alt.value("#9BA4A7")),
            order=alt.condition(hover, alt.value(1), alt.value(0)),
        )
        .add_params(hover, click, highlight)
        .transform_lookup(
            lookup="id",
            from_=alt.LookupData(filtered_df, "iso_numeric", [y_column, "country"]),
        )
        .properties(height=800, width="container")
        .project(
        'equalEarth',
        scale=250
        )
    )

    background_map = alt.Chart(world_shp).mark_geoshape(color="lightgrey").project(scale=250)


    return ((background_map + geo_chart)).to_dict()


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
        [legends["e_mort_exc_tbhiv_num"], legends["e_inc_num"]],
    )

    # Create the line plot for TB Case Fatality Ratio
    case_fatality_ratio_fig = create_line_plot(
        filtered_data, "year", ["cfr"], [legends["cfr"]]
    )

    # Create the line plot for TB-HIV coinfection incidence and mortality
    hiv_coinfection_fig = create_line_plot(
        filtered_data,
        "year",
        ["e_mort_tbhiv_num", "e_inc_tbhiv_num"],
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
    
    order_age = ['0-4', '5-14', '15-24', 
                 '25-34', '35-44', '45-54', 
                 '55-64', '65plus']
    
    rff3['age_group'] = pd.Categorical(
        rff3['age_group'], 
        categories=order_age, ordered=True)

    rff3 = rff3.sort_values('age_group')

    fig = px.bar(
        rff3,
        x="age_group",
        y="best",
        color="sex",
        labels={
            "age_group": "Age Group",
            "best": "TB Incidence",
        },
        template="plotly_white",
        color_discrete_sequence=px.colors.qualitative.Bold,
    )

    fig.update_layout(margin={"l": 40, "b": 40, "t": 10, "r": 0}, hovermode="closest")

    # Custom legend labels
    custom_labels = {"m": "Male", "f": "Female"}

    for trace in fig.data:
        if trace.name in custom_labels:
            trace.name = custom_labels[trace.name]

    fig.update_layout(legend_title_text="Sex")

    return fig


@callback(Output("rf-pie-chart", "figure"), Input("rf-country-dropdown", "value"))
def update_pie_chart(country_value):
    # If no country is selected, do not update the chart
    if not country_value:
        raise PreventUpdate

    # Filter the data for the selected country
    country_data = preprocessed_rf_data[
        preprocessed_rf_data["country"] == country_value
    ]

    columns_except_country = [col for col in country_data.columns if col != "country"]

    # Prepare the data for the pie chart
    risk_factors_sums = country_data[columns_except_country].sum()

    # Create a dictionary for human-readable risk factor names
    risk_factor_names = {
        "all": "All",
        "alc": "Alcohol Use",
        "dia": "Diabetes",
        "hiv": "HIV",
        "smk": "Smoking",
        "und": "Undernourishment",
    }

    # Prepare the data for the pie chart with human-readable names
    pie_data = pd.DataFrame(
        {
            "Risk Factor": [
                risk_factor_names.get(x, x) for x in risk_factors_sums.index
            ],
            "Count": risk_factors_sums.values,
        }
    )

    # Create the pie chart using the aggregated data
    fig = px.pie(
        pie_data,
        names="Risk Factor",
        values="Count",
        color_discrete_sequence=px.colors.qualitative.Bold,
    )

    # Customize the layout of the pie chart
    fig.update_traces(textinfo="percent+label")
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


@callback(
    Output("modal", "is_open"),
    [Input("learn-more-open", "n_clicks"), Input("learn-more-close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
