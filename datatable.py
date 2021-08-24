import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import RF_new

# manage first training
#loc = "descripciones_tickets_preprocess.csv"
#model = RF_new.model_classifier(loc)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.title = 'SIGMA Classifier'
# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#30454C",
    "color": "#E2EBEB",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# style for logo in sidebar
LOGO_STYLE = {
    "justify-content": "center",
}


# logo component
logo = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.H2("SIGMA", className="display-4"),
                        style={"padding-left": "20px", "padding-right": "7px", }),
                dbc.Col(dbc.Spinner(color="primary", type="grow"), style={
                        "padding-top": "20px", "pading-left": "3px"}),
            ]
        )
    ],
)

# sidebar component
sidebar = html.Div(
    [
        logo,
        html.Hr(style={"border": "0", "border-top": "1px solid #E2EBEB", }),
        html.P(
            "Category classifier and problem solver for SIGMA Ingeniería S.A customer Service", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Entry", href="/", active="exact"),
                dbc.NavLink("Help", href="/help", active="exact")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


# input description field
description_input = dbc.FormGroup(
    [
        dbc.Label("Insert a description",
                  html_for="example-email-row", width=5, ),
        dbc.Col(
            dbc.Textarea(
                id="description-entry",
                placeholder="Description...",
                className="border border-secondary border-top-0 border-right-0 border-left-0 rounded-0",
            ),
            width=7,
        ),
    ],
    row=True,
)

# modal
modal = dbc.Modal(
    [
        dbc.ModalHeader("Classifier"),
        dbc.ModalBody(
            "The model will give you a prediction in a while, it could take a few minutes."),
        dbc.ModalFooter(
            dbc.Button(
                "Close",
                id="close",
                href="/help",
                className="ml-auto",
                n_clicks=0
            )
        ),
    ],
    id="modal",
    is_open=False,
)

# main page
ticket_solver = html.Div(
    [
        
        html.Div([
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H4("Ticket Solver",
                                                className="d-inline")
                                    ],
                                    className="card-title d-flex justify-content-between mb-0",
                                ),
                                html.Div(
                                    [
                                        html.P(
                                            "Group:", className="font-weight-light d-inline"),
                                        html.P(
                                            " Support", className=" d-inline"),
                                    ],
                                    className="mb-4 mt-0"
                                )
                            ],
                        ),
                        description_input
                    ]
                ),
                className="p-3 rounded mb-4",
            ),
            html.Div(
                [
                    dbc.Button("Classify and Solve",
                               id="submit-val",
                               color="primary",
                               className="mr-1 w-50",
                               n_clicks=0,
                               href="/suggestions",
                               style={"border-radius": "20px"}),
                ],
                className="d-flex justify-content-center"
            ),
        ],
            style={"margin": "15%", "margin-top": "15%"},
        ),
    ]
)


suggestions = html.Div(
    [
        # section title
        html.H1("Suggested Solutions", className="mb-4"),

        # suggestions
        html.Div(
            [
                # CARD
                dbc.Card(
                    # cuerpo de la Card
                    dbc.CardBody(
                        [
                            # TITULO DE LA CARD
                            html.Div([
                                html.H5("Model Suggestions"),
                                html.P(
                                    "This is a list of the top 5 best suggestions to solve the problem", className="font-wight-light"),
                            ]),

                            # TABLA DE SUGERENCIAS
                            dbc.Table(
                                [
                                    html.Thead(
                                        html.Tr(
                                            [
                                                html.Th(
                                                    html.P(
                                                        "Solution", className="font-wight-light"),
                                                    className="font-weight-light pb-0",
                                                ),
                                                html.Th(
                                                    html.P(
                                                        "Predicted Category", className="font-wight-light"),
                                                    className="font-weight-light pb-0",
                                                ),
                                                html.Th(
                                                    html.P(
                                                        "Confidence Level", className="font-wight-light"),
                                                    className="font-weight-light pb-0",
                                                ),
                                            ],
                                            className="mb-0",
                                            style={"margin-bottom": "1px",
                                                   "padding": "0px"},
                                        ),
                                    ),

                                    # RESULTADOS DE LA PREDICCIÓN
                                    html.Tbody(
                                        id="suggestion-result", children=[]),
                                ],
                                bordered=False,
                            ),


                        ],
                        className=""
                    ),
                ),
            ],
            className=""
        ),

    ],
    className=""
)

help_window = html.Div(id="help-window", children="help window")

# content accesor
content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

# layout definition to thw whole site
app.layout = html.Div([
    dcc.Location(id="url"),
    dcc.Store(id="memory"),
    sidebar,
    content
])


# store description to session until change
@app.callback(Output('memory', 'data'),
              Input('description-entry', 'value'),
              State('memory', 'data'))            
def saveDescription(desc, data):
    if desc is None:
        raise PreventUpdate
    data = data or {'description': ""}
    data['description'] = desc
    return data


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")],
    [State("memory", "data")]
)
def render_page_content(pathname, data):
    
    if pathname == "/":
        return [ticket_solver]

    elif pathname == "/suggestions":
        print(data)
        return [suggestions, html.P(data.get("description"))]

    elif pathname == "/help":
        return [help_window]

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-dark"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=True, port=3500)
