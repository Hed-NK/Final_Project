# Importing Libraries
import pandas as pd
import streamlit as st
import numpy as np
import altair as alt

# Page Title
st.set_page_config(page_title='COVID-19 Exploratory Data Analysis', page_icon='🦠', layout='wide', initial_sidebar_state="expanded")
st.title('🦠 COVID-19 Explatory Data Analysis')

# App Description
with st.expander('About this app'):
    st.markdown('What can this app do?')
    st.info('This application presents twelve types of interactive visualizations. Bar Plot of Deaths per Country color coded by Continent. Scatter Plot of Recovered per cases color coded by Country. Pie Chart of Active cases distribution color coded by Continent. Histogram of Critical cases per overall cases color coded by Country. Heatmap of Active cases per overall cases color coded by Continent. Bubble Chart of cases per Recovered by continent and Population Size. 3D Scatter Plot of COVID-19 Cases, Deaths, and Recovered color coded by continent. Pair Plot of COVID-19 Data color coded by continent. Cluster World Map of COVID-19 Data by case numbers. Facet Grid of cases per Deaths by Continent. Joint Plot of Critical cases per Tests by Continent. Additionally, the app includes user-friendly dropdown menus to customize the data visualizations dynamically.')
    st.markdown('How to use this app?')
    st.info('Users can select specific countries or continents using dropdown menus. Adjusting these filters dynamically updates the visualizations.')

# Project Description
with st.expander('Project Objectives'):
     st.markdown('What are the objectives of this project?')
     st.info('This project provides a comprehensive analysis and comparison of COVID-19 statistics, including the number of cases, deaths, recoveries, and critical conditions, across various countries and continents. By visualizing and interpreting these metrics, the project aims to offer valuable insights into the global impact of the pandemic.')

# Load Data
df = pd.read_csv('infectious_diseases_data.csv')
df = df.dropna(subset=['continent'])

# Country Selection - Dropdown Menu
Country_list = df.country.unique()
Country_selection = st.multiselect('Select Countries', Country_list, default=('Afghanistan', 'Dominican Republic', 'Kenya', 'French Polynesia', 'Czechia'))

# Continent Selection - Dropdown Menu
Continent_list = df.continent.unique()
Continent_selection = st.multiselect('Select Continents', Continent_list, default=Continent_list)

# Data Overview 
st.write('Data Overview')
st.write(df.describe())

# Filtered Data
filtered_df = df[ (df['country'].isin(Country_selection)) 
& (df['continent'].isin(Continent_selection))]
st.write('Filtered Data', filtered_df)

# Bar Chart
chart = alt.Chart(filtered_df).mark_bar().encode(
    x='country',
    y='deaths',
    color='continent',
    tooltip=['country', 'cases', 'deaths', 'recovered', 'critical', 'active', 'casesPerOneMillion', 'deathsPerOneMillion', 'tests', 'testsPerOneMillion', 'population', 'oneCasePerPeople', 'oneDeathPerPeople', 'oneTestPerPeople', 'activePerOneMillion', 'recoveredPerOneMillion', 'criticalPerOneMillion']
).interactive().properties( title='Bar Chart of Deaths per Country by Continent' )
st.altair_chart(chart, use_container_width=True)

# Scatter Plot 
scatter_plot = alt.Chart(filtered_df).mark_circle(size=60).encode( 
    x='cases', 
    y='recovered', 
    color='country', 
    tooltip=['country', 'cases', 'deaths', 'recovered', 'critical', 'active', 'casesPerOneMillion', 'deathsPerOneMillion', 'tests', 'testsPerOneMillion', 'population', 'oneCasePerPeople', 'oneDeathPerPeople', 'oneTestPerPeople', 'activePerOneMillion', 'recoveredPerOneMillion', 'criticalPerOneMillion']
).interactive().properties( title='Scatter Plot of Recovered per Cases by Country' )
st.altair_chart(scatter_plot, use_container_width=True)

# Pie Chart for active cases distribution by continent  
pie_chart = alt.Chart(filtered_df).mark_arc().encode( 
    theta=alt.Theta(field='active', type='quantitative'), 
    color=alt.Color(field='continent', type='nominal'), 
    tooltip=['continent', 'country', 'cases', 'deaths', 'recovered', 'critical', 'active', 'casesPerOneMillion', 'deathsPerOneMillion', 'tests', 'testsPerOneMillion', 'population', 'oneCasePerPeople', 'oneDeathPerPeople', 'oneTestPerPeople', 'activePerOneMillion', 'recoveredPerOneMillion', 'criticalPerOneMillion']
 ).properties( width=400, height=400, title='Pie Chart of Active Cases distribution by Continent') 
