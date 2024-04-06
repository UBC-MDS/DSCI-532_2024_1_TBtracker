from src.app import layout as main_layout
import os
src_path = os.path.abspath(os.path.dirname(__file__))

from dash import Dash
import dash_bootstrap_components as dbc

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.layout = main_layout

# Check if the file is executed as main (useful for running the server from this file if needed)
if __name__ == "__main__":
    app.run_server(port=8000, host="127.0.0.1",
                   debug=True, dev_tools_hot_reload=True)
