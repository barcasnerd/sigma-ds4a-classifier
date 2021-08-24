# import RF_new

# loc = "descripciones_tickets_preprocess.csv"
# model = RF_new.model_classifier(loc)

# RF_new.make_pred(loc,["Hola"],model)


# description = "a"

# def saveDesc(text):
#     global description
#     description = text
#     return text

# print(saveDesc("hey"))
# print(description)

import dash

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

# This stylesheet makes the buttons and table pretty.
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Store(id='memory', storage_type='session'),
    dcc.Input(id='desc', type='text'),
    html.Button('memory', id='memory-button'),
    html.P("desc", id='desc-option')
]
)

# store description
@app.callback(Output('memory', 'data'),
              Input('desc', 'value'),
              State('memory', 'data'))            
def on_click(desc, data):
    if desc is None:
        raise PreventUpdate
    data = data or {'description': ""}
    data['description'] = desc
    return data


# description
# @app.callback(Output('desc-option'.format('session'), 'children'),
#                Input('memory', 'modified_timestamp'),
#                State('memory', 'data'))
# def on_data(ts, data):
#     if ts is None:
#         raise PreventUpdate
#     data = data or {}
#     return data.get('description', "")

# extract data
@app.callback(
    Output('desc-option', 'children'),
    [Input('memory', 'data')],
    [State('desc', 'value')])
def update_output(ts, data):
    return data.get('description')



if __name__ == '__main__':
    app.run_server(debug=True, port=3500, threaded=True)
