import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go

validation = pd.read_csv('\DataSamples\InfillType_20190731.csv') # <<< read from csv
#validation = pd.read_csv('\DataSamples\MultiSpeed.csv') # <<< read from csv

validation1 = validation[['DayID','InfillType','InfillTypeCount']]
validation2 = validation1.sort_values(['DayID'])
validation_X = validation2[validation2.InfillType == 'X'][['DayID','InfillType','InfillTypeCount']]
validation_D = validation2[validation2.InfillType == 'D'][['DayID','InfillType','InfillTypeCount']]
validation_U = validation2[validation2.InfillType == 'U'][['DayID','InfillType','InfillTypeCount']]
validation_A = validation2[validation2.InfillType == 'A'][['DayID','InfillType','InfillTypeCount']]
validation_B = validation2[validation2.InfillType == 'B'][['DayID','InfillType','InfillTypeCount']]

ValidationSites_TN = pd.read_csv('\DataSamples\SitesVsTN_20190807_v2.csv')
ValidationSites_TN1 = ValidationSites_TN.sort_values(['DayID'])
ValidationSites_TN_Bin1 = ValidationSites_TN1[['DayID',' -1 to -0.5']]
ValidationSites_TN_Bin2 = ValidationSites_TN1[['DayID',' -0.5 to -0.05']]
ValidationSites_TN_Bin3 = ValidationSites_TN1[['DayID',' -0.05 to -0.025']]
ValidationSites_TN_Bin4 = ValidationSites_TN1[['DayID',' -0.025 to -0.005']]
ValidationSites_TN_Bin5 = ValidationSites_TN1[['DayID',' -0.005 to -0.0025']]
ValidationSites_TN_Bin6 = ValidationSites_TN1[['DayID',' -0.0025 to 0']]
ValidationSites_TN_Bin7 = ValidationSites_TN1[['DayID',' 0 to 0.0025']]
ValidationSites_TN_Bin8 = ValidationSites_TN1[['DayID',' 0.0025 to 0.005']]
ValidationSites_TN_Bin9 = ValidationSites_TN1[['DayID',' 0.005 to 0.025']]
ValidationSites_TN_Bin10 = ValidationSites_TN1[['DayID',' 0.025 to 0.05']]
ValidationSites_TN_Bin11 = ValidationSites_TN1[['DayID',' 0.05 to 0.5']]
ValidationSites_TN_Bin12 = ValidationSites_TN1[['DayID',' 0.5 to 1']]

DV_FusedIndex = pd.read_csv('\DataSamples\DV_FusedIndex_20190812.csv')
DV_FusedIndex01 = DV_FusedIndex.sort_values(['TravelDate'])
DV_FusedIndex01_Bin0 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_0']]
DV_FusedIndex01_Bin1 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_1']]
DV_FusedIndex01_Bin2 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_2']]
DV_FusedIndex01_Bin3 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_3']]
DV_FusedIndex01_Bin4 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_4']]
DV_FusedIndex01_Bin5 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_5']]
DV_FusedIndex01_Bin6 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_6']]
DV_FusedIndex01_Bin7 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_7']]
DV_FusedIndex01_Bin8 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_8']]
DV_FusedIndex01_Bin9 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_9']]
DV_FusedIndex01_Bin10 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_10']]
DV_FusedIndex01_Bin11 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_11']]
DV_FusedIndex01_Bin12 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_12']]
DV_FusedIndex01_Bin13 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_13']]
DV_FusedIndex01_Bin14 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_14']]
DV_FusedIndex01_Bin15 = DV_FusedIndex01[['TravelDate','FusedIndex_Prop_15']]

DV_FusedIndex_TimePeriod_HeatMap = pd.read_csv('\DataSamples\DV_FusedIndexTimePeriod_20190814.csv')
DV_FusedIndex_TimePeriod_HeatMap_01 = DV_FusedIndex_TimePeriod_HeatMap[['DateID','TimePeriodID','FusedIndex_Prop_0','FusedIndex_Prop_12','FusedIndex_Prop_13','FusedIndex_Prop_14','FusedIndex_Prop_15']]
DV_FusedIndex_TimePeriod_HeatMap_02 = DV_FusedIndex_TimePeriod_HeatMap_01.sort_values(['DateID','TimePeriodID'])

