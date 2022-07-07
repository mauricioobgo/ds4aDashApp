
from dash.dependencies import Input, Output
import geopandas as gpd
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from sklearn.cluster import KMeans
import dash_core_components as dcc
import boto3
from app import app
#from pages.eda.eda_data import dataframe
from pages.eda.eda_data import load_depanum,load_years,load_cultivos,load_process_data,load_municipios,convert_to_list

df=load_process_data()
municipios=load_municipios()[['Código del Municipio','geometry']]

## series
@app.callback(
    Output("generate_serie", "figure"), 
    Input("year", "value"),
    Input("departamento", "value"),
    Input("municipio", "value"),
    Input("metrica", "value"),
    Input("cultivo", "value")
    )
def generate_serie( year, departamento,municipio,metrica,cultivo):
    years=convert_to_list(year)
    department=convert_to_list(departamento)
    municipio_n=convert_to_list(municipio)
    cultivo_n=convert_to_list(cultivo)

    ser_df=df[ (df['Cultivo'].isin(cultivo_n)) & (df['Año'].isin(years)) & (df['Departamento'].isin(department)) & (df['Municipio'].isin(municipio_n)) ]
    ser_df= ser_df.groupby('Año').sum().reset_index()
    fig = px.line(ser_df, x='Año', y=metrica,color_discrete_sequence=list(reversed(px.colors.sequential.Greens))[1:])
    fig.update_layout(transition_duration=500)
    return fig

# ## Pie
## series
@app.callback(
    Output("generate_pie", "figure"), 
    Input("year", "value"),
    Input("departamento", "value"),
    Input("municipio", "value"),
    Input("metrica", "value"),
    Input("cultivo", "value")
    )
def generate_pie( year, departamento,municipio,metrica,cultivo):
    years=convert_to_list(year)
    department=convert_to_list(departamento)
    municipio_n=convert_to_list(municipio)
    cultivo_n=convert_to_list(cultivo)

    pie_df=df[ (df['Cultivo'].isin(cultivo_n)) & (df['Año'].isin(years)) & (df['Departamento'].isin(department)) & (df['Municipio'].isin(municipio_n)) ]
    fig = px.pie(pie_df, values=metrica, names='Departamento', hole=.3,color_discrete_sequence=list(reversed(px.colors.sequential.Greens))[1:])
    fig.update_layout(transition_duration=500)
    return fig



@app.callback(
    Output("generate_bar", "figure"), 
    Input("year", "value"),
    Input("departamento", "value"),
    Input("municipio", "value"),
    Input("metrica", "value"),
    Input("cultivo", "value")
    )
def generate_bar( year, departamento,municipio,metrica,cultivo):
    years=convert_to_list(year)
    department=convert_to_list(departamento)
    municipio_n=convert_to_list(municipio)
    cultivo_n=convert_to_list(cultivo)
    
    bar_df=df[ (df['Cultivo'].isin(cultivo_n)) & (df['Año'].isin(years)) & (df['Departamento'].isin(department)) & (df['Municipio'].isin(municipio_n)) ]
    fig = px.box(bar_df[['Departamento','Municipio',metrica]], x='Municipio', y=metrica, notched=True)
    fig.update_layout(transition_duration=500)
    return fig


@app.callback(
    Output("generate_map", "figure"), 
    Input("year", "value"),
    Input("departamento", "value"),
    Input("municipio", "value"),
    Input("metrica", "value"),
    Input("cultivo", "value")
    )
def generate_map( year, departamento,municipio,metrica,cultivo):
    years=convert_to_list(year)
    department=convert_to_list(departamento)
    municipio_n=convert_to_list(municipio)
    cultivo_n=convert_to_list(cultivo)
    
    geo_modifcation=df[ (df['Cultivo'].isin(cultivo_n)) & (df['Año'].isin(years)) & (df['Departamento'].isin(department)) & (df['Municipio'].isin(municipio_n)) ]
    geo_modifcation= geo_modifcation.groupby('Código del Municipio').sum().reset_index()
    gdf = pd.merge(geo_modifcation,municipios[['Código del Municipio','geometry']], on ='Código del Municipio', how='left')
    gdf= gpd.GeoDataFrame(gdf, geometry ='geometry')
    gdf=gdf.set_index('Código del Municipio')
    fig = px.choropleth_mapbox(gdf, geojson=gdf['geometry'], locations=gdf.index, color=metrica,color_continuous_scale=px.colors.sequential.Greens[1:],
                               mapbox_style="carto-positron",zoom=4.5, center = {"lat": 5.45, "lon": -73.36})
    fig.update_geos(fitbounds="locations", visible=False)
    return fig

