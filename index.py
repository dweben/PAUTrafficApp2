import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

from app import app
from apps import RIS1_DV, RIS2_LC,RIS2_DV, RIS2_Heatmaps, RIS2_Multi_Speed_Analysis, Examples


# =============================================================================
# df = pd.read_csv('\DataSamples\DataSetTesting_HGV.csv') # <<< read from csv
# df1 = df[['NTISLinkID','DayTimePeriodID','ProfileFlow','TotalFlow','RIS1ProfileFlow','ProfileSpeed','SpeedMph','SpeedLimitMph','InfillIncrement','WorksActive','ImpactActive']]
# df2 = df1.sort_values(['DayTimePeriodID'])
# df2['WorksActive'].fillna(0, inplace=True)
# df2['ImpactActive'].fillna(0, inplace=True)
# NTISLinkID1 = df2['NTISLinkID'] == 200045641
# df3 = df2[NTISLinkID1]
# 
# speedgraph = pd.read_csv('\DataSamples\MultiSpeed2.csv') # <<< read from csv
# speedgraph1 = speedgraph[['NTISLinkID','DayTimePeriodID','TravelSpeedMedian','FusedTravelSpeed','FVD_TravelSpeed','TravelSpeedAverage']]
# speedgraph2 = speedgraph1.sort_values(['DayTimePeriodID'])
# 
# speedgraph_v2 = pd.read_csv('\DataSamples\MultiSpeed3.csv') # <<< read from csv
# speedgraph_v2_1 = speedgraph_v2[['NTISLinkID','DayTimePeriodID','TravelSpeedMedianMph','TravelSpeedHarmonicMph','FusedTravelSpeedMph','FVD_TravelSpeedMph','FusedJTSpeedMph','FSOTravelSpeedMph','TNSpeedMph']]
# speedgraph_v2_2 = speedgraph_v2_1.sort_values(['DayTimePeriodID'])
# 
# fsovalidation = pd.read_csv('\DataSamples\DataValidation_FSO_20190717.csv') # <<< read from csv
# fsovalidation1 = fsovalidation[['Date','NTISModelVersion','ProfileFlowNullCheck','ProfileFlowZeroCheck','TotalFlowNullCheck','TotalFlowZeroCheck','TotalFlow_Max','ProfileFlow_Max','RecordCountCheck']]
# fsovalidation2 = fsovalidation1.sort_values(['Date'])
# =============================================================================

navbar = dbc.NavbarSimple(
                        children=[
                            #dbc.NavItem(dbc.NavLink("Home", href="http://127.0.0.1:8050/")),
                            dbc.NavItem(dbc.NavLink("RIS1 DV", href="/page-1"), id="page-1-link"),
                            #dbc.NavItem(divider=True),
                            dbc.NavItem(dbc.NavLink("RIS2 DV", href="/page-2"), id="page-2-link"),
                            dbc.NavItem(dbc.NavLink("RIS2 Link", href="/page-3"), id="page-3-link"),
                            dbc.NavItem(dbc.NavLink("RIS2 Heatmaps", href="/page-4"), id="page-4-link"),
                            dbc.NavItem(dbc.NavLink("RIS2 Multi Speed", href="/page-5"), id="page-5-link"),
                            dbc.NavItem(dbc.NavLink("Examples", href="/page-6"), id="page-6-link"),
                            #dbc.NavItem(divider=True),
                            dbc.DropdownMenu(
                                children=[
                                    dbc.DropdownMenuItem("RIS 1", header=True),
                                    dbc.DropdownMenuItem("Traffic Data Validation", href="#", id='ris1datavalidation'),
                                    dbc.DropdownMenuItem("RIS 2", header=True),
                                    dbc.DropdownMenuItem("Traffic Data Validation", href="#"),
                                    dbc.DropdownMenuItem("Link Validation", href="#"),
                                    dbc.DropdownMenuItem("Multispeed analysis", href="#"),
                                    dbc.DropdownMenuItem("Example Charts", header=True),
                                    dbc.DropdownMenuItem("Charts", href="#"),
                                ],
                                nav=True,
                                in_navbar=True,
                                label="Reports",
                                id='dropdownmenu1',
                            ),
                            dbc.DropdownMenu(
                                children=[
                                    dbc.DropdownMenuItem("GIS", header=True),
                                    dbc.DropdownMenuItem("NTIS Network Model", href="#"),
                                    dbc.DropdownMenuItem("GIS 2", href="#"),
                                    dbc.DropdownMenuItem("GIS 3", href="#"),
                                ],
                                nav=True,
                                in_navbar=True,
                                label="GIS",
                                id='dropdownmenu2',
                            ),
                            dbc.DropdownMenu(
                                children=[
                                    dbc.DropdownMenuItem("Dash Plotly", href="https://dash.plot.ly/"),
                                    dbc.DropdownMenuItem("Bootswatch", href="https://bootswatch.com/"),
                                ],
                                nav=True,
                                in_navbar=True,
                                label="Web",
                                id='dropdownmenu3',
                            ),            
                        ],
                        brand="PAU Traffic App",
                        brand_href=html.Img(src="/assets/sheep75px.png"),
                        color="dark",
                        dark=True,
                    )


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([navbar]),
    html.Div(id='page-content')
])

index_page = html.Div([
    #navbar,
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page-3'),
    html.Br(),
    dcc.Link('Go to Page 4', href='/page-4'),
    html.Br(),
    dcc.Link('Go to Page 5', href='/page-5'),
    html.Br(),
    dcc.Link('Go to Page 6', href='/page-6'),
])


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return RIS1_DV.layout
    elif pathname == '/page-2':
        return RIS2_DV.layout
    elif pathname == '/page-3':
        return RIS2_LC.layout
    elif pathname == '/page-4':
        return RIS2_Heatmaps.layout
    elif pathname == '/page-5':
        return RIS2_Multi_Speed_Analysis.layout
    elif pathname == '/page-6':
        return Examples.layout
    else:
        return index_page
    
# =============================================================================
# @app.callback(
#     Output('pau-graph', 'figure'),
#     [Input('dropdown_yearid', 'value'),
#      Input('dropdown_monthid', 'value')
#      ])
#                         
# def update_graph(xaxis_column_name, yaxis_column_name,
#                  xaxis_type, yaxis_type,
#                  year_value):
#     df3 = df3[df3['Year'] == year_value]
# =============================================================================




if __name__ == '__main__':
    app.run_server(debug=True)