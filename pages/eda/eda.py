import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from pages.header import *
from app import app
from dash.dependencies import Input, Output
#from pages.eda.eda_data import dataframe
#from components.table import make_dash_table
from pages.eda.eda_data import load_depanum,load_years,load_cultivos,load_process_data

depamun_df=load_depanum()
years_df=load_years()
cultivos_df=load_cultivos()

controls = dbc.Card(
    [
        dbc.Form(
            [
            dbc.FormGroup(
                [
                    dbc.Label("Departamento"),
                    dcc.Dropdown(
                        id="departamento",
                        options=[
                            {"label": col, "value": col} for col in depamun_df['Departamento'].unique()
                        ],
                        value=None,
                        multi=True,
                        persistence_type='memory',
                    ),
                ],
            ),
            dbc.FormGroup(
                [
                    dbc.Label("Municipio"),
                    dcc.Dropdown(
                        id="municipio",
                        multi=True,
                    ),
                ],
            ),
            dbc.FormGroup(
                [
                    dbc.Label("Año"),
                    dcc.Dropdown(
                        id="year",
                        options=[
                            {"label": col, "value": col} for col in years_df.year.to_list()
                        ],
                        value='Todos',
                        multi=True,

                    ),
                ],
            ),
            dbc.FormGroup(
                [
                    dbc.Label("Metrica"),
                    dcc.Dropdown(
                        id="metrica",
                        options=[
                            {"label": "Area Sembrada (ha)", "value": "Area Sembrada (ha)"} ,
                            {"label": "Area Cosechada (ha)", "value": "Area Cosechada (ha)"} ,
                            {"label": "% Area municipal sembrada", "value": "% Area municipal sembrada"} ,
                            {"label": "% Area municipal cosechada", "value": "% Area municipal cosechada"}  
                        ],
                        value="Area Sembrada (ha)",

                    ),
                ],
            ),
            dbc.FormGroup(
                [
                    dbc.Label("Cultivo"),
                    dcc.Dropdown(
                        id="cultivo",
                        options=[
                            {"label": col, "value": col} for col in cultivos_df.Cultivo.to_list()
                        ],
                        value=None,
                        multi=True
                    ),
                ],
            ),
        ]
        ),
    ],
    body=True,
)

layout = dbc.Container(
    [
        header,
        html.H1("EXPLORATORY DATA ANALYSIS"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dbc.Col(dcc.Graph(id="generate_serie"), md=8),
            ],
            align="center",
        ),
        html.Hr(),
        dbc.Row([
            dbc.Col(
                children=[dcc.Graph(id="generate_pie")], 
                md=6
                ),
            dbc.Col(
                children=[dcc.Graph(id="generate_bar")]
                , md=6
                )
        ]),
        dbc.Row([
            dbc.Col(
                children=[dcc.Graph(id="generate_map")], 
                )
        ])
        #     dbc.Col(make_dash_table(dataframe()), width={"size": 8, "offset": 3}),
        #     align="center",
        
        # dcc.Store(id='local_depanm', data=load_depanum().to_dict('records'),storage_type='local'),
        # dcc.Store(id='df_graphs', data=load_process_data().to_dict('records'),storage_type='memmory')

    ],
    fluid=True,
)

# layout = html.Div(
#  children=[
#     ### Header
    
#     html.Div(
#             children=[
#             html.H4('Analysis of municipal Crops ', className="Title"),
#             ]),
#     ## Filters
#     html.Div(
#         children=[
#             html.Div(
#             children=[
#             html.Div(children="Año:", className="menu-title"),
#                 dcc.Dropdown(id='year',
#                     options=[],
#                     value='Todos', clearable=False,multi=True,
#                     style={
#                                 'width':'40%',
#                                 "display": "inline-block",
#                                 'margin-right': 10
#                                 # 'padding-left':'25%',
#                                 # 'padding-right':'25%',
#                                 #display= "inline-block"
#                     })
#             ]),
#             html.Div(
#             children=[
#             html.Div(children="Departamento", className="menu-title"),
#                 dcc.Dropdown(id='departamento',
#                     options=[],
#                     value='Todos', clearable=False,multi=True,
#                     style={
#                                 'width':'40%',
#                                 "display": "inline-block",
#                                 'margin-right': 10
#                                 # 'padding-left':'25%',
#                                 # 'padding-right':'25%',
#                                 #display= "inline-block"
#                     })
#             ]),
#             html.Div(
#             children=[
#             html.Div(children="Municipio", className="menu-title"),
#                 dcc.Dropdown(id='municipio',
#                     options=[],
#                     value='Todos', clearable=False,multi=True,
#                     style={
#                                 'width':'40%',
#                                 "display": "inline-block",
#                                 'margin-right': 10
#                                 # 'padding-left':'25%',
#                                 # 'padding-right':'25%',
#                                 # 'vertical-align': 'top'
#                                 #display= "inline-block"
#                     })
#             ]),
#             html.Div(
#             children=[
#             html.Div(children="Cultivo:", className="menu-title"),
#                 dcc.Dropdown(id='cultivo',
#                     options=[],
#                     value='Todos', clearable=False,multi=True,
#                     style={
#                                 'width':'40%',
#                                 "display": "inline-block",
#                                 'margin-right': 10
#                                 # 'padding-left':'25%',
#                                 # 'padding-right':'25%',
#                                 # 'vertical-align': 'top'
#                                 #display= "inline-block"
#                     })
#             ]),
            
            
#             html.Div(
#             children=[
#             html.Div(children="Metrica:", className="metrica"),
#                 dcc.Dropdown(id='metrica',
#                     options=["Area Sembrada (ha)","Area Cosechada (ha)","% Area municipal sembrada","% Area municipal cosechada"],
#                     value="% Area municipal sembrada", clearable=False,
#                     style={
#                                 'width':'40%',
#                                 "display": "inline-block",
#                                 'margin-right': 10
#                                 # 'padding-left':'25%',
#                                 # 'padding-right':'25%',
#                                 # 'vertical-align': 'top'
#                                 #display= "inline-block"
#                     })
#             ]),
#             html.Div(
#             children=[
#             html.Div(children="Nivel de agregacion:", className="metrica"),
#                 dcc.Dropdown(id='agregacion',
#                     options=['Departamento','Municipio',"Cultivo"],
#                     value='Departamento', clearable=False,
#                     style={
#                                 'width':'40%',
#                                 "display": "inline-block",
#                                 'margin-right': 10
#                                 # 'padding-left':'25%',
#                                 # 'padding-right':'25%',
#                                 # 'vertical-align': 'top'
#                                 #display= "inline-block"
#                     })
#             ]),
#         ]),
    

#     ## Mapa
#     # html.Div(
#     # children=[
#     # dcc.Graph(id="map"),
#     # ]),      
        
        
#     ## PIe, barras y series
#     html.Div(
#     children=[
#     dcc.Graph(id="serie")
#     #dcc.Graph(id="pie"),
#     #dcc.Graph(id="bar"),
#     ]),
    

# ])


