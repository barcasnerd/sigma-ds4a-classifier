import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate


card_content_3 = [
    dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
    dbc.CardBody(
        [
            html.H5("Card with image", className="card-title"),
            html.P(
                "This card has an image on top, and a button below",
                className="card-text",
            ),
            dbc.Button("Click me!", color="primary"),
        ]
    ),
]


cards = dbc.CardColumns(
    [
        dbc.Card(card_content_3, color="light"),
        dbc.Card(card_content_3, color="light"),
        dbc.Card(card_content_3, color="light"),
        dbc.Card(card_content_3, color="light"),
        dbc.Card(card_content_3, color="light"),
        dbc.Card(card_content_3, color="light"),
        dbc.Card(card_content_3, color="light"),
    ]
)



component = html.Div([
    html.H1("Contact Us"),
    html.Div([
        html.P("Hello user! this the first SIGMA Ingeniería S.A category prediction model  for customer service. Our model allows, in just a few seconds, to generate the categories of tickets that are entered by the user, in this way it can be directed to the area in charge of a more immediate way and in this way be managed. This process generates a reduction in response time since it allows tickets to be correctly associated to the category, avoiding reprocessing in case they arrive in the wrong area and generating dissatisfaction in customers."),
        html.P("It also reduces the learning curve of the people who enter the support area, who enter the tickets, since the same system will give you which is the category that best matches the text entered, thus avoiding errors in the assignment."),
    ], className="mt-3"),
    cards,
])
