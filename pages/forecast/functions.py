import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')

#reading the models
area_harvested_model = pickle.load(open('data/area_harvested_model.pickle', 'rb'))
#production_model = pickle.load(open('data/production_model.pickle', 'rb'))
#yield_model = pickle.load(open('data/yield_model.pickle', 'rb'))

#forecasts
depts = ['code', 'amazonas', 'antioquia', 'arauca', 'atlantico', 'bolivar', 'boyaca', 'caldas', 'caqueta', 'casanare', 'cauca', 'cesar', 'choco', 'cordoba',
 'cundinamarca', 'guainia', 'guaviare', 'huila', 'la guajira', 'magdalena', 'meta', 'narino', 'norte de santander', 'putumayo', 'quindio', 'risaralda',
  'san andres y providencia', 'santander', 'sucre', 'tolima', 'valle del cauca', 'vaupes', 'vichada']
groups = ['cereales', 'fibras', 'flores y follajes', 'forestales', 'frutales', 'hongos', 'hortalizas', 'leguminosas', 'oleaginosas',
 'otros permanentes', 'otros transitorios', 'plantas aromaticas, condimentarias y medicinales', 'tuberculos y platanos']


def predict(area_seeded, dept, group, model):

    if model == "area_harvested_model":
        model = area_harvested_model
    elif model == "production_model":
        model = production_model
    elif model == "yield_model":
        model = yield_model
    else:
        raise Exception("Model not found")

    ex_dict = []
    for d in depts:
        for g in groups:
                ex_dict.append({'area_seeded': area_seeded, 'dept': d, 'group': g})
    ex = pd.DataFrame.from_dict(ex_dict)
    ex =pd.get_dummies(ex, columns= ['dept', 'group'], drop_first = False)
    bools = [x and y for x, y in zip(ex['dept_'+dept] == 1, ex['group_'+group] == 1)]
    ex = ex[bools]
    m = model.predict(n_periods=1, exogenous=ex)[0].sum()
    return(m)
def predict_depts(area_seeded, group, model):
    out_dict = []
    for d in depts:
        if d!= 'code':
            out_dict.append({'Department': d, 'Prediction': max(0,predict(area_seeded, d, group, model))})
    return(pd.DataFrame.from_dict(out_dict).sort_values(by='Prediction', ascending=False))
    
def predict_groups(area_seeded, dept, model):
    groups = []
    for var in list(area_harvested_model.params().index):
        if "group_" in var:
            groups.append(var.replace("group_",''))
    out_dict = []
    for g in groups:
        out_dict.append({'Group': g, 'Prediction': max(0,predict(area_seeded, dept, g, model))})
    return(pd.DataFrame.from_dict(out_dict).sort_values(by='Prediction', ascending=False)) 