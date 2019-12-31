import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


app = dash.Dash('Quick Plotter')
server = app.server

data = pd.read_csv('datasets/iris.csv')

data_dict = {}
for col in data.columns:
    data_dict[col] = data[col]


app.layout = html.Div([
    html.Div([
        html.H2('Quick Plotter',
                style={'float': 'left',
                       }),
        
    dcc.Dropdown(id='x_axis',
                 options=[{'label': s, 'value': s} for s in data_dict.keys()],
                 placeholder='Select x-axis',
                 multi=False
                 ),
    dcc.Dropdown(id='y_axis',
                 options=[{'label': s, 'value': s} for s in data_dict.keys()],
                 placeholder='Select y-axis',
                 multi=False
                 ),
    # dcc.RadioItems(id='plot_type',
    #             options=[{'label': 'Line',          'value': 'lines'},
    #                     {'label': 'Scatter',       'value': 'markers'},
    #                     {'label': "Bring 'em all", 'value': 'lines+markers'}],
    #             value='lines')
    dcc.Dropdown(id='plot_type',
                 options=[{'label': 'Line',          'value': 'lines'},
                         {'label': 'Scatter',       'value': 'markers'},
                         {'label': "Bring 'em all", 'value': 'lines+markers'}],
                 placeholder='Select Plot type',
                 multi=False)
                 ],
    style={'width':'40%'}),
    html.Div(children=html.Div(id='graphs'), className='row')], 
    className="container",
    style={'width':'98%',
            'margin-left':10,
            'margin-right':10,
            'max-width':50000})


@app.callback(
    Output('graphs','children'),
    [Input('x_axis', 'value'), 
    Input('y_axis', 'value'),
    Input('plot_type', 'value')],
    )
def update_graph(x_axis, y_axis, plot_type):
    graphs = []
    class_choice = 'col s12'
    x, y = x_axis, y_axis

    if x and y:
        data = go.Scatter(
            x       = list(data_dict[x]),
            y       = list(data_dict[y]),
            name    = 'Line Plot',
            mode    = plot_type
            )

        graphs.append(html.Div(dcc.Graph(
            id='data_names',
            animate=False,
            figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(data_dict[x]),max(data_dict[x])]),
                                                        yaxis=dict(range=[min(data_dict[y]),max(data_dict[y])]),
                                                        # margin={'l':50,'r':1,'t':45,'b':1},
                                                        title=f'{x} v/s {y}')}),
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
