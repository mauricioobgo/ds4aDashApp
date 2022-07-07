import dash_html_components as html
import dash_bootstrap_components as dbc
from pages.header import *

danny = dbc.Card(
    [
        dbc.CardImg(src="https://i.postimg.cc/yx5Qnr2j/DANNY-SANCHEZ-min.jpg",  top=True),
        dbc.CardBody(
            [
                html.H4("Danny Sanchez", className="card-title"),
                html.P(
                    "Mechanical engineer with 10 years of experience in project management, visual artist and Data Science enthusiastic",
                    className="card-text",
                ),
                dbc.Button("sitio web", href="https://dajasaba.art/", target="_blank", color="primary"),
            ]
        ),
    ],
    style={"width": "auto"},
)

guillermo = dbc.Card(
    [
        dbc.CardImg(src="https://i.postimg.cc/Pr475DpJ/guillermo.png", top=True),
        dbc.CardBody(
            [
                html.H4("Guillermo Velez", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Linkedin", href="https://www.linkedin.com/in/guillermo-jos%C3%A9-velez-loaiza-87833a55/", target="_blank", color="primary"),
            ]
        ),
    ],
    style={"width": "auto"},
)

jaime = dbc.Card(
    [
        dbc.CardImg(src="https://i.postimg.cc/P5VFmkMk/jaime.png",  top=True),
        dbc.CardBody(
            [
                html.H4("Jaime Delgado", className="card-title"),
                html.P(
                    "Civil engineer. Master in Educational Technology Management. Experience in drawing structures in Autocad and Civil3D. Teaching experience. Currently reinforcing programming skills and learning Data Science.",
                    className="card-text",
                ),
                dbc.Button("Linkedin", href="https://www.linkedin.com/in/jaime--delgado", target="_blank", color="primary"),
            ]
        ),
    ],
    style={"width": "auto"},
)

jehider = dbc.Card(
    [
        dbc.CardImg(src="https://i.postimg.cc/d07N6SWZ/Jehider.png",  top=True),
        dbc.CardBody(
            [
                html.H4("Jehider   Pinto", className="card-title"),
                html.P(
                    "Petroleum Engineer recently graduated from the National University of Colombia. Emphasis in the area of reservoirs and data science. ",
                    className="card-text",
                ),
                dbc.Button("Linkedin", href="http://www.linkedin.com/in/jehider-pinto-montes", target="_blank", color="primary"),
            ]
        ),
    ],
    style={"width": "auto"},
)

joseph = dbc.Card(
    [
        dbc.CardImg(src="https://i.postimg.cc/pX78nNX3/joseph.png",  top=True),
        dbc.CardBody(
            [
                html.H4("Joseph Martinez", className="card-title"),
                html.P(
                    "Honors Industrial Engineering with knowledge in statistics; data analysis; machine learning models; Social Network Analysis and Natural Language Processing",
                    className="card-text",
                ),
                dbc.Button("LinkedIn", href="https://www.linkedin.com/in/joseph-martinez-/", target="_blank", color="primary"),
            ]
        ),
    ],
    style={"width": "auto"},
)

mauricio = dbc.Card(
    [
        dbc.CardImg(src="https://i.postimg.cc/sggNQ27c/Mauricio.png",  top=True),
        dbc.CardBody(
            [
                html.H4("Mauricio Obando", className="card-title"),
                html.P(
                    "Mathematics student Konrad Lorenz Foundation. He works as a backend developer at Globant.",
                    className="card-text",
                ),
                dbc.Button("GitHub", href="https://github.com/mauricioobgo", target="_blank", color="primary"),
            ]
        ),
    ],
    style={"width": "auto"},
)

nicolas = dbc.Card(
    [
        dbc.CardImg(src="https://i.postimg.cc/DfW6mc7j/nicolas.png",  top=True),
        dbc.CardBody(
            [
                html.H4("Nicolas Cristancho", className="card-title"),
                html.P(
                    "Economist and data scientist. Experience in AI modeling with satellite images and impact assessments",
                    className="card-text",
                ),
                dbc.Button("Linkedin", href="https://www.linkedin.com/in/nicolas-cristancho-bbba96205/", target="_blank", color="primary"),
            ]
        ),
    ],
    style={"width": "auto"},
)

the_project = dbc.Card(
    dbc.CardBody(
        [
            html.H4("The Project", className="card-title"),
            
            html.P(
                "The proposal is based on building a model capable of predicting either which crops and/or which location will have a higher efficiency in terms of production per unit of land. ",
                
                className="card-text",
            ),
            html.P(
                "Agriculture industry is a key to the Colombian economy. it not only 	provides jobs to millions (about 20 percent from total) but it represents an important slice in the country GDP and almost 15 percent of total exports despite the fact that less than 5 percent of the territory is used for crops. ",
               
                className="card-text",
            ),
            html.P(
                "Agriculture industry in Colombia is facing some challenges as climate change is affecting the agriculture industry in the entire country, affecting the efficiency in production. Volatility in their costs and prices and a strong competition with external markets gives a higher risk to investors and, Colombia investment in agriculture (11,6 percent) is below the OCDE mean value (16,8 percent)",
                className="card-text",
            ),
        ],
    ),
    style={"width": "auto"},
)

the_sources = dbc.Card(
    dbc.CardBody(
        [
            html.H4("The Sources", className="card-title"),
            html.H6("Municipal Agricultural Evaluations 2006-2020", className="card-subtitle"),
            html.P(
                "Municipal Agricultural Evaluations 2006-2020: information on national agricultural production. This dataset has detailed information on agricultural production, it is a panel dataset with description details of the production cycle, type of crop and yield.",
                className="card-text",
            ),
            dbc.CardLink("Municipal Agricultural Evaluations", href="https://www.datos.gov.co/Agricultura-y-Desarrollo-Rural/Evaluaciones-Agropecuarias-Municipales-EVA/2pnw-mmge/data"),
        ]
    ),
    style={"width": "auto"},
)

the_team = dbc.Card(
    dbc.CardBody(
        [
            html.H4("The Team", className="card-title"),
        ]
    ),
    style={"width": "auto"},
)



layout = dbc.Container(    
    [
        header,
        html.Hr(),
        dbc.Row(dbc.Col(the_project, width="auto"),className="mt-4"),
        dbc.Row(dbc.Col(the_sources, width="auto"),className="mt-4"),
        dbc.Row(dbc.Col(the_team, width="auto"),className="mt-4"),       
        dbc.Row(
            [
                dbc.Col(danny, width=3),
                dbc.Col(guillermo, width=3),
                dbc.Col(jaime, width=3),
                dbc.Col(jehider, width=3),              
            ],className="mt-4"
        ),
        dbc.Row(
            [
                dbc.Col(joseph, width=3),
                dbc.Col(mauricio, width=3),
                dbc.Col(nicolas, width=3),
            ],className="mt-4"
        ),
        
    ],
    fluid=True,
)
        