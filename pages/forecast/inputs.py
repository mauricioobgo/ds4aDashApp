import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

###choose prediction model 
input0 = dbc.FormGroup(
    [
        dbc.Label("Choose prediction model"),
        dbc.RadioItems(
            options=[
                {"label": "Maximize Cultivated Area (Ha)", "value": 1},
                {"label": "Maximize Production (Ton) ", "value": 2},
                {"label": "Maximize Yield (Ton/Ha)", "value": 3},
            ],
            value=1,
            id="radioitems-inline-input",
            inline=True,
        ),
    ],
),

### input the area of land
input1 = dbc.FormGroup(
    [
        html.P("Type the number of hectareas"),
        dbc.Input(type="number", min=0, step=1),
    ],
    id="styled-numeric-input",
),

##dropdown menu to select department of Colombia
input2_1 = dbc.FormGroup(
    [
        dbc.Label("Select the Colombian department where the selected farm is located", html_for="dropdown"),
        dcc.Dropdown(
            id="dropdown",
            options=[
                {"label": "AMAZONAS", "value":"amazonas"},
                {"label": "ANTIOQUIA", "value":"antioquia"},
                {"label": "ARAUCA", "value":"arauca"},
                {"label": "ATLANTICO", "value":"atlantico"},
                {"label": "BOLIVAR", "value":"bolivar"},
                {"label": "BOYACA", "value":"boyaca"},
                {"label": "CALDAS", "value":"caldas"},
                {"label": "CAQUETA", "value":"caqueta"},
                {"label": "CASANARE", "value":"casanare"},
                {"label": "CAUCA", "value":"cauca"},
                {"label": "CESAR", "value":"cesar"},
                {"label": "CHOCO", "value":"choco"},
                {"label": "CORDOBA", "value":"cordoba"},
                {"label": "CUNDINAMARCA", "value":"cundinamarca"},
                {"label": "GUAINIA", "value":"guainia"},
                {"label": "GUAVIARE", "value":"guaviare"},
                {"label": "HUILA", "value":"huila"},
                {"label": "LA GUAJIRA", "value":"la guajira"},
                {"label": "MAGDALENA", "value":"magdalena"},
                {"label": "META", "value":"meta"},
                {"label": "NARINO", "value":"narino"},
                {"label": "NORTE DE SANTANDER", "value":"norte de santander"},
                {"label": "PUTUMAYO", "value":"putumayo"},
                {"label": "QUINDIO", "value":"quindio"},
                {"label": "RISARALDA", "value":"risaralda"},
                {"label": "SAN ANDRES Y PROVIDENCIA", "value":"san andres y providencia"},
                {"label": "SANTANDER", "value":"santander"},
                {"label": "SUCRE", "value":"sucre"},
                {"label": "TOLIMA", "value":"tolima"},
                {"label": "VALLE DEL CAUCA", "value":"valle del cauca"},
                {"label": "VAUPES", "value":"vaupes"},
                {"label": "VICHADA", "value":"vichada"},

            ],
        ),
    ],
    className="mb-3",
)

##dropdown menu to select crop group
input2_2 = dbc.FormGroup(
    [
        dbc.Label("Select the crop Group you want to grow in the selected farm", html_for="dropdown"),
        dcc.Dropdown(
            id="dropdown",
            options=[
                {"label": "CEREALES", "value":"cereales"},
                {"label": "FIBRAS", "value":"fibras"},
                {"label": "FLORES Y FOLLAJES", "value":"flores y follajes"},
                {"label": "FORESTALES", "value":"forestales"},
                {"label": "FRUTALES", "value":"frutales"},
                {"label": "HONGOS", "value":"hongos"},
                {"label": "HORTALIZAS", "value":"hortalizas"},
                {"label": "LEGUMINOSAS", "value":"leguminosas"},
                {"label": "OLEAGINOSAS", "value":"oleaginosas"},
                {"label": "OTROS PERMANENTES", "value":"otros permanentes"},
                {"label": "OTROS TRANSITORIOS", "value":"otros transitorios"},
                {"label": "PLANTAS AROMATICAS", "value":"plantas aromaticas"},
                {"label": "CONDIMENTARIAS Y MEDICINALES", "value":"condimentarias y medicinales"},
                {"label": "TUBERCULOS Y PLATANOS", "value":"tuberculos y platanos"},
            ],
        ),
    ]
)