# @app.callback(
#     Output("pie", "figure"), 
#     Input("agregacion", "value"), 
#     Input("metrica", "value"),
#     Input("year", "value"),
#     Input("departamento", "value"),
#     Input("municipio", "value"),
#     Input("cultivo", "value"),
    
#     )
# def generate_pie(agregacion, metrica, year, departamento,municipio,cultivo):
#     pie_df = df.copy()
#     if cultivo != 'Todos':
#         pie_df=  pie_df[(pie_df['Cultivo']==cultivo)]
#     if year != 'Todos':
#         pie_df=  pie_df[(pie_df['Año']==year)]
#     if departamento != 'Todos':
#         pie_df=  pie_df[(pie_df['Departamento']==departamento)]
#     if municipio != 'Todos':
#         pie_df=  pie_df[(pie_df['Municipio']==municipio)]
#     fig = px.pie(pie_df, values=metrica, names=agregacion, hole=.3,color_discrete_sequence=list(reversed(px.colors.sequential.Greens))[1:])
#     return fig

# ## barras
# @app.callback(
#     Output("bar", "figure"), 
#     Input("agregacion", "value"), 
#     Input("metrica", "value"),
#     Input("year", "value"),
#     Input("departamento", "value"),
#     Input("municipio", "value"),
#     Input("cultivo", "value"),
    
#     )
# def generate_bar(agregacion, metrica, year, departamento,municipio,cultivo):
#     bar_df = df.copy()
#     if cultivo != 'Todos':
#         bar_df=  bar_df[(bar_df['Cultivo']==cultivo)]
#     if year != 'Todos':
#         bar_df=  bar_df[(bar_df['Año']==year)]
#     if municipio != 'Todos':
#         bar_df=  bar_df[(bar_df['Municipio']==municipio)]
#     if departamento != 'Todos':
#         bar_df=  bar_df[(bar_df['Departamento']==departamento)]
#     fig = px.box(bar_df, x=agregacion, y=metrica, color="Departamento", notched=True)
#     return fig

# ## Mapa
# @app.callback(
#     Output("map", "figure"), 
#     Input("agregacion", "value"), 
#     Input("metrica", "value"),
#     Input("year", "value"),
#     Input("departamento", "value"),
#     Input("municipio", "value"),
#     Input("cultivo", "value"),
    
#     )
# def generate_mapa(agregacion, metrica, year, departamento,municipio,cultivo):
#     gdf = df.copy()
#     if cultivo != 'Todos':
#         gdf=  gdf[(gdf['Cultivo']==cultivo)]
#     if year != 'Todos':
#         gdf=  gdf[(gdf['Año']==year)]
#     if departamento != 'Todos':
#         gdf=  gdf[(gdf['Departamento']==departamento)]
#     if municipio != 'Todos':
#         gdf=  gdf[(gdf['Municipio']==municipio)]
#     gdf= gdf.groupby('Código del Municipio').sum().reset_index()
#     gdf = pd.merge(gdf,municipios[['Código del Municipio','geometry']], on ='Código del Municipio', how='left')
#     gdf= gpd.GeoDataFrame(gdf, geometry ='geometry')
#     gdf=gdf.set_index('Código del Municipio')
#     fig = px.choropleth_mapbox(gdf, geojson=gdf['geometry'], locations=gdf.index, color=metrica,color_continuous_scale=px.colors.sequential.Greens[1:],
#                                mapbox_style="carto-positron",zoom=4.5, center = {"lat": 5.45, "lon": -73.36})
#     fig.update_geos(fitbounds="locations", visible=False)
#     return fig

## data_storing filters
@app.callback(
    Output(component_id="municipio", component_property="options"),
    Input(component_id="departamento", component_property="value"),
    )
def definning_municipio(departamento):
    print(departamento)
    dataframe=load_depanum()
    if type(departamento)==list:
        list_municipios=dataframe[dataframe['Departamento'].isin(departamento)]['Municipio']
    else:
        list_municipios=dataframe[dataframe['Departamento']==departamento]['Municipio']
    return [{'label': i, 'value': i} for i in list_municipios.to_list()]
    



