import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import pandas_datareader.data as web
import datetime



# print(data.head())

app = dash.Dash()

app.layout = html.Div(children=[
    
    html.Div(children='''
        Enter the stock name
    '''),

    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output'),

    

])

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_graph(input_data):
    
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()

    data = web.DataReader(input_data, 'yahoo', start, end)
    
    return dcc.Graph(
        id='graph1',
        figure = {
            'data' : [
                {'x':data.index, 'y':data.Close, 'type':'line', 'name':input_data}
                    ],
            'layout' : {
                'title' : input_data
                        }
                }
            )


if __name__ == '__main__':
    app.run_server(debug=True)