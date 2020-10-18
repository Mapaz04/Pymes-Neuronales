#pip install dash==1.16.3
#pip install dash-auth==1.3.2

#Librerias
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

dfclientes=pd.read_csv("clientes.csv")
def ExtraerDatos(x):
    datos = []
    for i in dfclientes.index:
        if x == dfclientes.loc[i, "customer_id"]:  # compara i con los v. de la columna customer_id
            datos = dfclientes.loc[i]
    return datos

VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': 'world'
}
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)


app.layout = html.Div([
    html.Link(href="https://fonts.googleapis.com/css2? family = Be + Vietnam & display = swap", rel='stylesheet'),
    html.Link(href="https://fonts.googleapis.com/css2? family = Be + Vietnam & display = swap", rel='stylesheet'),
    html.Header([
        html.Nav([
               html.A([
                 "HackTech - BBVA"
               ],className="navbar-brand",style={'color':'white','margin':'5px 9%','font-family':'Vietnam','font-size':'1.5em'})
        ],className="navbar")
    ],className="site-header",style={'background-color':'#409dc4'}),

    html.Div([
        html.H1("Simula tu credito!"),
        dcc.Markdown('''Aproxima tu credito PYME ahora con _**PymeNeuronal**_.''',style={'margin-bottom':'4rem','font-size':'1.5em'}),

        html.Div(children=[
            html.Div(children=[
                html.Img(src="https://image.freepik.com/vector-gratis/tienda-dibujos-animados-compras_18591-44033.jpg",style={'width':'100%','high':'100%','border-radius': '25px 0px 0px 25px'}),
            ],style={'width':'33%','float':'left'}),

            html.Div(children=[
                html.H4("Introduce tu codigo de cliente",style={'margin':'30px 0px','text-align':'center'}),
                dcc.Input(id="my-input", type="text", placeholder="",style={'border':'grey 1px solid','border-radius':'8px','padding':'7px','height':'30px','width':'80%','margin':'0px 10%'}),
                html.H4("¿El plazo es mayor a 5 meses?", style={'margin': '30px 0px', 'text-align': 'center'}),
                dcc.RadioItems(
                    options=[
                        {'label': 'Sí', 'value': '1'},
                        {'label': 'No', 'value': '2'},
                    ],
                    value='1',
                    style={'margin':'0px 5px','text-align':'center','padding':'5px'}
                ),
                html.Img(src="https://img.icons8.com/plasticine/100/000000/stack-of-money.png", style={'margin':'10px auto','display':'block'})
            ],style={'padding':'0.5rem 1rem','width':'34%','float':'left'}),

            html.Div(children=[
                html.H4(id='my-output1',style={'margin':'30px 0px','text-align':'center'}),
                html.Div(id='my-output2',style={'text-align':'center'})
            ],style={'padding':'0.5rem 1rem','width':'33%','float':'left'}),
            html.Br(style={'clear': 'both'})
        ],style={'background-color':'white','border-radius':'30px','box-shadow': '0px 5px rgba(0,0,0,0.2)','border':'solid rgba(0,0,0,0.2)'})
    ],style={'margin':'1.5rem 10%'})
])


@app.callback(
    [Output(component_id='my-output1', component_property='children'),
     Output(component_id='my-output2', component_property='children')],
    [Input(component_id='my-input', component_property='value')]
)
def update_output_div(input_value):
    if input_value==None:
        return "",""
    elif input_value[-1]=="1":
        return "¡Credito Aprobado!","Para un mediano plazo te recomendamos Credito hipotecario y credito vehicular"
    else:
        return "Credito Desaprobado.","Para un mediano plazo te recomendamos Descuento en Letras y Leasing"


if __name__ == '__main__':
    app.run_server(debug=True)


#x=input("Ingrese su código:")
#codigo= df['customer_id']