st.altair_chart(pie_chart, use_container_width=True)

# Box Plot
box_plot = alt.Chart(filtered_df).mark_boxplot().encode(
    x='tests',
    y='deaths',
    color='country',
    tooltip=['country', 'cases', 'deaths', 'recovered', 'critical', 'active', 'casesPerOneMillion', 'deathsPerOneMillion', 'tests', 'testsPerOneMillion', 'population', 'oneCasePerPeople', 'oneDeathPerPeople', 'oneTestPerPeople']
).properties(
    title='Box Plot of Deaths per Tests by Country'
)
st.altair_chart(box_plot, use_container_width=True)

# Histogram 
histogram = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('cases', bin=True),
    y='critical',
    color='country',
    tooltip=['cases', 'count()','country', 'deaths', 'recovered', 'critical', 'active', 'casesPerOneMillion', 'deathsPerOneMillion', 'tests', 'testsPerOneMillion', 'population', 'oneCasePerPeople', 'oneDeathPerPeople', 'oneTestPerPeople']
).properties(
    title='Histogram of Critical Cases per Overall Cases'
)
st.altair_chart(histogram, use_container_width=True)

# Heatmap 
heatmap = alt.Chart(filtered_df).mark_rect().encode(
    x='cases',
    y='active',
    color='continent',
    tooltip=['cases', 'deaths', 'count()', 'country', 'recovered', 'critical', 'active', 'casesPerOneMillion', 'deathsPerOneMillion', 'tests', 'testsPerOneMillion', 'population', 'oneCasePerPeople', 'oneDeathPerPeople', 'oneTestPerPeople']
).properties(
    title='Heatmap of Active Cases per Overall Cases'
)
st.altair_chart(heatmap, use_container_width=True)

# Bubble Chart 
bubble_chart = alt.Chart(filtered_df).mark_circle().encode(
    x='cases',
    y='recovered',
    size='population',
    color='continent',
    tooltip=['country', 'cases', 'deaths', 'population', 'count()', 'recovered', 'critical', 'active', 'casesPerOneMillion', 'deathsPerOneMillion', 'tests', 'testsPerOneMillion', 'population', 'oneCasePerPeople', 'oneDeathPerPeople', 'oneTestPerPeople']
).properties(
    title='Bubble Chart of Cases vs. Recovered by continent and Population Size'
)
st.altair_chart(bubble_chart, use_container_width=True)

# 3D Scatter Plot 
import plotly.express as px
fig = px.scatter_3d(filtered_df, x='cases', y='deaths', z='recovered', color='continent', hover_data=['country', 'cases', 'deaths', 'population', 'recovered', 'critical', 'active', 'casesPerOneMillion', 'deathsPerOneMillion', 'tests', 'testsPerOneMillion', 'population', 'oneCasePerPeople', 'oneDeathPerPeople', 'oneTestPerPeople']) 
fig.update_layout(title='3D Scatter Plot of COVID-19 Cases, Deaths, and Recovered by continent') 
# Display Plot in Streamlit 
st.plotly_chart(fig)

# Pair Plot 
fig = px.scatter_matrix(filtered_df, dimensions=['cases', 'deaths', 'recovered', 'critical', 'active', 'tests', 'population'], color='continent', 
                        title='Pair Plot of COVID-19 Data') 
# Display Plot in Streamlit 
st.plotly_chart(fig)

# Cluster Map 
fig = px.scatter_geo(filtered_df, locations='country', locationmode='country names', color='continent', hover_name='country', size='cases', projection='natural earth', title='Cluster Map of COVID-19 Data by Case numbers') 
fig.update_layout(mapbox_style="carto-positron", title='Cluster Map of COVID-19 Data by Case numbers', height=600) 
# Display Plot in Streamlit 
st.plotly_chart(fig)

import seaborn as sns
import matplotlib.pyplot as plt

# Facet Grid 
fig_facet = px.scatter(filtered_df, x='cases', y='deaths', color='continent', facet_col='continent', title='Facet Grid of Cases per Deaths by Continent')
st.plotly_chart(fig_facet)

# Joint Plot (scatter plot with marginal histograms)
fig_joint = px.scatter(filtered_df, x='tests', y='critical', color='continent', marginal_x='histogram', marginal_y='histogram', title='Joint Plot of Critical Cases per Tests by Continent')
st.plotly_chart(fig_joint)
