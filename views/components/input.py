from dash import dcc, html
import dash_bootstrap_components as dbc

Dash_Input = html.Div(
    [
        dbc.Input(id="my-input", placeholder="Type something...", type="text"),
        html.Br(),
        html.P(id="output"),
    ]
)
