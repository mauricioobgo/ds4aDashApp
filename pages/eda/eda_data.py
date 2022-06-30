import pandas as pd

from sklearn import datasets

from app import cache
from utils.constants import TIMEOUT


@cache.memoize(timeout=TIMEOUT)
def query_data():
    # This could be an expensive data querying step
    eda_raw = datasets.load_iris()
    eda = pd.DataFrame(eda_raw["data"], columns=eda_raw["feature_names"])
    return eda.to_json(date_format='iso', orient='split')

def dataframe():    
    return pd.read_json(query_data(), orient='split')