"""
SpaceX Falcon 9 Launch Analytics Dashboard
===========================================
An interactive web dashboard for analyzing SpaceX Falcon 9 launch data,
including success rates, payload analysis, and site-specific insights.

"""

# Import required libraries
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# ============================================================================
# DATA LOADING
# ============================================================================

# Read the SpaceX launch data into pandas dataframe
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "spacex_launch_data_clean.csv")
spacex_df = pd.read_csv(csv_path)
max_payload = spacex_df['PayloadMass'].max()
min_payload = spacex_df['PayloadMass'].min()

# ============================================================================
# DASH APP INITIALIZATION
# ============================================================================

# Create a dash application
app = dash.Dash(__name__)
app.title = "SpaceX Launch Analytics"

# ============================================================================
# COLOR SCHEME & STYLING
# ============================================================================

# Define color scheme - Professional Light Theme
colors = {
    'background': '#f5f7fa',
    'card_bg': '#ffffff',
    'text': '#2c3e50',
    'primary': '#3498db',
    'secondary': '#95a5a6',
    'success': '#27ae60',
    'danger': '#e74c3c',
    'warning': '#f39c12',
    'border': '#ecf0f1'
}

# Card styling
card_style = {
    'backgroundColor': colors['card_bg'],
    'padding': '25px',
    'borderRadius': '12px',
    'marginBottom': '20px',
    'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.08)',
    'border': f'1px solid {colors["border"]}'
}

# Header styling
header_style = {
    'textAlign': 'center',
    'color': colors['text'],
    'marginBottom': '10px',
    'fontWeight': 'bold',
    'fontSize': '42px'
}

# Subtitle styling
subtitle_style = {
    'textAlign': 'center',
    'color': colors['secondary'],
    'marginBottom': '40px',
    'fontSize': '18px'
}

# ============================================================================
# DASHBOARD LAYOUT
# ============================================================================

