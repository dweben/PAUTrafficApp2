import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

speedgraph_v2 = pd.read_csv('\DataSamples\MultiSpeed3.csv') # <<< read from csv
speedgraph_v2_1 = speedgraph_v2[['NTISLinkID','DayTimePeriodID','TravelSpeedMedianMph','TravelSpeedHarmonicMph','FusedTravelSpeedMph','FVD_TravelSpeedMph','FusedJTSpeedMph','FSOTravelSpeedMph','TNSpeedMph']]
speedgraph_v2_2 = speedgraph_v2_1.sort_values(['DayTimePeriodID'])


layout = html.Div([
            html.H3('Multi Speed Analysis'),
            dcc.Graph(
                id='speed-graph',
                figure={
                    'data': [
                        go.Scattergl(
                            x=speedgraph_v2_2['DayTimePeriodID'],
                            y=speedgraph_v2_2['TravelSpeedMedianMph'],
                            name='TravelSpeedMedianMph',
                            mode='lines'
                            ),
                        go.Scattergl(
                            x=speedgraph_v2_2['DayTimePeriodID'],
                            y=speedgraph_v2_2['TravelSpeedHarmonicMph'],
                            name='TravelSpeedHarmonicMph',
                            mode='lines'
                            ),
                        go.Scattergl(
                            x=speedgraph_v2_2['DayTimePeriodID'],
                            y=speedgraph_v2_2['FusedTravelSpeedMph'],
                            name='FusedTravelSpeedMph',
                            mode='lines'
                            ),
                        go.Scattergl(
                            x=speedgraph_v2_2['DayTimePeriodID'],
                            y=speedgraph_v2_2['FVD_TravelSpeedMph'],
                            name='FVD_TravelSpeedMph',
                            mode='lines'
                            ),
                        go.Scattergl(
                            x=speedgraph_v2_2['DayTimePeriodID'],
                            y=speedgraph_v2_2['FusedJTSpeedMph'],
                            name='FusedJTSpeedMph',
                            mode='lines'
                            ),
                        go.Scattergl(
                            x=speedgraph_v2_2['DayTimePeriodID'],
                            y=speedgraph_v2_2['FSOTravelSpeedMph'],
                            name='FSOTravelSpeedMph',
                            mode='lines'
                            ),
                        go.Scattergl(
                            x=speedgraph_v2_2['DayTimePeriodID'],
                            y=speedgraph_v2_2['TNSpeedMph'],
                            name='TNSpeedMph',
                            mode='lines'
                            )
                        ],
                    'layout': go.Layout(
                        xaxis=dict(
                            type='category', 
                            title='TimePeriodID',
                            domain=[0.00, 0.85],
                            side = 'bottom',
                            overlaying='y',
                            automargin=True
                            ),
                        yaxis=dict( 
                            title='Site Median Speed',
                            titlefont=dict(color='#000000'),
                            tickfont=dict(color='#000000'),
                            side = 'left',
                            rangemode = "tozero",
                            gridcolor='#757575'
                            )
                        )
                        
                }
            )
        ])