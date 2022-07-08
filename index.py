from app import app, server

from routes import render_page_content

from layout.sidebar.sidebar_callbacks import toggle_collapse, toggle_classname

from pages.forecast.forecast_callbacks import update_figure
#from pages.eda.eda_callbacks import make_graph
from pages.eda.eda_callbacks import generate_serie,definning_municipio
#,generate_pie,generate_bar,generate_mapa

from environment.settings import APP_HOST, APP_PORT, APP_DEBUG, DEV_TOOLS_PROPS_CHECK


if __name__ == "__main__":
    app.run_server(
        host=APP_HOST,
        port=APP_PORT,
        debug=APP_DEBUG,
        dev_tools_props_check=DEV_TOOLS_PROPS_CHECK
    )