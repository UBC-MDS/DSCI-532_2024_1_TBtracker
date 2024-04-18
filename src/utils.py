import plotly.express as px

world_url = "https://vega.github.io/vega-datasets/data/world-110m.json"


def create_line_plot(df, x_column, y_columns, legend_names, title=""):
    plot_df = df.copy()

    # Rename the columns for the legend
    for original_col, new_name in zip(y_columns, legend_names):
        plot_df[new_name] = plot_df[original_col]

    # Create the figure using the new column names for y-values
    fig = px.line(
        plot_df,
        x=x_column,
        y=legend_names,
        color_discrete_sequence=px.colors.qualitative.Bold,
        title=title,
    )
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Count",
        legend=dict(
            title="",
            title_font=dict(size=10),
            font=dict(size=14),
            x=1,  # Horizontally align to the right
            y=1.05,  # Vertically align to the top
            orientation="h",
            yanchor="bottom",
            xanchor="right",
        ),
        plot_bgcolor="white",
    )

    # Optionally remove the original column names from the hover data
    fig.update_traces(hovertemplate=None)

    return fig


def update_card_content(scale, variable):
    # Logic to create content based on scale and variable
    if variable == "incidence":
        text = "Incidence"
    else:
        text = "Mortality"

    if scale == "absolute":
        text += " in Absolute Numbers"
    else:
        text += " in Relative Numbers"

    return text
