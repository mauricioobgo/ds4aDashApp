import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from pages.header import *
from pages.forecast.forecast_data import dataframe
from pages.forecast.inputs import *


###tab to predict by Location
by_location= dbc.Card(
    dbc.CardBody(
        [
            html.P("PREDICT BY LOCATION", className="card-text"),
            dbc.Row(
            [            
                dbc.Col(
                    [
                        html.P( "The model predicts the best crop group for the selected department"),
                        input2_1,
                    ]

                ),
            ]
        ),
        ]
    ),
    className="mt-3",
),

###tab to select by crop group 
by_group = dbc.Card(
    dbc.CardBody(
        [
            html.P("PREDICT BY CROP GROUP", className="card-text"),
            dbc.Row(
            [            
                dbc.Col(
                    [
                        html.P( "The model predicts the best department for the selected selected crop group"),
                        input2_2,
                    ]

                ),
            ]
        ),
        ]
    ),
    className="mt-3",
),

tabs = dbc.Tabs(
    [
        dbc.Tab(by_location, label="Tab 1"),
        dbc.Tab(by_group, label="Tab 2"),
    ],
),


layout = html.Div(
    [
        header,
        html.H3("PREDICTION MODELS"),
        html.Hr(),
        html.P("To begin you must Select your inputs"),
        input0,
        input1,
        html.Hr(),
        tabs,
    ]
)




dbc.Row(
            [
                
                dbc.Col(
                    [
                        dcc.Graph(id='graph-with-slider'),
                        dcc.Slider(
                            id='year-slider',
                            min=dataframe()['year'].min(),
                            max=dataframe()['year'].max(),
                            value=dataframe()['year'].min(),
                            marks={str(year): str(year) for year in dataframe()['year'].unique()},
                            step=None
                        ),
                    ]
                ),
                dbc.Col(
                    [
                        html.Thead(html.Tr([html.Th("First Name"), html.Th("Last Name")])),
                        
                        html.P(
                            "Some quick example text to build on the card title and "
                            "make up the bulk of the card's content."
                        ),
                    ],
                ),
            ],
        ),