DV_Fused_Coverage = pd.read_csv('\DataSamples\DV_Fused_Coverage_20190815.csv')
DV_Fused_Coverage_01 = DV_Fused_Coverage[['TravelDate','TimePeriodID','Prop_ALL']]
DV_Fused_Coverage_02 = DV_Fused_Coverage_01.sort_values(['TravelDate','TimePeriodID'])

# =============================================================================
# M25_Incident = pd.read_csv('\DataSamples\M25_Incident_Example.csv')
# M25_Incident_01 = M25_Incident.sort_values(['TravelDate','TimePeriodID'])
# M25_Incident_199056602 = M25_Incident_01[M25_Incident_01.NTISLinkID==199056602][['NTISLinkID','TravelDate','TimePeriodID','SpeedMph']]
# M25_Incident_200047941 = M25_Incident_01[M25_Incident_01.NTISLinkID==200047941][['NTISLinkID','TravelDate','TimePeriodID','SpeedMph']]
# =============================================================================
M25_Incident = pd.read_csv('\DataSamples\M25_Test2.csv')
M25_Incident_01 = M25_Incident.sort_values(['TravelDate','TimePeriodID'])

M25_IncidentDay = pd.read_csv('\DataSamples\M25_Test3.csv')
M25_IncidentDay_01 = M25_IncidentDay.sort_values(['SequenceID','TravelDate','TimePeriodID'])

validationTotalFlow = pd.read_csv('\DataSamples\TotalFlowHistogram_20190812.csv') # <<< read from csv
validationTotalFlow1 = validationTotalFlow[['YearID','TotalFlow','TotalFlow_Count']]
validationTotalFlow2 = validationTotalFlow1.sort_values(['YearID','TotalFlow'])

validationTags = pd.read_csv('\DataSamples\ImpactWorksTags_20190731.csv') # <<< read from csv
validationTags1 = validationTags[['DayID','ImpactCount','WorksCount']]
validationTags2 = validationTags1.sort_values(['DayID'])

validationNew5Tags = pd.read_csv('\DataSamples\ImpactWorksTags_20190806_New5_v2.csv') # <<< read from csv
validationNew5Tags1 = validationNew5Tags[['DayID','ImpactCount','WorksCount']]
validationNew5Tags2 = validationNew5Tags1.sort_values(['DayID'])


