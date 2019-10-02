import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go

fsovalidation = pd.read_csv('\DataSamples\DataValidation_FSO_20190717.csv') # <<< read from csv
fsovalidation1 = fsovalidation[['Date','NTISModelVersion','ProfileFlowNullCheck','ProfileFlowZeroCheck','TotalFlowNullCheck','TotalFlowZeroCheck','TotalFlow_Max','ProfileFlow_Max','RecordCountCheck']]
fsovalidation2 = fsovalidation1.sort_values(['Date'])

layout = html.Div([
        #Null Checks
            #dbc.Row(dbc.Col(html.H3('RIS 1 Traffic Data Validation'))),
            dbc.Row([
                    dbc.Col(
                    html.Div([
                        #html.H5('RIS 1 Traffic Data Validation'),
                        #html.Div(id='app-1-display-value'),
                        dcc.Graph(
                            id='speed-graph',
                            #style={'width': 900,'height': 600},
                            figure={
                                'data': [
                                    go.Scattergl(
                                        x=fsovalidation2['Date'],
                                        y=fsovalidation2['ProfileFlowNullCheck'],
                                        name='ProfileFlowNullCheck',
                                        yaxis='y',
                                        mode='lines'
                                        ),
                                    go.Scattergl(
                                        x=fsovalidation2['Date'],
                                        y=fsovalidation2['TotalFlowNullCheck'],
                                        name='TotalFlowNullCheck',
                                        yaxis='y',
                                        mode='lines'
                                        ),
                                    ],
                                'layout': go.Layout(
                                    xaxis=dict(
                                        type='category', 
                                        title='Date',
                                        domain=[0.00, 1.00],
                                        side = 'bottom',
                                        overlaying='y',
                                        automargin=True,
                                        showgrid=False
                                        ),
                                    yaxis=dict( 
                                        title='',
                                        titlefont=dict(color='#000000'),
                                        tickfont=dict(color='#000000'),
                                        side = 'left',
                                        rangemode = "tozero",
                                        #gridcolor='#FFFFFF',
                                        showgrid=False,
                                        range=[80000,200000]
                                        ),
                                    legend={'x': 0.60, 'y': 1},
                                    margin=dict(l=50,r=20,b=50,t=50)
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
                            id='speed-graph2',
                            #style={'width': 900,'height': 600},
                            figure={
                                'data': [
                                    go.Scattergl(
                                        x=fsovalidation2['Date'],
                                        y=fsovalidation2['ProfileFlowZeroCheck'],
                                        name='ProfileFlowZeroCheck',
                                        yaxis='y',
                                        mode='lines'
                                        ),
                                    go.Scattergl(
                                        x=fsovalidation2['Date'],
                                        y=fsovalidation2['TotalFlowZeroCheck'],
                                        name='TotalFlowZeroCheck',
                                        yaxis='y',
                                        mode='lines'
                                        ),
                                    ],
                                'layout': go.Layout(
                                    xaxis=dict(
                                        type='category', 
                                        title='Date',
                                        domain=[0.00, 1.00],
                                        side = 'bottom',
                                        overlaying='y',
                                        automargin=True,
                                        showgrid=False
                                        ),
                                    yaxis=dict( 
                                        title='',
                                        titlefont=dict(color='#000000'),
                                        tickfont=dict(color='#000000'),
                                        side = 'left',
                                        rangemode = "tozero",
                                        showgrid=False,
                                        range=[0,50000]
                                        #gridcolor='#FFFFFF'
                                        ),
                                    legend={'x': 0.60, 'y': 1},
                                    margin=dict(l=50,r=50,b=50,t=50)
                                    #height=100
                                    )
                                }
                            )
                    ]),width=6)
                ],no_gutters=True), #Row end
            dbc.Row([
                dbc.Col(
                    html.Div([
                        #html.H5('RIS 1 Traffic Data Validation'),
                        #html.Div(id='app-1-display-value'),
                        dcc.Graph(
                            id='speed-graph3',
                            #style={'width': 900,'height': 600},
                            figure={
                                'data': [
                                    go.Scattergl(
                                        x=fsovalidation2['Date'],
                                        y=fsovalidation2['RecordCountCheck'],
                                        name='RecordCountCheck',
                                        yaxis='y',
                                        mode='lines'
                                        )
                                    ],
                                'layout': go.Layout(
                                    xaxis=dict(
                                        type='category', 
                                        title='Date',
                                        domain=[0.00, 1.00],
                                        side = 'bottom',
                                        overlaying='y',
                                        automargin=True,
                                        showgrid=False
                                        ),
                                    yaxis=dict( 
                                        title='',
                                        titlefont=dict(color='#000000'),
                                        tickfont=dict(color='#000000'),
                                        side = 'left',
                                        rangemode = "tozero",
                                        #gridcolor='#FFFFFF',
                                        showgrid=False,
                                        range=[630000,680000]
                                        ),
                                    legend={'x': 0.60, 'y': 1},
                                    margin=dict(l=50,r=20,b=50,t=50),
                                    height=300
                                    )
                                }
                            )
                    ]),width=4),
                dbc.Col(
                    html.Div([
                        #html.H5('RIS 1 Traffic Data Validation'),
                        #html.Div(id='app-1-display-value'),
                        dcc.Graph(
                            id='speed-graph4',
                            #style={'width': 900,'height': 600},
                            figure={
                                'data': [
                                    go.Scattergl(
                                        x=fsovalidation2['Date'],
                                        y=fsovalidation2['NTISModelVersion'],
                                        name='NTISModelVersion',
                                        yaxis='y',
                                        mode='lines'
                                        )
                                    ],
                                'layout': go.Layout(
                                    xaxis=dict(
                                        type='category', 
                                        title='Date',
                                        domain=[0.00, 1.00],
                                        side = 'bottom',
                                        overlaying='y',
                                        automargin=True,
                                        showgrid=False
                                        ),
                                    yaxis=dict( 
                                        title='',
                                        titlefont=dict(color='#000000'),
                                        tickfont=dict(color='#000000'),
                                        side = 'left',
                                        rangemode = "tozero",
                                        #gridcolor='#FFFFFF',
                                        showgrid=False,
                                        range=[0,11]
                                        ),
                                    legend={'x': 0.60, 'y': 1},
                                    margin=dict(l=50,r=20,b=50,t=50),
                                    height=300
                                    )
                                }
                            )
                    ]),width=4),
                dbc.Col(
                    html.Div([
                        #html.H5('RIS 1 Traffic Data Validation'),
                        #html.Div(id='app-1-display-value'),
                        dcc.Graph(
                            id='speed-graph5',
                            #style={'width': 900,'height': 600},
                            figure={
                                'data': [
                                    go.Scattergl(
                                        x=fsovalidation2['Date'],
                                        y=fsovalidation2['TotalFlow_Max'],
                                        name='TotalFlow_Max',
                                        yaxis='y',
                                        mode='lines'
                                        ),
                                    go.Scattergl(
                                        x=fsovalidation2['Date'],
                                        y=fsovalidation2['ProfileFlow_Max'],
                                        name='ProfileFlow_Max',
                                        yaxis='y',
                                        mode='lines'
                                        )
                                    ],
                                'layout': go.Layout(
                                    xaxis=dict(
                                        type='category', 
                                        title='Date',
                                        domain=[0.00, 1.00],
                                        side = 'bottom',
                                        overlaying='y',
                                        automargin=True,
                                        showgrid=False
                                        ),
                                    yaxis=dict( 
                                        title='',
                                        titlefont=dict(color='#000000'),
                                        tickfont=dict(color='#000000'),
                                        side = 'left',
                                        rangemode = "tozero",
                                        #gridcolor='#FFFFFF',
                                        showgrid=False
                                        #range=[0,20000]
                                        ),
                                    legend={'x': 0.60, 'y': 1},
                                    margin=dict(l=50,r=20,b=50,t=50),
                                    height=300
                                    )
                                }
                            )
                    ]),width=4)],
                no_gutters=True) #Row end
                      
]) # Div layout end



# =============================================================================
# layout = html.Div([
#         html.H5('RIS 1 Traffic Data Validation'),
#         html.Div(id='app-1-display-value'),
#         dcc.Graph(
#             id='speed-graph',
#             figure={
#                 'data': [
#                     go.Scattergl(
#                         x=fsovalidation2['Date'],
#                         y=fsovalidation2['ProfileFlowNullCheck'],
#                         name='ProfileFlowNullCheck',
#                         yaxis='y',
#                         mode='lines'
#                         ),
#                     go.Scattergl(
#                         x=fsovalidation2['Date'],
#                         y=fsovalidation2['TotalFlowNullCheck'],
#                         name='TotalFlowNullCheck',
#                         yaxis='y',
#                         mode='lines'
#                         ),
#                     ],
#                 'layout': go.Layout(
#                     xaxis=dict(
#                         type='category', 
#                         title='Date',
#                         domain=[0.00, 0.95],
#                         side = 'bottom',
#                         overlaying='y',
#                         automargin=True
#                         ),
#                     yaxis=dict( 
#                         title='',
#                         titlefont=dict(color='#000000'),
#                         tickfont=dict(color='#000000'),
#                         side = 'left',
#                         rangemode = "tozero",
#                         gridcolor='#FFFFFF'
#                         ),
# 
#                     )
#                 }
#             )
# ])
# =============================================================================


# =============================================================================
# @app.callback(
#     Output('app-1-display-value', 'children'),
#     [Input('app-1-dropdown', 'value')])
# def display_value(value):
#     return 'You have selected "{}"'.format(value)
# =============================================================================
