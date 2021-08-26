import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate


component = html.Div([
    html.H1("Help, Support and Information"),
    
    html.Div([
        html.P("Hello user! this the first SIGMA Ingeniería S.A category prediction model  for customer service. Our model allows, in just a few seconds, to generate the categories of tickets that are entered by the user, in this way it can be directed to the area in charge of a more immediate way and in this way be managed. This process generates a reduction in response time since it allows tickets to be correctly associated to the category, avoiding reprocessing in case they arrive in the wrong area and generating dissatisfaction in customers."),
        html.P("It also reduces the learning curve of the people who enter the support area, who enter the tickets, since the same system will give you which is the category that best matches the text entered, thus avoiding errors in the assignment."),
    ], className="mt-5"),

    html.Div([
        html.H5("Usage"),
        html.Div([
            html.P("Enter the text corresponding to the ticket on the initial screen."),
            html.Img(src="https://avatars.githubusercontent.com/u/1280389?s=88&u=af411373e896f4861e1a2579c2f8109513bab60f&v=4")
        ]),
    ]),

])
