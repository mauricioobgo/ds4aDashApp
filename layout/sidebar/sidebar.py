
import dash_bootstrap_components as dbc
import dash_html_components as html

from utils.constants import home_page_location, forecast_page_location, eda_page_location

PLOTLY_LOGO = "https://i.postimg.cc/hPMpyfXR/Recurso-alta-4.png"

# we use the Row and Col components to construct the sidebar header
# it consists of a title, and a toggle, the latter is hidden on large screens

sidebar_header = dbc.Row(
    [
        
        dbc.Col(html.Img(src=PLOTLY_LOGO, style={"width": "10rem"})),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
            
        ),         
    ]

)

sidebar = html.Div(
    [
        sidebar_header,
        
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
                html.P(
                    "",
                    className="lead",
                ),
            ],
            id="blurb",
        ),        
           
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
           
            dbc.Nav(
                [
                    dbc.NavLink("HOME", href=home_page_location, active="exact"),
                    dbc.NavLink("EDA", href=eda_page_location, active="exact"),
                    dbc.NavLink("FORECAST", href=forecast_page_location, active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        is_open=False,
        ),
    ],
    id="sidebar",
)