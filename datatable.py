import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

# manage first training
trained = False

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
    "color" : "#E2EBEB",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

#style for logo in sidebar
LOGO_STYLE = {
    "justify-content": "center",
}



#logo component
logo = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.H2("SIGMA", className="display-4"), style={"padding-left":"20px","padding-right":"7px",}),                        
                dbc.Col(dbc.Spinner(color="primary", type="grow"), style={"padding-top":"20px","pading-left":"3px"}),
            ]
        )
    ],
)

#sidebar component
sidebar = html.Div(
    [
        logo,
        html.Hr(style={"border":"0","border-top":"1px solid #E2EBEB",}),
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

#content accesor
content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

#layout definition to thw whole site
app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])

#input description field
description_input = dbc.FormGroup(
    [
        dbc.Label("Insert a description", html_for="example-email-row", width=5, ),
        dbc.Col(
            dbc.Textarea(
                ##type="text", 
                id="description-entry", 
                placeholder="Description...",
                className="border border-secondary border-top-0 border-right-0 border-left-0 rounded-0",
            ),
            width=7,
        ),
    ],
    row=True,
)

#input ticket number field
ticket_input = dbc.FormGroup(
    [
        dbc.Label("Ticket number", html_for="example-password-row", width=5,),
        dbc.Col(
            dbc.Textarea(
                ##type="text",
                id="ticker-entry",
                placeholder="Ticket...",
                className="border border-secondary border-top-0 border-right-0 border-left-0 rounded-0",
            ),
            width=7,
        ),
    ],
    row=True,
)


#main page
ticket_solver=html.Div(
    [
        html.Div([
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H4("Ticket Solver", className="d-inline")
                                    ],
                                    className="card-title d-flex justify-content-between mb-0",
                                ),
                                html.Div(
                                    [
                                        html.P("Group:", className="font-weight-light d-inline"),
                                        html.P(" Support", className=" d-inline"),
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
                     dbc.Button("Classify and Solve", href="/suggestions", color="primary", className="mr-1 w-50", style={"border-radius":"20px"}),
                 ],
                 className="d-flex justify-content-center"
             ),
            ],
            style={"margin":"15%", "margin-top":"15%"},
        ),
    ]
)

overview = html.Div(
    [
        #title
        html.H1("Model Overview", className="mt-2"),

        #cards
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.P("Solved"),
                                        html.H2("60"),
                                    ],
                                ),
                            ),
                        ),
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.P("Unsolved"),
                                        html.H2("16"),
                                    ],
                                ),
                            ),
                        ),
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.P("Categories"),
                                        html.H2("43"),
                                    ],
                                ),
                            ),
                        ),
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.P("New Suggestions"),
                                        html.H2("64"),
                                    ],
                                ),
                            ),
                        ),
                    ]
                )
            ],
            className="mt-5"
        ),

        #plots
        html.Div(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div(
                            [
                                html.H4("Model Confidence Behavior"),
                                html.P("This plot is using example data for frontend mockup only.")
                            ],
                            className="card-title"
                        ),
                        html.Div(
                            dcc.Graph(id='bargraph',
                                figure=px.bar(df, barmode='group', x='Years',
                                y=['Girls High School', 'Boys High School']))
                        ),
                    ]
                )
            ),
            className="mt-5"
        ),

        #more details
        html.Div(
            dbc.Row(
                [
                    #most used categories
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    #TITLE most used categories
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.H4("Most Frequent Categories", className="d-inline"),
                                                    html.P("Frequency", className="d-inline text-primary"),
                                                ],
                                                className="d-flex justify-content-between mb-0"
                                            ),
                                            html.P("Category", className="d-inline font-weight-light"),
                                            html.P(" Name", className="d-inline"),
                                        ],
                                        className="card-title",
                                    ),

                                    #CONTENT most used categories
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.P("Awaiting developer fix", className="d-inline"),
                                                    html.P("4221", className="d-inline font-weight-light"),
                                                ],
                                                className="d-flex justify-content-between "
                                            ),
                                            html.Hr(style={"margin":"0px","padding":"1px"}),
                                            html.Div(
                                                [
                                                    html.P("Waiting on Feature Request", className="d-inline"),
                                                    html.P("3200", className="d-inline font-weight-light"),
                                                ],
                                                className="d-flex justify-content-between "
                                            ),
                                            html.Hr(style={"margin":"0px","padding":"1px"}),
                                            html.Div(
                                                [
                                                    html.P("Awaiting Customer Response", className="d-inline"),
                                                    html.P("1332", className="d-inline font-weight-light"),
                                                ],
                                                className="d-flex justify-content-between "
                                            ),
                                            html.Hr(style={"margin":"0px","padding":"1px"}),
                                            html.Div(
                                                [
                                                    html.P("Pending", className="d-inline"),
                                                    html.P("421", className="d-inline font-weight-light"),
                                                ],
                                                className="d-flex justify-content-between "
                                            ),
                                        ],
                                        className="mt-3",
                                    ),

                                ]
                            ),
                        ),
                    ),

                    #add more categories
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    #TITLE add more categories
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.H4("Card title", className="d-inline"),
                                                    html.P("Help", className="d-inline text-primary"),
                                                ],
                                                className="d-flex justify-content-between mb-0"
                                            ),
                                            html.P("Access:", className="d-inline font-weight-light"),
                                            html.P(" Solo personal autorizado", className="d-inline"),
                                        ],
                                        className="card-title",
                                    ),

                                    # CONTENT add more categories
                                    html.Div(
                                        dbc.Button("Click here to Login", color="primary", className="mr-1 w-50", style={"border-radius":"20px"}),
                                        className="d-flex justify-content-center"
                                    ),
                                ]
                            ),
                        ),
                    ),
                ]
            ),
            className="mt-5"
        ),
    ]
)


