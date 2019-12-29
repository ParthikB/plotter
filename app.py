import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from pandas_datareader.data import DataReader
import time
from collections import deque
import plotly.graph_objs as go
import random


app = dash.Dash('vehicle-data')

data = pd.read_csv('datasets/iris.csv')

data_dict = {}
for col in data.columns:
    data_dict[col] = data[col]


app.layout = html.Div([
    html.Div([
        html.H2('Plotter Analysis',
                style={'float': 'left',
                       }),
        ]),
    dcc.Dropdown(id='data-name',
                 options=[{'label': s, 'value': s} for s in data_dict.keys()],
                 value=['Id', 'SepalLengthCm'],
                 multi=True
                 ),
    html.Div(children=html.Div(id='graphs'), className='row'),
    ], className="container",style={'width':'98%','margin-left':10,'margin-right':10,'max-width':50000})


@app.callback(
    dash.dependencies.Output('graphs','children'),
    [dash.dependencies.Input('data-name', 'value')],
    )
def update_graph(data_names):
    graphs = []
    class_choice = 'col s12'

    # for data_name in data_names:
    # print(data_names)
    if data_names and len(data_names) == 2:
        # print(len(data_names))
        x, y = data_names
        data = go.Scatter(
            x=list(data_dict[x]),
            y=list(data_dict[y]),
            name='Line Plot',
            mode='markers'
            )
        # print(list(data_dict[x]))

        graphs.append(html.Div(dcc.Graph(
            id='data_names',
            animate=False,
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
for js in external_css:
    app.scripts.append_script({'external_url': js})


if __name__ == '__main__':
    app.run_server(debug=True)