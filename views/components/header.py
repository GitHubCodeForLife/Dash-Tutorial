from dash import dcc, html

Dash_Header = html.Div(
    [
        html.H2(
            "Live Model Training Viewer",
            id="title",
            className="eight columns",
            style={"margin-left": "3%"},
        ),
        html.Button(
            id="learn-more-button",
            className="two columns",
            children=["Learn More"],
        ),
        html.Img(
            src='/assets/image.png',
            className="two columns",
            id="plotly-logo",
        ),
    ],
    className="banner row",
)
