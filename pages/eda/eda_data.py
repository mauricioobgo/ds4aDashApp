import pandas as pd

from sklearn import datasets
import boto3
import pandas as pd
import unidecode
from app import cache
from utils.constants import TIMEOUT
import geopandas as gpd

@cache.memoize(timeout=TIMEOUT)
def simple_text(data):
    data= unidecode.unidecode(data)
    return data
def load_process_data():
    EVA=pd.read_csv('data/data_eva.csv')
    return  EVA

def load_municipios():
    municipios = gpd.read_file('data/muncipios.geojson')
    municipios['Código del Municipio'] =municipios['MPIO_CCNCT'].astype(int)
    return municipios

def load_depanum():
    depa_mun = pd.read_csv('data/department_municipios.csv')
    return depa_mun

def load_years():
    years_load=pd.read_csv('data/years.csv')
    return years_load

def load_cultivos():
    cultivos=pd.read_csv('data/cultivos.csv')
    return cultivos

def convert_to_list(value_convert):
    listall=[]
    if type(value_convert)!=list:
        listall.append( value_convert)
    else:
        listall=value_convert
    return listall