suggestions=html.Div(
    [
        #section title
        html.H1("Suggested Solutions", className="mb-4"),

        #suggestions
        html.Div(
            [
                #CARD
                dbc.Card(
                    #cuerpo de la Card
                    dbc.CardBody(
                        [
                            #TITULO DE LA CARD
                            html.Div([
                                html.H5("Model Suggestions"),
                                html.P("This is a list of the top 5 best suggestions to solve the problem", className="font-wight-light"),
                            ]),

                            #TABLA DE SUGERENCIAS
                            dbc.Table(
                                [
                                    html.Thead(
                                        html.Tr(
                                            [
                                                html.Th(
                                                    html.P("Solution",className="font-wight-light"),
                                                    className="font-weight-light pb-0",
                                                ),
                                                html.Th(
                                                    html.P("Predicted Category",className="font-wight-light"),
                                                    className="font-weight-light pb-0",
                                                ),
                                                html.Th(
                                                    html.P("Confidence Level",className="font-wight-light"),
                                                    className="font-weight-light pb-0",
                                                ),                                                
                                            ],
                                            className="mb-0",
                                            style={"margin-bottom":"1px", "padding":"0px"},
                                        ),
                                    ),
                                    html.Tbody(
                                        [
                                            html.Tr(
                                                [
                                                    html.Td("Contact Email not linked. Restart the server"),
                                                    html.Td("11"),
                                                    html.Td(
                                                        [
                                                            html.Div(
                                                                html.P("High"),
                                                                className="text-light rounded bg-success w-50 justify-content-center"
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            html.Tr(
                                                [
                                                    html.Td("Shutdown the GPS and try again"),
                                                    html.Td("21"),
                                                    html.Td(
                                                        [
                                                            html.Div(
                                                                html.P("High"),
                                                                className="text-light rounded bg-success w-50 justify-content-center"
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            html.Tr(
                                                [
                                                    html.Td("Contact with Geolumina service"),
                                                    html.Td("22"),
                                                    html.Td(
                                                        [
                                                            html.Div(
                                                                html.P("Normal"),
                                                                className="text-light rounded bg-warning w-50 justify-content-center"
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            html.Tr(
                                                [
                                                    html.Td("Abrir la nueva carpeta que está en el correo"),
                                                    html.Td("4"),
                                                    html.Td(
                                                        [
                                                            html.Div(
                                                                html.P("Normal"),
                                                                className="text-light rounded bg-warning w-50 justify-content-center"
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            html.Tr(
                                                [
                                                    html.Td("Restart the server"),
                                                    html.Td("8"),
                                                    html.Td(
                                                        [
                                                            html.Div(
                                                                html.P("Low"),
                                                                className="text-light rounded bg-danger w-50 justify-content-center"
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        className=""
                                    ),
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

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        dcc.Location
        return [ticket_solver]

    elif pathname == "/suggestions":
        return [suggestions]


    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-dark"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__=='__main__':
    app.run_server(debug=True, port=3500)

