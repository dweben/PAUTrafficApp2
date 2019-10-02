import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go

validationHeat_M25_Enh = pd.read_csv('\DataSamples\M25HeatMap_Enh.csv') # <<< read from csv
validationHeat_M25_Enh_1 = validationHeat_M25_Enh[['RoadNumber','YearID','DateID','TimePeriodID','Delay','RecurrentDelay','NonRecurrentDelay']]
validationHeat_M25_Enh_2 = validationHeat_M25_Enh_1.sort_values(['DateID','TimePeriodID'])

validationHeat_M42 = pd.read_csv('\DataSamples\M42HeatMapDate.csv') # <<< read from csv
validationHeat_M42_1 = validationHeat_M42[['RoadNumber','YearID','DateID','TimePeriodID','Delay']]
validationHeat_M42_2 = validationHeat_M42_1.sort_values(['DateID','TimePeriodID'])

validationHeat_M25 = pd.read_csv('\DataSamples\M25HeatMapDate.csv') # <<< read from csv
validationHeat_M25_1 = validationHeat_M25[['RoadNumber','YearID','DateID','TimePeriodID','Delay']]
validationHeat_M25_2 = validationHeat_M25_1.sort_values(['DateID','TimePeriodID'])

validationHeat_M5 = pd.read_csv('\DataSamples\M5HeatMapDate.csv') # <<< read from csv
validationHeat_M5_1 = validationHeat_M5[['RoadNumber','YearID','DateID','TimePeriodID','Delay']]
validationHeat_M5_2 = validationHeat_M5_1.sort_values(['DateID','TimePeriodID'])

validationHeat_M6 = pd.read_csv('\DataSamples\M6HeatMapDate.csv') # <<< read from csv
validationHeat_M6_1 = validationHeat_M6[['RoadNumber','YearID','DateID','TimePeriodID','Delay']]
validationHeat_M6_2 = validationHeat_M6_1.sort_values(['DateID','TimePeriodID'])

layout = html.Div([
        #Null Checks
            #dbc.Row(dbc.Col(html.H3('RIS 1 Traffic Data Validation'))),
            
             dbc.Row([
                     dbc.Col(
                        html.Div([
                            #html.H5('RIS 1 Traffic Data Validation'),
                            #html.Div(id='app-1-display-value'),
                            dcc.Graph(
                                id='heatmap_m25_large',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=validationHeat_M25_2['DateID'],
                                            y=validationHeat_M25_2['TimePeriodID'],
                                            z=validationHeat_M25_2['Delay'],
                                            name='Delay',
                                            colorscale='Viridis',
                                            zmin=0,
                                            zmax=50
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        #height=300,
                                        title='M25 Average Delay'
                                        #barmode='stack'
                                        )
                                    }
                                )
                        ]),width=12),
                 # Zero Checks    
                 ],no_gutters=True), #Row end
                dbc.Row([
                     dbc.Col(
                        html.Div([
                            #html.H5('RIS 1 Traffic Data Validation'),
                            #html.Div(id='app-1-display-value'),
                            dcc.Graph(
                                id='heatmap_m25_nonrec',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=validationHeat_M25_Enh_2['DateID'],
                                            y=validationHeat_M25_Enh_2['TimePeriodID'],
                                            z=validationHeat_M25_Enh_2['NonRecurrentDelay'],
                                            name='Delay',
                                            colorscale='Viridis',
                                            zmin=0,
                                            zmax=50
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        #height=300,
                                        title='M25 Average NonRecurrent Delay'
                                        #barmode='stack'
                                        )
                                    }
                                )
                        ]),width=6),
                     dbc.Col(
                        html.Div([
                            #html.H5('RIS 1 Traffic Data Validation'),
                            #html.Div(id='app-1-display-value'),
                            dcc.Graph(
                                id='heatmap_m25_rec',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=validationHeat_M25_Enh_2['DateID'],
                                            y=validationHeat_M25_Enh_2['TimePeriodID'],
                                            z=validationHeat_M25_Enh_2['RecurrentDelay'],
                                            name='Delay',
                                            colorscale='Viridis',
                                            zmin=0,
                                            zmax=50
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        #height=300,
                                        title='M25 Average Recurrent Delay'
                                        #barmode='stack'
                                        )
                                    }
                                )
                        ]),width=6),
                ],no_gutters=True), #Row end
             dbc.Row([
                     dbc.Col(
                        html.Div([
                            #html.H5('RIS 1 Traffic Data Validation'),
                            #html.Div(id='app-1-display-value'),
                            dcc.Graph(
                                id='heatmap42',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=validationHeat_M42_2['DateID'],
                                            y=validationHeat_M42_2['TimePeriodID'],
                                            z=validationHeat_M42_2['Delay'],
                                            name='Delay',
                                            colorscale='Viridis',
                                            zmin=0,
                                            zmax=50
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        #height=300,
                                        title='M42 Average Delay'
                                        #barmode='stack'
                                        )
                                    }
                                )
                        ]),width=6),
                 # Zero Checks        
                     dbc.Col(
                        html.Div([
                            #html.H5('RIS 1 Traffic Data Validation'),
                            #html.Div(id='app-1-display-value'),
                            dcc.Graph(
                                id='heatmapm25',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=validationHeat_M25_2['DateID'],
                                            y=validationHeat_M25_2['TimePeriodID'],
                                            z=validationHeat_M25_2['Delay'],
                                            name='Delay',
                                            colorscale='Viridis',
                                            zmin=0,
                                            zmax=50
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        #height=300,
                                        title='M25 Average Delay'
                                        #barmode='stack'
                                        )
                                    }
                                )
                        ]),width=6),
                ],no_gutters=True), #Row end
                                
dbc.Row([
                     dbc.Col(
                        html.Div([
                            #html.H5('RIS 1 Traffic Data Validation'),
                            #html.Div(id='app-1-display-value'),
                            dcc.Graph(
                                id='heatmapm5',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=validationHeat_M5_2['DateID'],
                                            y=validationHeat_M5_2['TimePeriodID'],
                                            z=validationHeat_M5_2['Delay'],
                                            name='Delay',
                                            colorscale='Viridis',
                                            zmin=0,
                                            zmax=50
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        #height=300,
                                        title='M5 Average Delay'
                                        #barmode='stack'
                                        )
                                    }
                                )
                        ]),width=6),
                 # Zero Checks        
                     dbc.Col(
                        html.Div([
                            #html.H5('RIS 1 Traffic Data Validation'),
                            #html.Div(id='app-1-display-value'),
                            dcc.Graph(
                                id='heatmapm6',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=validationHeat_M6_2['DateID'],
                                            y=validationHeat_M6_2['TimePeriodID'],
                                            z=validationHeat_M6_2['Delay'],
                                            name='Delay',
                                            colorscale='Viridis',
                                            zmin=0,
                                            zmax=50
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        #height=300,
                                        title='M6 Average Delay'
                                        #barmode='stack'
                                        )
                                    }
                                )
                        ]),width=6),
                ],no_gutters=True), #Row end
                      
]) # Div layout end