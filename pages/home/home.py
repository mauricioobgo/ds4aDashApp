import dash_html_components as html
import dash_bootstrap_components as dbc
danny = dbc.Card(
    [
        dbc.CardImg(src="https://i.postimg.cc/yx5Qnr2j/DANNY-SANCHEZ-min.jpg",  top=True),
        dbc.CardBody(
            [
                html.H4("Danny Sanchez", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("sitio web", href="https://dajasaba.art/", target="_blank", color="primary"),
            ]
        ),
    ],
    style={"width": "12rem"},
)

guillermo = dbc.Card(
    [
        dbc.CardImg(src="https://i.postimg.cc/yx5Qnr2j/DANNY-SANCHEZ-min.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Guillermo Velez", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", href="https://dajasaba.art/", target="_blank", color="primary"),
            ]
        ),
    ],
    style={"width": "12rem"},
)

jaime = dbc.Card(
    [
        dbc.CardImg(src="https://i.postimg.cc/yx5Qnr2j/DANNY-SANCHEZ-min.jpg",  top=True),
        dbc.CardBody(
            [
                html.H4("Jaime Delgado", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("sitio web", href="https://dajasaba.art/", target="_blank", color="primary"),
            ]
        ),
    ],
    style={"width": "12rem"},
)

jehider = dbc.Card(
    [
        dbc.CardImg(src="https://i.postimg.cc/yx5Qnr2j/DANNY-SANCHEZ-min.jpg",  top=True),
        dbc.CardBody(
            [
                html.H4("Jehider   Pinto", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("sitio web", href="https://dajasaba.art/", target="_blank", color="primary"),
            ]
        ),
    ],
    style={"width": "12rem"},
)

joseph = dbc.Card(
    [
        dbc.CardImg(src="https://i.postimg.cc/yx5Qnr2j/DANNY-SANCHEZ-min.jpg",  top=True),
        dbc.CardBody(
            [
                html.H4("Joseph Martinez", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("sitio web", href="https://dajasaba.art/", target="_blank", color="primary"),
            ]
        ),
    ],
    style={"width": "12rem"},
)

mauricio = dbc.Card(
    [
        dbc.CardImg(src="https://i.postimg.cc/yx5Qnr2j/DANNY-SANCHEZ-min.jpg",  top=True),
        dbc.CardBody(
            [
                html.H4("Mauricio Obando", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("sitio web", href="https://dajasaba.art/", target="_blank", color="primary"),
            ]
        ),
    ],
    style={"width": "12rem"},
)

nicolas = dbc.Card(
    [
        dbc.CardImg(src="https://i.postimg.cc/yx5Qnr2j/DANNY-SANCHEZ-min.jpg",  top=True),
        dbc.CardBody(
            [
                html.H4("Nicolas Cristancho", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("sitio web", href="https://dajasaba.art/", target="_blank", color="primary"),
            ]
        ),
    ],
    style={"width": "12rem"},
)

the_project = dbc.Card(
    dbc.CardBody(
        [
            html.H4("The Project", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text",
            ),
            dbc.CardLink("Card link", href="#"),
            dbc.CardLink("External link", href="https://google.com"),
        ]
    ),
    style={"width": "auto"},
)

the_sources = dbc.Card(
    dbc.CardBody(
        [
            html.H4("The Sources", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text",
            ),
            dbc.CardLink("Card link", href="#"),
            dbc.CardLink("External link", href="https://google.com"),
        ]
    ),
    style={"width": "auto"},
)

the_team = dbc.Card(
    dbc.CardBody(
        [
            html.H4("The Team", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text",
            ),
            dbc.CardLink("Card link", href="#"),
            dbc.CardLink("External link", href="https://google.com"),
        ]
    ),
    style={"width": "auto"},
)



layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Img(src="https://i.postimg.cc/3rSvzYJv/Recurso-alta-1.png", style={"width": "10rem"})),
                dbc.Col(html.H2("DS4A FINAL PROJECT TITLE"), style={"width": "auto"}),
                dbc.Col(html.Img(src="https://i.postimg.cc/V69MpLbk/Simple-Badge-Agriculture-Farm-Circle-Logo-1.png", style={"width": "5rem"})),
            ]
        ),

        dbc.Row(dbc.Col(the_project, width="auto"),className="mt-4"),
        dbc.Row(dbc.Col(the_sources, width="auto"),className="mt-4"),
        dbc.Row(dbc.Col(the_team, width="auto"),className="mt-4"),       
        dbc.Row(
            [
                dbc.Col(danny, width="auto"),
                dbc.Col(guillermo, width="auto"),
                dbc.Col(jaime, width="auto"),
                dbc.Col(jehider, width="auto"),              
            ],className="mt-4"
        ),
        dbc.Row(
            [
                dbc.Col(joseph, width="auto"),
                dbc.Col(mauricio, width="auto"),
                dbc.Col(nicolas, width="auto"),
            ],className="mt-4"
        ),

    ]
),
        