app.layout = html.Div(
    style={'backgroundColor': colors['background'], 'minHeight': '100vh', 'padding': '0'},
    children=[
        html.Div(
            style={'maxWidth': '1400px', 'margin': '0 auto', 'padding': '20px'},
            children=[
        # Header Section
        html.Div([
            html.H1('🚀 SpaceX Falcon 9 Launch Analytics Dashboard', style=header_style),
            html.P('Interactive Analysis of First Stage Landing Predictions', style=subtitle_style),
        ]),
        
        # Stats Cards Row
        html.Div(id='stats-cards', style={'marginBottom': '30px'}),
        
        # Control Panel
        html.Div(
            style=card_style,
            children=[
                html.Label('🎯 Select Launch Site:', 
                          style={'color': colors['text'], 'fontSize': '18px', 'fontWeight': 'bold', 'marginBottom': '10px', 'display': 'block'}),
                dcc.Dropdown(
                    id='site-dropdown',
                    options=[
                        {'label': '🌍 All Sites', 'value': 'ALL'},
                        {'label': '🇺🇸 CCAFS LC-40', 'value': 'CCAFS LC-40'},
                        {'label': '🇺🇸 CCSFS SLC 40', 'value': 'CCSFS SLC 40'},
                        {'label': '🇺🇸 KSC LC-39A', 'value': 'KSC LC-39A'},
                        {'label': '🇺🇸 VAFB SLC-4E', 'value': 'VAFB SLC 4E'}
                    ],
                    value='ALL',
                    placeholder="Select a Launch Site",
                    searchable=True,
                    style={
                        'backgroundColor': colors['card_bg'], 
                        'color': colors['text'],
                        'borderRadius': '5px'
                    }
                ),
            ]
        ),
        
        # Chart: Pie Chart with Insights
        html.Div(
            style=card_style,
            children=[
                html.Div([
                    dcc.Graph(id='success-pie-chart')
                ], style={'width': '60%', 'display': 'inline-block', 'verticalAlign': 'top'}),
                
                html.Div([
                    html.Div(id='pie-insights')
                ], style={'width': '40%', 'display': 'inline-block', 'padding': '20px', 'verticalAlign': 'top'}),
            ]
        ),
        
        # Payload Slider Section
        html.Div(
            style=card_style,
            children=[
                html.Label('📊 Payload Mass Range (Kg):', 
                          style={'color': colors['text'], 'fontSize': '18px', 'fontWeight': 'bold', 'marginBottom': '15px', 'display': 'block'}),
                dcc.RangeSlider(
                    id='payload-slider',
                    min=0,
                    max=10000,
                    step=500,
                    marks={i: {'label': f'{i:,}', 'style': {'color': colors['text']}} 
                           for i in range(0, 11000, 2000)},
                    value=[min_payload, max_payload],
                    tooltip={"placement": "bottom", "always_visible": True}
                ),
            ]
        ),
        
        # Charts Row 2: Scatter Plot with Insights
        html.Div(
            style=card_style,
            children=[
                html.Div([
                    dcc.Graph(id='success-payload-scatter-chart')
                ], style={'width': '70%', 'display': 'inline-block', 'verticalAlign': 'top'}),
                
                html.Div([
                    html.Div(id='scatter-insights')
                ], style={'width': '30%', 'display': 'inline-block', 'padding': '20px', 'verticalAlign': 'top'}),
            ]
        ),
        
        # Bar Chart with Insights
        html.Div(
            style=card_style,
            children=[
                html.Div([
                    dcc.Graph(id='orbit-success-bar-chart')
                ], style={'width': '60%', 'display': 'inline-block', 'verticalAlign': 'top'}),
                
                html.Div([
                    html.Div(id='orbit-insights')
                ], style={'width': '40%', 'display': 'inline-block', 'padding': '20px', 'verticalAlign': 'top'}),
            ]
        ),
        
        # Timeline Chart with Insights
        html.Div(
            style=card_style,
            children=[
                html.Div([
                    dcc.Graph(id='timeline-chart')
                ], style={'width': '100%', 'display': 'block'}),
                
                html.Div([
                    html.Div(id='timeline-insights')
                ], style={'width': '100%', 'display': 'block', 'padding': '20px 0'}),
            ]
        ),
        
        # Footer
        html.Div([
            html.Hr(style={'borderColor': colors['border']}),
            html.P('Data Source: SpaceX Launch Records | Dashboard by Visura Rodrigo',
                   style={'textAlign': 'center', 'color': colors['text'], 'fontSize': '14px', 'marginTop': '20px'})
        ])
            ]
        )
    ]
)

# ============================================================================
# CALLBACK FUNCTIONS
# ============================================================================

