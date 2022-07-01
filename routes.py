import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

from utils.constants import home_page_location, forecast_page_location, eda_page_location

from pages.home import home
from pages.forecast import forecast
from pages.eda import eda



@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == home_page_location:
        return home.layout
    elif pathname == forecast_page_location:
        return forecast.layout
    elif pathname == eda_page_location:
        return eda.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )