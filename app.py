
from dash import Dash, html

from views.components.header import Dash_Header
from views.components.input import Dash_Input
from views.callbacks.demo import Demo

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    Dash_Header,
    Dash_Input,
    html.Br(),
    html.Div(id='my-output'),
    html.Div(
        children=html.Div([
            html.H5('Overview'),
            html.Div('''
                This is an example of a simple Dash app with
                local, customized CSS.
            ''')
        ])
    )
])

# Callbacks
Demo(app)