layout = html.Div([
        #Null Checks
            #dbc.Row(dbc.Col(html.H3('RIS 1 Traffic Data Validation'))),
            dbc.Row([
                    dbc.Col(
                    html.Div([
                        #html.H5('RIS 1 Traffic Data Validation'),
                        #html.Div(id='app-1-display-value'),
                        dcc.Graph(
                            id='TN_FVD_Validation',
                            #style={'width': 900,'height': 600},
                            figure={
                                'data': [
                                    go.Scatter(
                                        x=ValidationSites_TN_Bin1['DayID'],
                                        y=ValidationSites_TN_Bin1[' -1 to -0.5'],
                                        name=' -1 to -0.5',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(3, 252, 74)'),
                                        stackgroup='one',
                                        ),
# =============================================================================
#                                     go.Scatter(
#                                         x=ValidationSites_TN_Bin1['TravelDate'],
#                                         y=ValidationSites_TN_Bin1['FusedIndex_Prop_0'],
#                                         name='FusedIndex_0',
#                                         yaxis='y',
#                                         mode='lines',
#                                         line=dict(width=0.1, color='rgb(0, 46, 95)'),
#                                         stackgroup='one',
#                                         ),
# =============================================================================
                                    go.Scatter(
                                        x=ValidationSites_TN_Bin2['DayID'],
                                        y=ValidationSites_TN_Bin2[' -0.5 to -0.05'],
                                        name=' -0.5 to -0.05',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(0, 139, 203)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=ValidationSites_TN_Bin3['DayID'],
                                        y=ValidationSites_TN_Bin3[' -0.05 to -0.025'],
                                        name=' -0.05 to -0.025',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(74, 74, 74)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=ValidationSites_TN_Bin4['DayID'],
                                        y=ValidationSites_TN_Bin4[' -0.025 to -0.005'],
                                        name=' -0.025 to -0.005',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(255, 47, 168)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=ValidationSites_TN_Bin5['DayID'],
                                        y=ValidationSites_TN_Bin5[' -0.005 to -0.0025'],
                                        name=' -0.005 to -0.0025',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(214, 214, 255)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=ValidationSites_TN_Bin6['DayID'],
                                        y=ValidationSites_TN_Bin6[' -0.0025 to 0'],
                                        name=' -0.0025 to 0',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(255, 46, 12)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=ValidationSites_TN_Bin7['DayID'],
                                        y=ValidationSites_TN_Bin7[' 0 to 0.0025'],
                                        name=' 0 to 0.0025',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(255, 229, 156)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=ValidationSites_TN_Bin8['DayID'],
                                        y=ValidationSites_TN_Bin8[' 0.0025 to 0.005'],
                                        name=' 0.0025 to 0.005',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(255, 9, 23)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=ValidationSites_TN_Bin9['DayID'],
                                        y=ValidationSites_TN_Bin9[' 0.005 to 0.025'],
                                        name=' 0.005 to 0.025',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(255, 132, 0)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=ValidationSites_TN_Bin10['DayID'],
                                        y=ValidationSites_TN_Bin10[' 0.025 to 0.05'],
                                        name=' 0.025 to 0.05',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(141, 255, 63)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=ValidationSites_TN_Bin11['DayID'],
                                        y=ValidationSites_TN_Bin11[' 0.05 to 0.5'],
                                        name=' 0.05 to 0.5',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(0, 249, 255)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=ValidationSites_TN_Bin12['DayID'],
                                        y=ValidationSites_TN_Bin12[' 0.5 to 1'],
                                        name=' 0.5 to 1',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(235, 64, 52)'),
                                        stackgroup='one',
                                        ),
                                    ],
                                'layout': go.Layout(
                                    xaxis=dict(
                                        type='category', 
                                        title='Date',
                                        domain=[0.00, 0.90],
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
                                        #range=[80000,200000]
                                        ),
                                    legend={'x': 0.90, 'y': 1},
                                    margin=dict(l=50,r=20,b=50,t=50),
                                    barmode='stack',
                                    title='Daily proportion of speed (TN Cars - Harmonic Site Speed/Harmonic Site Speed) by Bins '
                                    )
                                }
                            )
                    ]),width=12),
                ],no_gutters=True), #Row end
                dbc.Row([
                    dbc.Col(
                    html.Div([
                        #html.H5('RIS 1 Traffic Data Validation'),
                        #html.Div(id='app-1-display-value'),
                        dcc.Graph(
                            id='Fused_Index',
                            #style={'width': 900,'height': 600},
                            figure={
                                'data': [
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin0['TravelDate'],
                                        y=DV_FusedIndex01_Bin0['FusedIndex_Prop_0'],
                                        name='FusedIndex_0',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(0, 46, 95)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin1['TravelDate'],
                                        y=DV_FusedIndex01_Bin1['FusedIndex_Prop_1'],
                                        name='FusedIndex_1',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(0, 139, 203)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin2['TravelDate'],
                                        y=DV_FusedIndex01_Bin2['FusedIndex_Prop_2'],
                                        name='FusedIndex_2',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(74, 74, 74)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin3['TravelDate'],
                                        y=DV_FusedIndex01_Bin3['FusedIndex_Prop_3'],
                                        name='FusedIndex_3',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(255, 47, 168)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin4['TravelDate'],
                                        y=DV_FusedIndex01_Bin4['FusedIndex_Prop_4'],
                                        name='FusedIndex_4',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(214, 214, 255)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin5['TravelDate'],
                                        y=DV_FusedIndex01_Bin5['FusedIndex_Prop_5'],
                                        name='FusedIndex_5',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(255, 46, 12)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin6['TravelDate'],
                                        y=DV_FusedIndex01_Bin6['FusedIndex_Prop_6'],
                                        name='FusedIndex_6',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(255, 229, 156)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin7['TravelDate'],
                                        y=DV_FusedIndex01_Bin7['FusedIndex_Prop_7'],
                                        name='FusedIndex_7',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(255, 9, 23)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin8['TravelDate'],
                                        y=DV_FusedIndex01_Bin8['FusedIndex_Prop_8'],
                                        name='FusedIndex_8',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(255, 132, 0)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin9['TravelDate'],
                                        y=DV_FusedIndex01_Bin9['FusedIndex_Prop_9'],
                                        name='FusedIndex_9',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(141, 255, 63)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin10['TravelDate'],
                                        y=DV_FusedIndex01_Bin10['FusedIndex_Prop_10'],
                                        name='FusedIndex_10',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(0, 249, 255)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin11['TravelDate'],
                                        y=DV_FusedIndex01_Bin11['FusedIndex_Prop_11'],
                                        name='FusedIndex_11',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(243, 255, 253)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin12['TravelDate'],
                                        y=DV_FusedIndex01_Bin12['FusedIndex_Prop_12'],
                                        name='FusedIndex_12',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(91, 19, 96)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin13['TravelDate'],
                                        y=DV_FusedIndex01_Bin13['FusedIndex_Prop_13'],
                                        name='FusedIndex_13',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(161, 252, 3)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin14['TravelDate'],
                                        y=DV_FusedIndex01_Bin14['FusedIndex_Prop_14'],
                                        name='FusedIndex_14',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(3, 252, 74)'),
                                        stackgroup='one',
                                        ),
                                    go.Scatter(
                                        x=DV_FusedIndex01_Bin15['TravelDate'],
                                        y=DV_FusedIndex01_Bin15['FusedIndex_Prop_15'],
                                        name='FusedIndex_15',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(255,250,205)'),
                                        stackgroup='one',
                                        ),
                                    ],
                                'layout': go.Layout(
                                    xaxis=dict(
                                        type='category', 
                                        title='Date',
                                        domain=[0.00, 0.90],
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
                                        #range=[80000,200000]
                                        ),
                                    legend={'x': 0.90, 'y': 1},
                                    margin=dict(l=50,r=20,b=50,t=50),
                                    barmode='stack',
                                    title='Fused JT Indices, mainCarriagway SRN only'
                                    )
                                }
                            )
                    ]),width=12),
                ],no_gutters=True), #Row end
                 # Zero Checks 
             dbc.Row([
                     dbc.Col(
                        html.Div([
                            #html.H5('RIS 1 Traffic Data Validation'),
                            #html.Div(id='app-1-display-value'),
                            dcc.Graph(
                                id='jt_index_0',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=DV_FusedIndex_TimePeriod_HeatMap_01['DateID'],
                                            y=DV_FusedIndex_TimePeriod_HeatMap_01['TimePeriodID'],
                                            z=DV_FusedIndex_TimePeriod_HeatMap_01['FusedIndex_Prop_0'],
                                            name='FusedIndex_Prop_15',
                                            colorscale='Viridis',
                                            zmin=0,
                                            zmax=1
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        #height=300,
                                        title='Fused JT FusedIndex_Prop_0 (Carr/SRN only)'
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
                                id='jt_index_15',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=DV_FusedIndex_TimePeriod_HeatMap_01['DateID'],
                                            y=DV_FusedIndex_TimePeriod_HeatMap_01['TimePeriodID'],
                                            z=DV_FusedIndex_TimePeriod_HeatMap_01['FusedIndex_Prop_15'],
                                            name='FusedIndex_Prop_15',
                                            colorscale='Viridis',
                                            zmin=0,
                                            zmax=1
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        #height=300,
                                        title='Fused JT FusedIndex_Prop_15 (Carr/SRN only)'
                                        #barmode='stack'
                                        )
                                    }
                                )
                        ]),width=6),
                 # Zero Checks    
                 ],no_gutters=True), #Row end
                      
             dbc.Row([
                     dbc.Col(
                        html.Div([
                            #html.H5('RIS 1 Traffic Data Validation'),
                            #html.Div(id='app-1-display-value'),
                            dcc.Graph(
                                id='jt_index_12',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=DV_FusedIndex_TimePeriod_HeatMap_01['DateID'],
                                            y=DV_FusedIndex_TimePeriod_HeatMap_01['TimePeriodID'],
                                            z=DV_FusedIndex_TimePeriod_HeatMap_01['FusedIndex_Prop_12'],
                                            name='FusedIndex_Prop_12',
                                            colorscale='Viridis',
                                            zmin=0,
                                            zmax=1
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        height=300,
                                        title='Fused JT FusedIndex_Prop_12 (Carr/SRN only)'
                                        #barmode='stack'
                                        )
                                    }
                                )
                        ]),width=4),
                    dbc.Col(
                        html.Div([
                            #html.H5('RIS 1 Traffic Data Validation'),
                            #html.Div(id='app-1-display-value'),
                            dcc.Graph(
                                id='jt_index_13',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=DV_FusedIndex_TimePeriod_HeatMap_01['DateID'],
                                            y=DV_FusedIndex_TimePeriod_HeatMap_01['TimePeriodID'],
                                            z=DV_FusedIndex_TimePeriod_HeatMap_01['FusedIndex_Prop_13'],
                                            name='FusedIndex_Prop_13',
                                            colorscale='Viridis',
                                            zmin=0,
                                            zmax=1
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        height=300,
                                        title='Fused JT FusedIndex_Prop_13 (Carr/SRN only)'
                                        #barmode='stack'
                                        )
                                    }
                                )
                        ]),width=4),
                    dbc.Col(
                        html.Div([
                            #html.H5('RIS 1 Traffic Data Validation'),
                            #html.Div(id='app-1-display-value'),
                            dcc.Graph(
                                id='jt_index_14',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=DV_FusedIndex_TimePeriod_HeatMap_01['DateID'],
                                            y=DV_FusedIndex_TimePeriod_HeatMap_01['TimePeriodID'],
                                            z=DV_FusedIndex_TimePeriod_HeatMap_01['FusedIndex_Prop_14'],
                                            name='FusedIndex_Prop_14',
                                            colorscale='Viridis',
                                            zmin=0,
                                            zmax=1
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        height=300,
                                        title='Fused JT FusedIndex_Prop_14 (Carr/SRN only)'
                                        #barmode='stack'
                                        )
                                    }
                                )
                        ]),width=4),
                 # Zero Checks    
                 ],no_gutters=True), #Row end
             dbc.Row([
                     dbc.Col(
                        html.Div([
                            #html.H5('RIS 1 Traffic Data Validation'),
                            #html.Div(id='app-1-display-value'),
                            dcc.Graph(
                                id='jt_coverage_0',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=DV_Fused_Coverage_02['TravelDate'],
                                            y=DV_Fused_Coverage_02['TimePeriodID'],
                                            z=DV_Fused_Coverage_02['Prop_ALL'],
                                            name='Fused Coverage',
                                            #colorscale='Viridis',
                                            colorscale=[[0, 'red'], [0.8, 'red'], [1.0, 'green']],
                                            zmin=0,
                                            zmax=1
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        #height=300,
                                        title='Fused JT Coverage (Carr/SRN only)'
                                        #barmode='stack'
                                        )
                                    }
                                )
                        ]),width=12),   
                 ],no_gutters=True), #Row end
                                
             dbc.Row([
                     dbc.Col(
                        html.Div([
                            #html.H5('RIS 1 Traffic Data Validation'),
                            #html.Div(id='app-1-display-value'),
                            dcc.Graph(
                                id='M25_Incident_Range',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=M25_Incident_01['TravelDate'],
                                            y=M25_Incident_01['TimePeriodID'],
                                            z=M25_Incident_01['SpeedMph'],
                                            name='M25_Incident_01',
                                            colorscale='Viridis',
                                            #colorscale=[[0, 'red'], [0.8, 'red'], [1.0, 'green']],
                                            zmin=0,
                                            zmax=80
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        #height=300,
                                        title='M25_Incident'
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
                                id='M25_Incident_Day',
                                #style={'width': 900,'height': 600},
                                figure={
                                    'data': [
                                        go.Heatmap(
                                            x=M25_IncidentDay_01['SequenceID'],
                                            y=M25_IncidentDay_01['TimePeriodID'],
                                            z=M25_IncidentDay_01['SpeedMph'],
                                            name='M25_Incident_Day',
                                            colorscale='Viridis',
                                            #colorscale=[[0, 'red'], [0.8, 'red'], [1.0, 'green']],
                                            zmin=0,
                                            zmax=80
                                            #yaxis='y',
                                            #mode='lines'
                                            ),
                                        ],
                                    'layout': go.Layout(
                                        #legend={'x': 0.30, 'y': 1},
                                        #rangemode = "tozero",
                                        margin=dict(l=50,r=50,b=50,t=50),
                                        #height=300,
                                        title='M25_Incident'
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
                            id='speed-graph2',
                            #style={'width': 900,'height': 600},
                            figure={
                                'data': [
                                    go.Scatter(
                                        x=validationTags2['DayID'],
                                        y=validationTags2['ImpactCount'],
                                        name='ImpactCount',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(3, 252, 74)'),
                                        stackgroup='one',
                                        #mode='lines'
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
                                        #range=[80000,200000]
                                        ),
                                    legend={'x': 0.30, 'y': 1},
                                    margin=dict(l=50,r=50,b=50,t=50),
                                    height=300,
                                    title='Count of Impact events per day'
                                    #barmode='stack'
                                    )
                                }
                            )
                    ]),width=4),
                dbc.Col(
                    html.Div([
                        #html.H5('RIS 1 Traffic Data Validation'),
                        #html.Div(id='app-1-display-value'),
                        dcc.Graph(
                            id='speed-graph3',
                            #style={'width': 900,'height': 600},
                            figure={
                                'data': [
                                    go.Scatter(
                                        x=validationTags2['DayID'],
                                        y=validationTags2['WorksCount'],
                                        name='WorksCount',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(3, 252, 74)'),
                                        stackgroup='one',
                                        #mode='lines'
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
                                        #range=[80000,200000]
                                        ),
                                    legend={'x': 0.30, 'y': 1},
                                    margin=dict(l=50,r=50,b=50,t=50),
                                    height=300,
                                    title='Count of Works events per day'
                                    #barmode='stack'
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
                                        x=validationTotalFlow2[validationTotalFlow2['YearID'] == i]['TotalFlow'],
                                        y=validationTotalFlow2[validationTotalFlow2['YearID'] == i]['TotalFlow_Count'],
                                        #name='TotalFlow',
                                        yaxis='y',
                                        mode='lines',
                                        name = str(i)
                                        ) for i in validationTotalFlow2.YearID.unique()
                                    ],
                                'layout': go.Layout(
                                    xaxis=dict(
                                        type='category', 
                                        title='TotalFlow Bins',
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
                                        #color='YearID',
                                        #range=[80000,200000]
                                        ),
                                    legend={'x': 0.60, 'y': 1},
                                    margin=dict(l=50,r=20,b=50,t=50),
                                    height=300,
                                    title='TotalFlow Histogram By Year',
                                    #barmode='stack'
                                    )
                                }
                            )
                    ]),width=4)
                ],no_gutters=True), #Row end
                            
                dbc.Row([
                    dbc.Col(
                    html.Div([
                        #html.H5('RIS 1 Traffic Data Validation'),
                        #html.Div(id='app-1-display-value'),
                        dcc.Graph(
                            id='speed-graph5',
                            #style={'width': 900,'height': 600},
                            figure={
                                'data': [
                                    go.Scatter(
                                        x=validationNew5Tags2['DayID'],
                                        y=validationNew5Tags2['ImpactCount'],
                                        name='ImpactCount',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(3, 252, 74)'),
                                        stackgroup='one',
                                        #mode='lines'
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
                                        #range=[80000,200000]
                                        ),
                                    legend={'x': 0.30, 'y': 1},
                                    margin=dict(l=50,r=50,b=50,t=50),
                                    height=300,
                                    title='Count of New5 Impact events per day'
                                    #barmode='stack'
                                    )
                                }
                            )
                    ]),width=4),
                dbc.Col(
                    html.Div([
                        #html.H5('RIS 1 Traffic Data Validation'),
                        #html.Div(id='app-1-display-value'),
                        dcc.Graph(
                            id='speed-graph6',
                            #style={'width': 900,'height': 600},
                            figure={
                                'data': [
                                    go.Scatter(
                                        x=validationNew5Tags2['DayID'],
                                        y=validationNew5Tags2['WorksCount'],
                                        name='WorksCount',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(3, 252, 74)'),
                                        stackgroup='one',
                                        #mode='lines'
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
                                        #range=[80000,200000]
                                        ),
                                    legend={'x': 0.30, 'y': 1},
                                    margin=dict(l=50,r=50,b=50,t=50),
                                    height=300,
                                    title='Count of New5 Works events per day'
                                    #barmode='stack'
                                    )
                                }
                            )
                    ]),width=4),
                dbc.Col(
                    html.Div([
                        #html.H5('RIS 1 Traffic Data Validation'),
                        #html.Div(id='app-1-display-value'),
                        dcc.Graph(
                            id='infilltype01',
                            #style={'width': 900,'height': 600},
                            figure={
                                'data': [
                                    go.Scatter(
                                        x=validation_X['DayID'],
                                        y=validation_X['InfillTypeCount'],
                                        name='InfillType_X',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(255, 47, 168)'),
                                        stackgroup='one',
                                        #mode='lines'
                                        ),
                                    go.Scatter(
                                        x=validation_D['DayID'],
                                        y=validation_D['InfillTypeCount'],
                                        name='InfillType_D',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(0, 139, 203)'),
                                        stackgroup='one',
                                        #mode='lines'
                                        ),
                                    go.Scatter(
                                        x=validation_U['DayID'],
                                        y=validation_U['InfillTypeCount'],
                                        name='InfillType_U',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(255, 132, 0)'),
                                        stackgroup='one',
                                        #mode='lines'
                                        ),
                                    go.Scatter(
                                        x=validation_A['DayID'],
                                        y=validation_A['InfillTypeCount'],
                                        name='InfillType_A',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(74, 74, 74)'),
                                        stackgroup='one',
                                        #mode='lines'
                                        ),
                                    go.Scatter(
                                        x=validation_B['DayID'],
                                        y=validation_B['InfillTypeCount'],
                                        name='InfillType_B',
                                        yaxis='y',
                                        mode='lines',
                                        line=dict(width=0.1, color='rgb(3, 252, 74)'),
                                        stackgroup='one',
                                        #mode='lines'
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
                                        #range=[80000,200000]
                                        ),
                                    legend={'x': 0.60, 'y': 1},
                                    margin=dict(l=50,r=50,b=50,t=50),
                                    height=300,
                                    barmode='stack',
                                    title='Count of infill type'
                                    )
                                }
                            )
                    ]),width=4),
                ],no_gutters=True), #Row end
]) # Div layout end