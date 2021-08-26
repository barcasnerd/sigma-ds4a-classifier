import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.CardHeader import CardHeader
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

mkd_string="""
|                     |                                                           |
|---------------------|-----------------------------------------------------------|
|   App               | No envia el backup de aplicación movil                    |
|                     | No cargan los datos correctamente en la aplicación        |
|                     | No inicia sesion en aplicación movil                      |
|                     | Subir aplicación móvil app a play store                   |
| Consultas           | Revisión de Consultas                                     |
| Datos               | Cambiar datos por BD                                      |
|                     | Carga de datos masiva                                     |
|                     | Datos erroneos en BI                                      |
|                     | Datos erroneos en Cubo                                    |
| Formulario          | No carga un formulario                                    |
|                     | Calculo erroneo en formulario                             |
|                     | Formulario no guarda, no edita y o no elimina             |
|                     | Configuración de nuevo campo                              |
|                     | No busca ni filtra en formulario                          |
| Funcionalidad       | Adición o modificación de funcionalidad en perfil         |
|                     | Capacitacion de modulo o funcionalidad                    |
|                     | Implantación módulo o nueva funcionalidad                 |
| GPS                 | Configuración de equipos GPS                              |
|                     | No transmite GPS                                          |
|                     | Revisión de GPS                                           |
|                     | Saltos de GPS Descalibrado                                |
| Nuevo requerimiento | 1- Nuevo requerimiento                                    |
| Otros               | 0- No definido                                            |
| Reporte             | Faltan datos en un reporte                                |
|                     | Configuración de nuevo Reporte                            |
|                     | Error al exportar reporte                                 |
|                     | Datos erroneos en reporte                                 |
|                     | No descarga reporte                                       |
|                     | Generar reporte, informe, datos solicitado por el cliente |
| Servicios           | Publicación de servicios, capas                           |
|                     | Interrupcion completa del servicio                        |
| Shape               | Generación de shape                                       |
| Sistema             | No inicia sesion un usuario en movilidad                  |
|                     | No carga el sistema                                       |
|                     | Imposibilidad ingreso de un usuario                       |
|                     | Disminucion del desempeño de plataforma                   |
|                     | Duda en uso de plataforma                                 |
|                     | Creación de usuarios para ingreso plataforma              |
|                     | Sale error en movilidad al adicionar                      |
|                     | Duda en uso de campos                                     |
|                     | Auditoria del sistema                                     |
| Visor               | Datos erroneos en Visor                                   |
|                     | Configuracion de nueva capa en visor                      |
|                     | No funciona adecuadamente widget del visor                |
|                     | No carga el visor                                         |
|                     | Configuracion de nuevo widget en visor                    |
|                     | No cargan las capas en el visor                           |
|                     | Lentitud en el visor                                      |

"""


category_table = html.Div([
    dbc.Row([
        dbc.Card([
            dbc.CardHeader([
                dbc.Row([
                    dbc.Col(html.H5("Model Category")),
                    dbc.Col(html.H5("Sigma Category")),
                ]),
            ]),
            dbc.CardBody([
                dcc.Markdown(mkd_string)
            ]),
        ]),
    ], justify="center")
])

component = html.Div([
    html.H1("Help, Support and Information"),

    html.Div([
        html.P("Hello user! this the first SIGMA Ingeniería S.A category prediction model  for customer service. Our model allows, in just a few seconds, to generate the categories of tickets that are entered by the user, in this way it can be directed to the area in charge of a more immediate way and in this way be managed. This process generates a reduction in response time since it allows tickets to be correctly associated to the category, avoiding reprocessing in case they arrive in the wrong area and generating dissatisfaction in customers."),
        html.P("It also reduces the learning curve of the people who enter the support area, who enter the tickets, since the same system will give you which is the category that best matches the text entered, thus avoiding errors in the assignment."),
    ], className="mt-3"),




    html.Div([
        html.H4("Model Usage", className="", style={"padding-top": "1.5%"}),

        dbc.Row([
            html.Div([
                html.P("Enter the text corresponding to the ticket on the initial screen. This text should be reviewed in terms to get better results within the model prediction, follow the next hint for mode information"),
            ], className="rounded bg-light p-3", style={"max-width": "95%", "padding": "3%"}),
        ], justify="center", className="mt-3 p-3", style={"padding": "2%"}),

        html.Div([
            # image 0ne
            html.Div([
                dbc.Row([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Row([
                                    html.Img(
                                        src="https://raw.githubusercontent.com/barcasnerd/sigma-ds4a-classifier/jair-changes/images/insert_text.jpg", style={"width": "100%", "max-width": "100%"}),
                                    ], justify="center"),
                        ]),
                    ], className="w-75"),
                ], justify="center"),
            ], className="mt-3"),

            dbc.Row([
                html.Div([
                    html.H6("Hint"),
                    html.P("Preferably enter technical words associated with the system, try not to use greeting words such as 'Buenos días' 'Cordial saludo' and similar phrases."),
                ], className="rounded bg-light p-3", style={"max-width": "95%", "padding": "3%"}),
            ], justify="center", className="mt-3 p-3", style={"padding": "2%"}),

            dbc.Row([
                html.Div([
                    html.P("After entering the text, an informative message will appear where the response of the model must be awaited. Click on close and wait for the system's response"),
                ], className="rounded bg-light p-3", style={"max-width": "95%", "padding": "3%"}),
            ], justify="center", className="mt-1 p-3", style={"padding": "2%"}),

            # image 2two
            html.Div([
                dbc.Row([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Row([
                                    html.Img(
                                        src="https://raw.githubusercontent.com/barcasnerd/sigma-ds4a-classifier/jair-changes/images/warning.jpg", style={}),
                                    ], justify="center"),
                        ]),
                    ], className="w-75", style={"margin-top": "1.5%"}),
                ], justify="center"),
            ], className="mt-3"),

            dbc.Row([
                html.Div([
                    html.P("The result of the prediction will correspond to the first 3 categories most coincident with the text entered, in order of accuracy"),
                ], className="rounded bg-light p-3", style={"max-width": "95%", "padding": "3%"}),
            ], justify="center", className="mt-3 p-3", style={"padding": "2%"}),            

            # image 3three
            html.Div([
                dbc.Row([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Row([
                                    html.Img(
                                        src="https://raw.githubusercontent.com/barcasnerd/sigma-ds4a-classifier/jair-changes/images/suggest.jpg", style={"width": "100%", "max-width": "100%"}),
                                    ], justify="center"),
                        ]),
                    ], className="w-75", style={"margin-top": "1.5%"}),
                ], justify="center"),
            ]),

            dbc.Row([
                html.Div([
                    html.P("The model was based on more generic categories to allow better precision. The following table details which are the business categories according to the prediction of the model"),
                ], className="rounded bg-light p-3", style={"max-width": "95%", "padding": "3%"}),
            ], justify="center", className="mt-3 p-3", style={"padding": "2%"}),            

        ],),
    ]),

    html.Div([
         html.H4("Category Modeling Table", className="", style={"padding-top": "1.5%", "padding-bottom":"2%"}),
        category_table,
    ]),

])
