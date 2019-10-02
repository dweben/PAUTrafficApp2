import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('\DataSamples\DataSetTesting_HGV.csv') # <<< read from csv
df1 = df[['NTISLinkID','DayTimePeriodID','YearID','MonthID','NTISDayTypeID','ProfileFlow','TotalFlow','RIS1ProfileFlow','ProfileSpeed','SpeedMph','SpeedLimitMph','InfillIncrement','WorksActive','ImpactActive']]
df2 = df1.sort_values(['DayTimePeriodID'])
df2['WorksActive'].fillna(0, inplace=True)
df2['ImpactActive'].fillna(0, inplace=True)
NTISLinkID1 = df2['NTISLinkID'] == 200045641
df3 = df2[NTISLinkID1]

layout = html.Div([
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(
                        id='dropdown_yearid', 
                        options=[{'label': i, 'value': i} for i in df3.YearID.unique()],
                        #value=df3.YearID.max(),
                        multi=True, 
                        placeholder='Filter by Year...'
                        ),
                ],width=2),
                dbc.Col([
                    dcc.Dropdown(
                        id='dropdown_monthid', 
                        options=[{'label': i, 'value': i} for i in df3.MonthID.unique()],
                        #value=df3.MonthID.max(),
                        multi=True, 
                        placeholder='Filter by Month...'
                        ),
                ],width=2),
                dbc.Col([
                    dcc.Dropdown(
                        id='dropdown_daytype', 
                        options=[{'label': i, 'value': i} for i in df3.NTISDayTypeID.unique()],
                        #value=df3.NTISDayTypeID.max(),
                        multi=True, 
                        placeholder='Filter by NTIS Day Type...'
                        ),
                ],width=2) 
            ]), # End of row element
            dbc.Row([
                dbc.Col([
                    dcc.Graph(
                        id='pau-graph',animate = False,
                        figure={
                            'data': [
                                go.Scattergl(    
                                    x=df3['DayTimePeriodID'],
                                    y=df3['ProfileFlow'],
                                    name='ProfileFlow',
                                    #yaxis='y1',
                                    mode='lines'
                                    ),
                                go.Scattergl(    
                                    x=df3['DayTimePeriodID'],
                                    y=df3['TotalFlow'],
                                    name='TotalFlow',
                                    #yaxis='y1',
                                    mode='lines'
                                ),
                                go.Scattergl(    
                                    x=df3['DayTimePeriodID'],
                                    y=df3['SpeedMph'],
                                    name='SpeedMph',
                                    #xaxis='x2',
                                    yaxis='y2',
                                    mode='lines'
                                ),
                                go.Scattergl(    
                                    x=df3['DayTimePeriodID'],
                                    y=df3['ProfileSpeed'],
                                    name='ProfileSpeed',
                                    #xaxis='x2',
                                    yaxis='y2',
                                    mode='lines'
                                ),
                                go.Scattergl(    
                                    x=df3['DayTimePeriodID'],
                                    y=df3['SpeedLimitMph'],
                                    name='SpeedLimitMph',
                                    #xaxis='x2',
                                    yaxis='y2',
                                    mode='lines',
                                    line = dict(dash = 'dash')
                                ),
                                go.Scattergl(    
                                    x=df3['DayTimePeriodID'],
                                    y=df3['WorksActive'],
                                    name='WorksActive',
                                    yaxis='y3',
                                    mode='none',
                                    fill='tozeroy',
                                    #stackgroup='one',
                                    line=dict(color='rgba(255,165,0,0.25)',width=1.5)
                                    #marker=dict(color='rgba(255,165,0,0.25)',
                                    #line=dict(color='rgba(255,165,0,0.25)',width=1.5))
                                ),
                                go.Scattergl(    
                                    x=df3['DayTimePeriodID'],
                                    y=df3['ImpactActive'],
                                    name='ImpactActive',
                                    yaxis='y3',
                                    mode='none',
                                    fill='tozeroy',
                                    #fill='tonexty',
                                    #stackgroup='one',
                                    line=dict(color='rgba(0,191,255,0.50)',width=1.5)
                                    #marker=dict(color='rgba(0,191,255,0.25)',
                                    #line=dict(color='rgba(0,191,255,0.25)',width=1.5))
                                ),
                                go.Scattergl(    
                                    x=df3['DayTimePeriodID'],
                                    y=df3['InfillIncrement'],
                                    name='InfillIncrement',
                                    yaxis='y4',
                                    mode='none',
                                    fill='tozeroy',
                                    #fill='tonexty',
                                    #stackgroup='one',
                                    line=dict(color='rgba(255,230,230,0.50)',width=1.5)
                                    #marker=dict(color='rgba(0,191,255,0.25)',
                                    #line=dict(color='rgba(0,191,255,0.25)',width=1.5))
                                )
                            ],
                            'layout': go.Layout(
                                xaxis=dict(
                                        type='category', 
                                        title='TimePeriodID',
                                        domain=[0.00, 0.95],
                                        side = 'bottom',
                                        overlaying='y',
                                        automargin=True,
                                        showgrid=False
                                        ),
                                yaxis=dict( 
                                        title='Flow',
                                        titlefont=dict(color='#000000'),
                                        tickfont=dict(color='#000000'),
                                        side = 'left',
                                        rangemode = "tozero",
                                        gridcolor='#757575',
                                        showgrid=False
                                        ),
                                yaxis2=dict( 
                                        title='Speed Mph',
                                        titlefont=dict(color='#000000'),
                                        tickfont=dict(color='#000000'),
                                        side = 'right',
                                        overlaying='y',
                                        rangemode = "tozero",
                                        gridcolor='#B2B2B2'
                                        ),   
                                yaxis3=dict( 
                                        #title='Works/Incident Active',
                                        #titlefont=dict(color='#000000'),
                                        #tickfont=dict(color='#000000'),
                                        side = 'right',
                                        overlaying='y',
                                        #rangemode = "tozero",
                                        #gridcolor='#B2B2B2',
                                        #anchor='free',
                                        #position=0.90,
                                        visible=False,
                                        range=[0,1],
                                        showgrid=False
                                        ),
                                yaxis4=dict( 
                                        #title='Infill Increment',
                                        #titlefont=dict(color='#000000'),
                                        #tickfont=dict(color='#000000'),
                                        side = 'right',
                                        overlaying='y',
                                        #rangemode = "tozero",
                                        #gridcolor='#B2B2B2',
                                        #anchor='free',
                                        #position=0.95,
                                        visible=False,
                                        range=[0,10],
                                        showgrid=False
                                        ),
                                    margin=dict(l=50,r=20,b=50,t=50),
                                    )
                                }
                            ) # End of graph
                        ],width=12) # End of col element
                    ]) # End of row element
                    
                ])
                        
