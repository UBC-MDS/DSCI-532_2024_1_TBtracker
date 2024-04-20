import plotly.express as px

world_url = "https://vega.github.io/vega-datasets/data/world-110m.json"


def create_line_plot(df, x_column, y_columns, legend_names, title=""):
    """
    Create a line plot with custom legend names and an optional title.

    Parameters
    ----------
    df : DataFrame
        Pandas DataFrame containing the data to plot.
    x_column : str
        Name of the column in DataFrame to be used as the x-axis.
    y_columns : list of str
        List of column names in DataFrame that are to be plotted on the y-axis.
    legend_names : list of str
        List of names that will appear in the legend, corresponding to `y_columns`.
    title : str, optional
        Title of the plot. Default is an empty string.

    Returns
    -------
    figure
        A Plotly Express line plot object configured with the specified parameters.
    """
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
    """
    Create descriptive text for a card based on the scale and variable of interest.

    Parameters
    ----------
    scale : str
        The scale of data presentation, either 'absolute' or 'relative'.
    variable : str
        The variable of interest, either 'incidence' or 'mortality'.

    Returns
    -------
    str
        Descriptive text that combines the scale and variable information.
    """

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
