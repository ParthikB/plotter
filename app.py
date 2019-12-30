import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import time
from collections import deque
import plotly.graph_objs as go
import random
import base64, io, datetime
import dash_table


def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    global df
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    return html.Div([html.H5(filename)])



app = dash.Dash('vehicle-data')

# data = pd.read_csv('datasets/iris.csv')
# data = pd.read_csv('datasets/BTC_USD.csv')


app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    )])   

@app.callback([Input('upload-data', 'contents')])
def update_output(list_of_contents, list_of_names):
    if list_of_contents is not None:
        global children
        children = [
            parse_contents(c, n) for c, n in
            zip(list_of_contents, list_of_names)]
        # print(df)
        return

data = df
data_dict = {}
for col in data.columns:
    data_dict[col] = data[col]

app.layout = html.Div([
    html.Div([
        html.H2('Plotter Analysis',
                style={'float': 'left',
                       }),
        ]),

    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),    

    dcc.Dropdown(id='x_axis',
                 options=[{'label': s, 'value': s} for s in data_dict.keys()],
                #  value=['Id', 'SepalLengthCm'],
                 multi=False,
                 placeholder='Select column for X-axis'
                 ),
    dcc.Dropdown(id='y_axis',
                 options=[{'label': s, 'value': s} for s in data_dict.keys()],
                #  value=['Id', 'SepalLengthCm'],
                 multi=False,
                 placeholder='Select column for Y-axis'
                 ),
    html.Div(id='output-data-upload'),
    html.Div(children=html.Div(id='graphs'), className='row'),
    ], 
    

    className="container",
    style={'width':'98%','margin-left':10,'margin-right':10,'max-width':50000},
    
    )



        


@app.callback(
    dash.dependencies.Output('graphs','children'),
    [dash.dependencies.Input('x_axis', 'value'), dash.dependencies.Input('y_axis', 'value')],
    )
def update_graph(x_axis, y_axis):
    graphs = []
    class_choice = 'col s12'

    if x_axis and y_axis:
        print(x_axis, y_axis)
        x, y = x_axis, y_axis
        data = go.Scatter(
            x=list(data_dict[x]),
            y=list(data_dict[y]),
            name='Line Plot',
            # mode='markers'
            )
        # print(list(data_dict[x]))

        graphs.append(html.Div(dcc.Graph(
            id='data_names',
            # figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(data_dict[x]),max(data_dict[x])]),
            #                                             yaxis=dict(range=[min(data_dict[y]),max(data_dict[y])]),
            #                                             margin={'l':50,'r':1,'t':45,'b':1},
            #                                             title=f'{x} v/s {y}')}
            figure={'data': [data],'layout' : go.Layout(title=f'{x} v/s {y}')}), 
            className=class_choice))

        return graphs









external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
for js in external_js:
    app.scripts.append_script({'external_url': js})


if __name__ == '__main__':
    app.run_server(debug=True)