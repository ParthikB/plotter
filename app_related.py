import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import pandas_datareader.data as web
import datetime

app = dash.Dash()

app.layout = html.Div(children=[
    
    # html.Div(children='''
    #     available cols : {}
    # ''')

    html.Div(children='''
        Enter the X, Y axis
    '''),
    dcc.Input(id='input_x', value='', type='text'),
    html.Div(id='output_x'),


    # html.Div(children='''
    #     Enter the Y axis
    # '''),
    # dcc.Input(id='input_y', value='', type='text'),
    # html.Div(id='output_y'),

    

])

@app.callback(
    Output(component_id='output_x', component_property='children'),
    [Input(component_id='input_x', component_property='value')],

    # Output(component_id='output_y', component_property='children'),
    # [Input(component_id='input_y', component_property='value')]
)
def update_graph(input_data):
    x, y, type = input_data.split(',')
    print(input_data.split(','))
    data = pd.read_csv('datasets/BTC_USD.csv')

    return dcc.Graph(
        id='graph1',
        figure = {
            'data' : [
                {'x':data[x], 'y':data[y], 'type':type, 'name':f'{x} v/s {y}'}
                    ],
            'layout' : {
                'title' : f'{x} v/s {y}'
                        }
                }
            )


if __name__ == '__main__':
    app.run_server(debug=True)