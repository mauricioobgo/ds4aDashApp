import dash_html_components as html
import dash_bootstrap_components as dbc

header=dbc.Container(
    [
        dbc.Row(
        [
            dbc.Col([html.Img(src="https://i.postimg.cc/V69MpLbk/Simple-Badge-Agriculture-Farm-Circle-Logo-1.png", style={"width": 55})],sm=2, width=2, align="center"),
            dbc.Col([html.H3("PREDICTION MODEL TO SELECT THE BEST CROP OR LOCATION IN COLOMBIA")], sm=8, width= 8,  align="center"),
            dbc.Col([html.Img(src="https://i.postimg.cc/9f0kHvLH/Recurso-alta-4-logo-2.png", style={"width": 55})], sm=2, width=2, align="center"),
        ]
        ),
    ],
    fluid=True,
)