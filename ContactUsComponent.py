import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate


card_content_1 = [
    dbc.CardImg(src="""https://s3.amazonaws.com/uploads.use1.cloud.rocket.chat/L9bLyLzJWyZRmfo8p/avatars/FNh8pS5RpitWm8pjk?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAILPK6SHTK5RJZLHQ%2F20210826%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210826T091520Z&X-Amz-Expires=120&X-Amz-Signature=cc6e8ccc616d8d538f8ada3dacf6a179b20bf846a6e1627a64379024c2d94f92&X-Amz-SignedHeaders=host&response-content-disposition=inline%3B%20filename%3D%22catalinaej22-gmail.com%22""", top=True, className="rounded-circle"),
    dbc.CardBody(
        [
            html.H5("Catalina Escobar", className="card-title"),
            html.P(
                "Computer Scientist and Database expert at Leonisa",
                className="card-text",
            ),
            dbc.Button("More Info", color="primary", className="fixed-bottom"),
        ]
    ),
]


card_content_2 = [
    dbc.CardImg(src="https://s3.amazonaws.com/uploads.use1.cloud.rocket.chat/L9bLyLzJWyZRmfo8p/avatars/ZcMCjuJSKBimiCjPK?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAILPK6SHTK5RJZLHQ%2F20210826%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210826T100037Z&X-Amz-Expires=120&X-Amz-Signature=184b7363d36a2bb1055e694071dadce820f325696ea4303d88d724227a7c6a27&X-Amz-SignedHeaders=host&response-content-disposition=inline%3B%20filename%3D%22juliansantiago99-gmail.com%22", top=True, className="rounded-circle"),
    dbc.CardBody(
        [
            html.H5("Julián Martínez", className="card-title"),
            html.P(
                "Statistics Student at Pontificia Universidad Javeriana",
                className="card-text",
            ),
            dbc.Button("More Info", color="primary", className="fixed-bottom"),
        ]
    ),
]

card_content_3 = [
    dbc.CardImg(src="https://static.wixstatic.com/media/82a5ff_a6dcca694acb488481cbbe766f25df00~mv2.jpg/v1/fill/w_260,h_260,al_c,q_80,usm_0.66_1.00_0.01/David%20Puentes%202_cuadrado.webp", top=True, className="rounded-circle"),
    dbc.CardBody(
        [
            html.H5("David Puentes", className="card-title"),
            html.P(
                "Msc on Industrial Engineering at Universidad Industrial de Santander.",
                className="card-text",
            ),
            dbc.Button("More Info", color="primary", href="https://www.linkedin.com/in/david-esteban-puentes-garzon-042568aa/"),
        ]
    ),
]

card_content_4 = [
    dbc.CardImg(src="https://yt3.ggpht.com/ytc/AKedOLRKG8rPQxRrz0d6zR4zQ3IpsG_PUbzz50pRI_aQxg=s900-c-k-c0x00ffffff-no-rj", top=True, className="rounded-circle"),
    dbc.CardBody(
        [
            html.H5("Jair Barcasnegras", className="card-title"),
            html.P(
                "Computer Science Student at Universidad del, TI assistant and freelancer developer",
                className="card-text",
            ),
            dbc.Button("More Info", color="primary", href="https://www.linkedin.com/in/jair-barcasnegras-estrada-20085517b"),
        ]
    ),
]

card_content_5 = [
    dbc.CardImg(src="https://media-exp1.licdn.com/dms/image/C4D03AQEssNee_43rsQ/profile-displayphoto-shrink_800_800/0/1581450649082?e=1635379200&v=beta&t=sAWf2rxaOo0APOKLqLhVgoDKToW1vfTrRYw4AVp92cg", top=True, className="rounded-circle"),
    dbc.CardBody(
        [
            html.H5("Raúl Arguello", className="card-title"),
            html.P(
                "Mechanical Engineer Specialist in Production and Operations Management Magister in Industrial Engineering.",
                className="card-text",
            ),
            dbc.Button("More Info", color="primary", href="https://www.linkedin.com/in/raul-arguello/"),
        ]
    ),
]

card_content_6 = [
    dbc.CardImg(src="https://media-exp1.licdn.com/dms/image/C4E03AQELVhcMwOkV0g/profile-displayphoto-shrink_200_200/0/1615221825203?e=1635379200&v=beta&t=ZW9_MhfWF7Q_QtJvSIaqr3IawwDhn0LdQ4FD2gNKXno", top=True, className="rounded-circle"),
    dbc.CardBody(
        [
            html.H5("Melissa Montes", className="card-title"),
            html.P(
                "Data Scientist and AI consultant at Google. Teacher assistant for Correlation One",
                className="card-text",
            ),
            
        ]
    ),
]

card_content_7 = [
    dbc.CardImg(src="https://media-exp1.licdn.com/dms/image/C5603AQFy33q3jW-Vcg/profile-displayphoto-shrink_200_200/0/1619799197169?e=1635379200&v=beta&t=S3sP3uup7k8-xXn3b0N4-SOGl6LmR6BHS7XKs4RyJN4", top=True, className="rounded-circle"),
    dbc.CardBody(
        [
            html.H5("Andrea Vásquez", className="card-title"),
            html.P(
                "Business administrator with a focus on project management and Data Analyst at Experimentality and EAFIT university",
                className="card-text",
            ),
            dbc.Button("More Info", color="primary", href="https://www.linkedin.com/in/gvasque6"),
        ]
    ),
]

