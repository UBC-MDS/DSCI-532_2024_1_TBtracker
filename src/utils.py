import plotly.express as px

world_url = "https://vega.github.io/vega-datasets/data/world-110m.json"


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
