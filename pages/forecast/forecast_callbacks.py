
from dash.dependencies import Input, Output
import pages.forecast.functions as models_selector
import plotly.express as px
from pages.eda.eda_data import load_depanum,load_years,load_cultivos,load_process_data,load_municipios,convert_to_list
from app import app
from pages.forecast.forecast_data import dataframe
from components.table import make_dash_table

models_list= ["area_harvested_model", "production_model", "yield_model"]
# @app.callback(
#     Output('graph-with-slider', 'figure'),
#     Input('year-slider', 'value'))
# def update_figure(selected_year):
#     forecast_data = dataframe()
#     filtered_df = forecast_data[forecast_data.year == selected_year]

#     fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
#                      size="pop", color="continent", hover_name="country",
#                      log_x=True, size_max=55)

#     fig.update_layout(transition_duration=500)

#     return fig

@app.callback(
    Output('table_manager', 'Children'),
    Input('dropdown_departamento', 'value'),
    Input('input_hect', 'value'),
    Input('radioitems-inline-input', 'value')
    )
def update_figure(departamento,hectareas,modelo):
    models= models_list[modelo]
    prediction=models_selector.predict_groups(hectareas, departamento, models).head(10)
    return make_dash_table(prediction)

@app.callback(
    Output('table_manager', 'Children'),
    Input('dropdown_groups', 'value'),
    Input('input_hect', 'value'),
    Input('radioitems-inline-input', 'value')
    )
def update_figure(group,hectareas,modelo):
    models= models_list[modelo]
    prediction=models_selector.predict_groups(hectareas, group, models).head(10)
    return make_dash_table(prediction)