import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go


validationSanKey = pd.read_csv('\DataSamples\SankeyTestNew4.csv') # <<< read from csv
validationSanKey1 = validationSanKey[['Source','Target','Value','Label']]
validationSanKey2 = validationSanKey1.sort_values(['Source','Target'])


layout = html.Div([
        #Null Checks
            #dbc.Row(dbc.Col(html.H3('RIS 1 Traffic Data Validation'))),
                dbc.Row([
                    dbc.Col(
                        html.Div([
                            #html.H5('RIS 1 Traffic Data Validation'),
                            #html.Div(id='app-1-display-value'),
                            dcc.Graph(
                                id='sankey',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Sankey(
                                            #valueformat = '.0',
                                            #valuesuffix = 'TWh',
                                            node = dict(
                                              pad = 15,
                                              thickness = 15,
                                              line = dict(color = 'black', width = 0.5),
                                              label =  validationSanKey2['Label'].drop_duplicates().tolist(),
                                              #label =  validationSanKey2['Label'],
                                              #label = ["A1", "A2", "B1", "B2", "C1", "C2"],
                                              color = 'blue'
                                              #color = validationSanKey2['Color']
                                              ),
                                            link = dict(
                                                  #source = validationSanKey2['Source'].drop_duplicates().tolist(),
                                                  #target = validationSanKey2['Target'].drop_duplicates().tolist(),
                                                  source = validationSanKey2['Source'],
                                                  target = validationSanKey2['Target'],
                                                  value = validationSanKey2['Value'],
                                                  label = validationSanKey2['Value']
                                                  #color = validationSanKey2['Color']
                                              )
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        #height=300,
                                        title='Train ticket journey example'
                                        #barmode='stack'
                                        )
                                    }
                                )
                        ]),width=12),
                ],no_gutters=True), #Row end
                            
]) # Div layout end