card_content_8 = [
    dbc.CardImg(src="https://media-exp1.licdn.com/dms/image/C4E03AQHBOUkFROuCJw/profile-displayphoto-shrink_200_200/0/1579516875894?e=1635379200&v=beta&t=kfdyxeRlyqsPjTJ9s8CV5HKRHC0GgS9JqzDNVRIszs8", top=True, className="rounded-circle"),
    dbc.CardBody(
        [
            html.H5("Wilmer Garzón", className="card-title"),
            html.P(
                "Doctoral Researcher at IMT Atlantique. Assistant Professor at Colombiam School of Engineering",
                className="card-text",
            ),
            dbc.Button("More Info", color="primary", href="https://www.linkedin.com/in/wegalfonso"),
        ]
    ),
]

card_content_9 = [
    dbc.CardImg(src="""https://s3.amazonaws.com/uploads.use1.cloud.rocket.chat/L9bLyLzJWyZRmfo8p/avatars/8sSuLtXmDLHHyrX7r?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAILPK6SHTK5RJZLHQ%2F20210826%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210826T091208Z&X-Amz-Expires=120&X-Amz-Signature=5bc627a206d56bcb8e6d3e26e6bf2ce1bb093c6ee0a6047914d90041a51abc3b&X-Amz-SignedHeaders=host&response-content-disposition=inline%3B%20filename%3D%22a.rosas-correlation-one.com%22""", top=True, className="rounded-circle"),
    dbc.CardBody(
        [
            html.H5("Andrés Caballero", className="card-title"),
            html.P(
                "Data Science experto and Teacher Assistant for Correletion One Data Science For All Colombian program",
                className="card-text",
            ),
            
        ]
    ),
]


cards2 = dbc.CardColumns(
    [
        dbc.Card(card_content_1, style={"max-width":"95%"}, color="light"),
        dbc.Card(card_content_2, style={"max-width":"95%"}, color="light"),
        dbc.Card(card_content_3, style={"max-width":"95%"}, color="light"),
        dbc.Card(card_content_4, style={"max-width":"95%"}, color="light"),
        dbc.Card(card_content_5, style={"max-width":"95%"}, color="light"),
        dbc.Card(card_content_6, style={"max-width":"95%"}, color="light"),
        dbc.Card(card_content_7, style={"max-width":"95%"}, color="light"),
        dbc.Card(card_content_8, style={"max-width":"95%"}, color="light"),
        dbc.Card(card_content_9, style={"max-width":"95%"}, color="light"),
    ], className="mt-4"
)

frontend = html.Div([
    dbc.Row([
        dbc.Col([dbc.Card(card_content_1, style={"max-width":"70%"}, color="light"),], className="d-flex justify-content-center"),
        dbc.Col([dbc.Card(card_content_4, style={"max-width":"70%"}, color="light"),], className="d-flex justify-content-center"),
        dbc.Col([dbc.Card(card_content_7, style={"max-width":"70%"}, color="light"),], className="d-flex justify-content-center"),
    ], justify="center", )
], style={"margin-top":"3%"})

backend = html.Div([
    dbc.Row([
        dbc.Col([dbc.Card(card_content_2, style={"max-width":"95%"}, color="light"),], className="d-flex justify-content-center"),
        dbc.Col([dbc.Card(card_content_3, style={"max-width":"95%"}, color="light"),], className="d-flex justify-content-center"),
        dbc.Col([dbc.Card(card_content_5, style={"max-width":"95%"}, color="light"),], className="d-flex justify-content-center"),
        dbc.Col([dbc.Card(card_content_8, style={"max-width":"95%"}, color="light"),], className="d-flex justify-content-center"),
    ], justify="center", )
], style={"margin-top":"3%"})

tas = html.Div([
    dbc.Row([
        dbc.Col([dbc.Card(card_content_6, style={"max-width":"50%"}, color="light"),], className="d-flex justify-content-center"),
        dbc.Col([dbc.Card(card_content_9, style={"max-width":"50%"}, color="light"),], className="d-flex justify-content-center"),
    ], justify="center", )
], style={"margin-top":"3%"})


cards = html.Div([
    html.H4("Front-End Team", style={"margin-top":"3%"}),
    html.P("The Front-End team is responsible for managing all views of the data and general information that can be seen from the browser side. In addition, the team is responsible for the deployment of the database on the cloud servers together with the deployment of the entire project so that it can be accessed from anywhere in the world. Moreover, you are also responsible for documenting the UX and UI functionality in detail."),
    frontend,
    html.H4("Back-End Team", style={"margin-top":"3%"}),
    html.P("The backend team is responsible for data cleansing, information analysis, modeling, and overall project functionality for category predictions. In addition, the team is responsible for testing the entire product in general for its correct operation."),    
    backend,
    html.H4("Teachers Assistant (TAs)", style={"margin-top":"3%"}),
    html.P("The TAs have generally been in charge of project supervision, as well as providing all the support and the necessary bases to be able to correctly implement both the Front-End, Back-End and documentation in general."),    
    tas
])

component = html.Div([
    html.H1("Contact Us"),
    html.Div([
        html.P("This is the group which made the project possible by creating the first SIGMA Ingeniería S.A category prediction model for customer service. Our model allows, in just a few seconds, to generate the categories of tickets that are entered by the user, in this way it can be directed to the area in charge of a more immediate way and in this way be managed. This process generates a reduction in response time since it allows tickets to be correctly associated to the category, avoiding reprocessing in case they arrive in the wrong area and generating dissatisfaction in customers. You can find more information about the team in the following section."),
    ], className="mt-3"),
    cards,
])