# Callback for Stats Cards
@app.callback(
    Output('stats-cards', 'children'),
    Input('site-dropdown', 'value')
)
def update_stats_cards(entered_site):
    if entered_site == 'ALL':
        filtered_df = spacex_df
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == entered_site]
    
    total_launches = len(filtered_df)
    successful_launches = filtered_df['Class'].sum()
    success_rate = (successful_launches / total_launches * 100) if total_launches > 0 else 0
    avg_payload = filtered_df['PayloadMass'].mean()
    
    return html.Div(
        style={'display': 'flex', 'justifyContent': 'space-between', 'gap': '15px', 'flexWrap': 'nowrap'},
        children=[
            html.Div([
                html.H3('📈 Total Launches', style={'color': colors['text'], 'fontSize': '16px', 'marginBottom': '10px', 'fontWeight': '500'}),
                html.H2(f'{total_launches}', style={'color': colors['primary'], 'fontSize': '36px', 'fontWeight': 'bold', 'margin': '0'})
            ], style={'backgroundColor': colors['card_bg'], 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center', 'boxShadow': '0 2px 8px rgba(0, 0, 0, 0.1)', 'border': f'1px solid {colors["border"]}', 'flex': '1'}),
            
            html.Div([
                html.H3('✅ Successful', style={'color': colors['text'], 'fontSize': '16px', 'marginBottom': '10px', 'fontWeight': '500'}),
                html.H2(f'{int(successful_launches)}', style={'color': colors['success'], 'fontSize': '36px', 'fontWeight': 'bold', 'margin': '0'})
            ], style={'backgroundColor': colors['card_bg'], 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center', 'boxShadow': '0 2px 8px rgba(0, 0, 0, 0.1)', 'border': f'1px solid {colors["border"]}', 'flex': '1'}),
            
            html.Div([
                html.H3('🎯 Success Rate', style={'color': colors['text'], 'fontSize': '16px', 'marginBottom': '10px', 'fontWeight': '500'}),
                html.H2(f'{success_rate:.1f}%', style={'color': colors['warning'], 'fontSize': '36px', 'fontWeight': 'bold', 'margin': '0'})
            ], style={'backgroundColor': colors['card_bg'], 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center', 'boxShadow': '0 2px 8px rgba(0, 0, 0, 0.1)', 'border': f'1px solid {colors["border"]}', 'flex': '1'}),
            
            html.Div([
                html.H3('📦 Avg Payload', style={'color': colors['text'], 'fontSize': '16px', 'marginBottom': '10px', 'fontWeight': '500'}),
                html.H2(f'{avg_payload:,.0f} kg', style={'color': colors['secondary'], 'fontSize': '32px', 'fontWeight': 'bold', 'margin': '0'})
            ], style={'backgroundColor': colors['card_bg'], 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center', 'boxShadow': '0 2px 8px rgba(0, 0, 0, 0.1)', 'border': f'1px solid {colors["border"]}', 'flex': '1'}),
        ]
    )

# Callback for Pie Chart Insights
@app.callback(
    Output('pie-insights', 'children'),
    Input('site-dropdown', 'value')
)
def update_pie_insights(entered_site):
    if entered_site == 'ALL':
        filtered_df = spacex_df
        site_success = filtered_df.groupby('LaunchSite').agg({
            'Class': ['sum', 'count', 'mean']
        }).round(3)
        site_success.columns = ['Successful', 'Total', 'Rate']
        site_success = site_success.sort_values('Successful', ascending=False)
        
        insights = [
            html.H3('📊 Launch Site Insights', style={'color': colors['primary'], 'marginBottom': '20px'}),
            html.Div([
                html.H4('🏆 Top Performing Sites:', style={'color': colors['text'], 'fontSize': '18px', 'marginTop': '15px'}),
                html.P(f"• {site_success.index[0]} leads with {int(site_success.iloc[0]['Successful'])} successful launches ({site_success.iloc[0]['Rate']*100:.1f}% success rate)", 
                       style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
                html.P(f"• {site_success.index[1]} has {int(site_success.iloc[1]['Successful'])} successful launches ({site_success.iloc[1]['Rate']*100:.1f}% success rate)", 
                       style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
                
                html.H4('📈 Total Statistics:', style={'color': colors['text'], 'fontSize': '18px', 'marginTop': '20px'}),
                html.P(f"• Total Launches: {len(filtered_df)}", 
                       style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
                html.P(f"• Successful: {int(filtered_df['Class'].sum())} ({filtered_df['Class'].mean()*100:.1f}%)", 
                       style={'color': colors['success'], 'fontSize': '14px', 'marginLeft': '10px', 'fontWeight': 'bold'}),
                html.P(f"• Failed: {len(filtered_df) - int(filtered_df['Class'].sum())} ({(1-filtered_df['Class'].mean())*100:.1f}%)", 
                       style={'color': colors['danger'], 'fontSize': '14px', 'marginLeft': '10px'}),
                
                html.H4('🎯 Key Findings:', style={'color': colors['text'], 'fontSize': '18px', 'marginTop': '20px'}),
                html.P(f"• Most active site: {site_success.index[0]} ({int(site_success.iloc[0]['Total'])} launches)", 
                       style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
                html.P(f"• Highest success rate: {site_success.sort_values('Rate', ascending=False).index[0]} ({site_success.sort_values('Rate', ascending=False).iloc[0]['Rate']*100:.1f}%)", 
                       style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
            ])
        ]
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == entered_site]
        total = len(filtered_df)
        successful = filtered_df['Class'].sum()
        failed = total - successful
        success_rate = (successful / total * 100) if total > 0 else 0
        
        insights = [
            html.H3(f'📊 {entered_site} Insights', style={'color': colors['primary'], 'marginBottom': '20px'}),
            html.Div([
                html.H4('📈 Performance Metrics:', style={'color': colors['text'], 'fontSize': '18px', 'marginTop': '15px'}),
                html.P(f"• Total Launches: {total}", 
                       style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
                html.P(f"• Successful: {int(successful)} ({success_rate:.1f}%)", 
                       style={'color': colors['success'], 'fontSize': '14px', 'marginLeft': '10px', 'fontWeight': 'bold'}),
                html.P(f"• Failed: {int(failed)} ({100-success_rate:.1f}%)", 
                       style={'color': colors['danger'], 'fontSize': '14px', 'marginLeft': '10px'}),
                
                html.H4('🎯 Analysis:', style={'color': colors['text'], 'fontSize': '18px', 'marginTop': '20px'}),
                html.P(f"• This site shows a {success_rate:.1f}% success rate", 
                       style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
                html.P(f"• Average payload: {filtered_df['PayloadMass'].mean():,.0f} kg", 
                       style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
            ])
        ]
    
    return html.Div(insights)

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(
            spacex_df,
            names='LaunchSite',
            values='Class',
            title='Total Success Launches By Site',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == entered_site]
        success_counts = filtered_df['Class'].value_counts()
        
        fig = px.pie(
            values=success_counts.values,
            names=['Failed' if i == 0 else 'Successful' for i in success_counts.index],
            title=f'Success vs Failed Launches for {entered_site}',
            color_discrete_map={'Successful': colors['success'], 'Failed': colors['danger']}
        )
    
    fig.update_layout(
        title_x=0.5,
        title_font_size=20,
        plot_bgcolor=colors['card_bg'],
        paper_bgcolor=colors['card_bg'],
        font_color=colors['text'],
        legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="right", x=1.15)
    )
    
    return fig

# Callback for Scatter Plot Insights
@app.callback(
    Output('scatter-insights', 'children'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter_insights(entered_site, payload_range):
    min_payload, max_payload = payload_range
    
    if entered_site == 'ALL':
        filtered_df = spacex_df
        site_text = "all sites"
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == entered_site]
        site_text = entered_site
    
    filtered_df = filtered_df[
        (filtered_df['PayloadMass'] >= min_payload) &
        (filtered_df['PayloadMass'] <= max_payload)
    ]
    
    total = len(filtered_df)
    if total == 0:
        return html.Div([
            html.H3('📊 Payload Analysis', style={'color': colors['primary'], 'marginBottom': '20px'}),
            html.P('No data available for selected filters', style={'color': colors['text']})
        ])
    
    successful = filtered_df['Class'].sum()
    success_rate = (successful / total * 100)
    avg_payload = filtered_df['PayloadMass'].mean()
    
    low_payload = filtered_df[filtered_df['PayloadMass'] < 5000]
    high_payload = filtered_df[filtered_df['PayloadMass'] >= 5000]
    
    low_success_rate = (low_payload['Class'].mean() * 100) if len(low_payload) > 0 else 0
    high_success_rate = (high_payload['Class'].mean() * 100) if len(high_payload) > 0 else 0
    
    insights = [
        html.H3('📊 Payload Analysis', style={'color': colors['primary'], 'marginBottom': '20px', 'fontSize': '20px'}),
        html.Div([
            html.H4('📈 Range Overview:', style={'color': colors['text'], 'fontSize': '16px', 'marginTop': '15px'}),
            html.P(f"• Payload Range: {min_payload:,.0f} - {max_payload:,.0f} kg", 
                   style={'color': colors['text'], 'fontSize': '13px', 'marginLeft': '10px'}),
            html.P(f"• Total Launches: {total}", 
                   style={'color': colors['text'], 'fontSize': '13px', 'marginLeft': '10px'}),
            html.P(f"• Success Rate: {success_rate:.1f}%", 
                   style={'color': colors['success'], 'fontSize': '13px', 'marginLeft': '10px', 'fontWeight': 'bold'}),
            
            html.H4('🎯 Correlation:', style={'color': colors['text'], 'fontSize': '16px', 'marginTop': '20px'}),
            html.P(f"• Low Payload (<5000kg): {low_success_rate:.1f}% success ({len(low_payload)} launches)", 
                   style={'color': colors['text'], 'fontSize': '13px', 'marginLeft': '10px'}),
            html.P(f"• High Payload (≥5000kg): {high_success_rate:.1f}% success ({len(high_payload)} launches)", 
                   style={'color': colors['text'], 'fontSize': '13px', 'marginLeft': '10px'}),
            
            html.H4('💡 Insight:', style={'color': colors['text'], 'fontSize': '16px', 'marginTop': '20px'}),
            html.P(f"• Average payload: {avg_payload:,.0f} kg", 
                   style={'color': colors['text'], 'fontSize': '13px', 'marginLeft': '10px'}),
            html.P(f"• {'Higher' if high_success_rate > low_success_rate else 'Lower'} payloads show better success rates", 
                   style={'color': colors['primary'], 'fontSize': '13px', 'marginLeft': '10px', 'fontWeight': 'bold'}),
        ])
    ]
    
    return html.Div(insights)

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def get_scatter_chart(entered_site, payload_range):
    min_payload, max_payload = payload_range
    
    if entered_site == 'ALL':
        filtered_df = spacex_df
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == entered_site]
    
    filtered_df = filtered_df[
        (filtered_df['PayloadMass'] >= min_payload) &
        (filtered_df['PayloadMass'] <= max_payload)
    ]
    
    fig = px.scatter(
        filtered_df,
        x='PayloadMass',
        y='Class',
        color='BoosterVersion',
        title=f'Payload vs Launch Success Correlation',
        labels={'PayloadMass': 'Payload Mass (kg)', 'Class': 'Launch Outcome'},
        color_discrete_sequence=px.colors.qualitative.Set2,
        hover_data=['LaunchSite', 'Date']
    )
    
    fig.update_layout(
        title_x=0.5,
        title_font_size=20,
        plot_bgcolor=colors['card_bg'],
        paper_bgcolor=colors['card_bg'],
        font_color=colors['text'],
        yaxis=dict(tickmode='array', tickvals=[0, 1], ticktext=['Failed', 'Successful']),
        legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5)
    )
    
    return fig

# Callback for Orbit Success Bar Chart
@app.callback(
    Output('orbit-success-bar-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def get_orbit_chart(entered_site):
    if entered_site == 'ALL':
        filtered_df = spacex_df
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == entered_site]
    
    orbit_success = filtered_df.groupby('Orbit').agg({
        'Class': ['mean', 'count']
    }).reset_index()
    orbit_success.columns = ['Orbit', 'SuccessRate', 'TotalLaunches']
    orbit_success['SuccessRate'] = orbit_success['SuccessRate'] * 100
    orbit_success = orbit_success.sort_values('SuccessRate', ascending=False)
    
    fig = go.Figure(data=[
        go.Bar(
            x=orbit_success['Orbit'],
            y=orbit_success['SuccessRate'],
            text=[f"{rate:.1f}%<br>({count} launches)" for rate, count in zip(orbit_success['SuccessRate'], orbit_success['TotalLaunches'])],
            textposition='auto',
            marker_color=colors['primary'],
            hovertemplate='<b>%{x}</b><br>Success Rate: %{y:.1f}%<extra></extra>'
        )
    ])
    
    fig.update_layout(
        title='Success Rate by Orbit Type',
        title_x=0.5,
        title_font_size=20,
        xaxis_title='Orbit Type',
        yaxis_title='Success Rate (%)',
        plot_bgcolor=colors['card_bg'],
        paper_bgcolor=colors['card_bg'],
        font_color=colors['text'],
        yaxis=dict(range=[0, 100])
    )
    
    return fig

# Callback for Orbit Insights
@app.callback(
    Output('orbit-insights', 'children'),
    Input('site-dropdown', 'value')
)
def update_orbit_insights(entered_site):
    if entered_site == 'ALL':
        filtered_df = spacex_df
        site_text = "all sites"
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == entered_site]
        site_text = entered_site
    
    orbit_stats = filtered_df.groupby('Orbit').agg({
        'Class': ['mean', 'count', 'sum']
    }).reset_index()
    orbit_stats.columns = ['Orbit', 'SuccessRate', 'Total', 'Successful']
    orbit_stats['SuccessRate'] = orbit_stats['SuccessRate'] * 100
    orbit_stats = orbit_stats.sort_values('SuccessRate', ascending=False)
    
    best_orbit = orbit_stats.iloc[0]
    worst_orbit = orbit_stats.iloc[-1]
    most_used = orbit_stats.sort_values('Total', ascending=False).iloc[0]
    
    insights = [
        html.H3('🛰️ Orbit Analysis', style={'color': colors['primary'], 'marginBottom': '20px'}),
        html.Div([
            html.H4('🏆 Best Performing:', style={'color': colors['text'], 'fontSize': '18px', 'marginTop': '15px'}),
            html.P(f"• {best_orbit['Orbit']} orbit: {best_orbit['SuccessRate']:.1f}% success rate", 
                   style={'color': colors['success'], 'fontSize': '14px', 'marginLeft': '10px', 'fontWeight': 'bold'}),
            html.P(f"  ({int(best_orbit['Successful'])} of {int(best_orbit['Total'])} launches)", 
                   style={'color': colors['text'], 'fontSize': '13px', 'marginLeft': '20px'}),
            
            html.H4('📊 Most Common:', style={'color': colors['text'], 'fontSize': '18px', 'marginTop': '20px'}),
            html.P(f"• {most_used['Orbit']} orbit: {int(most_used['Total'])} total launches", 
                   style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
            html.P(f"  ({most_used['SuccessRate']:.1f}% success rate)", 
                   style={'color': colors['text'], 'fontSize': '13px', 'marginLeft': '20px'}),
            
            html.H4('💡 Key Finding:', style={'color': colors['text'], 'fontSize': '18px', 'marginTop': '20px'}),
            html.P(f"• {len(orbit_stats)} different orbit types used at {site_text}", 
                   style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
            html.P(f"• Success rates vary from {worst_orbit['SuccessRate']:.1f}% to {best_orbit['SuccessRate']:.1f}%", 
                   style={'color': colors['primary'], 'fontSize': '14px', 'marginLeft': '10px', 'fontWeight': 'bold'}),
        ])
    ]
    
    return html.Div(insights)

# Callback for Timeline Chart
@app.callback(
    Output('timeline-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def get_timeline_chart(entered_site):
    if entered_site == 'ALL':
        filtered_df = spacex_df.copy()
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == entered_site].copy()
    
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])
    filtered_df = filtered_df.sort_values('Date')
    
    filtered_df['CumulativeSuccess'] = filtered_df['Class'].cumsum()
    filtered_df['CumulativeTotal'] = range(1, len(filtered_df) + 1)
    filtered_df['SuccessRate'] = (filtered_df['CumulativeSuccess'] / filtered_df['CumulativeTotal']) * 100
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=filtered_df['Date'],
        y=filtered_df['SuccessRate'],
        mode='lines+markers',
        name='Success Rate',
        line=dict(color=colors['primary'], width=3),
        marker=dict(size=6),
        hovertemplate='<b>%{x|%Y-%m-%d}</b><br>Success Rate: %{y:.1f}%<extra></extra>'
    ))
    
    fig.update_layout(
        title='Cumulative Success Rate Over Time',
        title_x=0.5,
        title_font_size=20,
        xaxis_title='Launch Date',
        yaxis_title='Cumulative Success Rate (%)',
        plot_bgcolor=colors['card_bg'],
        paper_bgcolor=colors['card_bg'],
        font_color=colors['text'],
        yaxis=dict(range=[0, 100]),
        hovermode='x unified'
    )
    
    return fig

# Callback for Timeline Insights
@app.callback(
    Output('timeline-insights', 'children'),
    Input('site-dropdown', 'value')
)
def update_timeline_insights(entered_site):
    if entered_site == 'ALL':
        filtered_df = spacex_df.copy()
        site_text = "all sites"
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == entered_site].copy()
        site_text = entered_site
    
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])
    filtered_df = filtered_df.sort_values('Date')
    
    first_launch = filtered_df['Date'].min()
    last_launch = filtered_df['Date'].max()
    days_span = (last_launch - first_launch).days
    
    mid_date = first_launch + pd.Timedelta(days=days_span/2)
    early_period = filtered_df[filtered_df['Date'] < mid_date]
    late_period = filtered_df[filtered_df['Date'] >= mid_date]
    
    early_success = (early_period['Class'].mean() * 100) if len(early_period) > 0 else 0
    late_success = (late_period['Class'].mean() * 100) if len(late_period) > 0 else 0
    
    final_success_rate = (filtered_df['Class'].sum() / len(filtered_df)) * 100
    
    insights = html.Div([
        html.Div([
            html.H3('📅 Timeline Analysis', style={'color': colors['primary'], 'marginBottom': '20px'}),
        ], style={'width': '100%'}),
        
        html.Div([
            html.Div([
                html.H4('📆 Period Overview:', style={'color': colors['text'], 'fontSize': '18px', 'marginTop': '15px'}),
                html.P(f"• First Launch: {first_launch.strftime('%Y-%m-%d')}", 
                       style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
                html.P(f"• Latest Launch: {last_launch.strftime('%Y-%m-%d')}", 
                       style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
                html.P(f"• Time Span: {days_span} days ({days_span/365:.1f} years)", 
                       style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
            ], style={'width': '33%', 'display': 'inline-block', 'verticalAlign': 'top'}),
            
            html.Div([
                html.H4('📈 Performance Trend:', style={'color': colors['text'], 'fontSize': '18px', 'marginTop': '15px'}),
                html.P(f"• Early Period: {early_success:.1f}% success ({len(early_period)} launches)", 
                       style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
                html.P(f"• Recent Period: {late_success:.1f}% success ({len(late_period)} launches)", 
                       style={'color': colors['success'] if late_success > early_success else colors['danger'], 
                              'fontSize': '14px', 'marginLeft': '10px', 'fontWeight': 'bold'}),
                html.P(f"• Improvement: {late_success - early_success:+.1f}%", 
                       style={'color': colors['success'] if late_success > early_success else colors['danger'], 
                              'fontSize': '14px', 'marginLeft': '10px'}),
            ], style={'width': '33%', 'display': 'inline-block', 'verticalAlign': 'top'}),
            
            html.Div([
                html.H4('💡 Key Insights:', style={'color': colors['text'], 'fontSize': '18px', 'marginTop': '15px'}),
                html.P(f"• Overall Success Rate: {final_success_rate:.1f}%", 
                       style={'color': colors['primary'], 'fontSize': '14px', 'marginLeft': '10px', 'fontWeight': 'bold'}),
                html.P(f"• Performance {'improved' if late_success > early_success else 'declined'} over time", 
                       style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
                html.P(f"• Technology and procedures have {'evolved positively' if late_success > early_success else 'faced challenges'}", 
                       style={'color': colors['text'], 'fontSize': '14px', 'marginLeft': '10px'}),
            ], style={'width': '33%', 'display': 'inline-block', 'verticalAlign': 'top'}),
        ], style={'width': '100%', 'display': 'block'})
    ])
    
    return insights

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
