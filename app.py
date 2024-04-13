import dash_bootstrap_components as dbc
from dash import Dash
from src.components.world import global_layout
from src.callbacks import *

# Initialize Dash app
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    title="Tb tracker",
)
server = app.server
app.layout = global_layout


# Check if the file is executed as main (useful for running the server from this file if needed)
if __name__ == "__main__":
    app.run(port=8000, host="127.0.0.1", debug=True, dev_tools_hot_reload=True)
