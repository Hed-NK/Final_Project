# Importing Libraries
import pandas as pd
import streamlit as st
import numpy as np
import altair as alt

# Page Title
st.set_page_config(page_title='Infectious Diseases Exploratory Data Analysis', page_icon='🦠', layout='wide', initial_sidebar_state="expanded")
st.title('🦠 Infectious Diseases Explatory Data Analysis')

# App Description
with st.expander('About this app'):
    st.markdown('What can this app do?')
    st.info('This application presents three types of interactive visualizations. Bar Plot: Illustrates COVID-19 cases across different countries, color-coded by continent for easy comparison. Scatter Plot: Displays the relationship between COVID-19 deaths and cases, also color-coded by continent for clarity. Pie Chart: Provides a proportional view of COVID-19 cases, with segments color-coded by continent. Additionally, the app includes user-friendly sidebar filters, featuring sliders and dropdown menus to customize the data visualizations dynamically.')
    st.markdown('How to use this app?')
    st.info('The application includes intuitive sidebar filters, featuring sliders to adjust the number of COVID-19 cases, deaths, recoveries, and critical patients. Users can also select specific countries or continents using dropdown menus. Adjusting these filters dynamically updates the visualizations. Bar Plot: Clicking on any bar reveals the country name along with the corresponding number of COVID-19 cases, deaths, recoveries, and critical patients. Scatter Plot: Interacting with any scatter point displays detailed information, including the country name and the number of COVID-19 cases, deaths, recoveries, and critical patients. Pie Chart: Hovering over any segment of the pie chart shows the continent, country name, and the number of COVID-19 cases.')

# Project Description
with st.expander('Project Objectives'):
     st.markdown('What are the objectives of this project?')
     st.info('This project provides a comprehensive analysis and comparison of COVID-19 statistics, including the number of cases, deaths, recoveries, and critical conditions, across various countries and continents. By visualizing and interpreting these metrics, the project aims to offer valuable insights into the global impact of the pandemic.')

# Load Data
df = pd.read_csv('infectious_diseases_data.csv')

# Country Selection - Dropdown Menu
Country_list = df.country.unique()
Country_selection = st.multiselect('Select Countries', Country_list, ['Afghanistan', 'Albania' ,'Algeria' ,'Andorra', 'Angola', 'Anguilla',
 'Antigua and Barbuda' ,'Argentina' ,'Armenia' ,'Aruba' ,'Australia', 'Austria',
 'Azerbaijan', 'Bahamas' ,'Bahrain', 'Bangladesh', 'Barbados' ,'Belarus',
 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia',
 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria',
 'Burkina Faso', 'Burundi' ,'Cabo Verde', 'Cambodia' ,'Cameroon', 'Canada',
 'Caribbean Netherlands' ,'Cayman Islands' ,'Central African Republic',
 'Chad', 'Channel Islands' ,'Chile' ,'China', 'Colombia', 'Comoros', 'Congo',
 'Cook Islands', 'Costa Rica' ,'Croatia' ,'Cuba', 'Curaçao', 'Cyprus', 'Czechia',
 "Côte d'Ivoire" ,'DRC', 'Denmark', 'Diamond Princess', 'Djibouti', 'Dominica',
 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
 'Eritrea', 'Estonia', 'Ethiopia' ,'Falkland Islands (Malvinas)',
 'Faroe Islands' ,'Fiji', 'Finland' ,'France' ,'French Guiana',
 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana',
 'Gibraltar', 'Greece' ,'Greenland', 'Grenada', 'Guadeloupe', 'Guatemala',
 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See (Vatican City State)',
 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran',
 'Iraq', 'Ireland' ,'Isle of Man' ,'Israel', 'Italy', 'Jamaica', 'Japan',
 'Jordan' ,'Kazakhstan', 'Kenya', 'Kiribati' ,'Kuwait', 'Kyrgyzstan',
 "Lao People's Democratic Republic", 'Latvia' ,'Lebanon', 'Lesotho', 'Liberia',
 'Libyan Arab Jamahiriya' ,'Liechtenstein', 'Lithuania' ,'Luxembourg',
 'MS Zaandam', 'Macao' ,'Macedonia' ,'Madagascar', 'Malawi', 'Malaysia',
 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique' ,'Mauritania',
 'Mauritius', 'Mayotte', 'Mexico' ,'Micronesia', 'Moldova' ,'Monaco' ,'Mongolia',
 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique' ,'Myanmar', 'N. Korea',
 'Namibia', 'Nauru' ,'Nepal' ,'Netherlands' ,'New Caledonia' ,'New Zealand',
 'Nicaragua' ,'Niger', 'Nigeria', 'Niue', 'Norway', 'Oman', 'Pakistan' ,'Palau',
 'Palestine', 'Panama' ,'Papua New Guinea' ,'Paraguay' ,'Peru', 'Philippines',
 'Poland', 'Portugal' ,'Qatar', 'Romania' ,'Russia', 'Rwanda', 'Réunion',
 'S. Korea', 'Saint Helena', 'Saint Kitts and Nevis' ,'Saint Lucia',
 'Saint Martin' ,'Saint Pierre Miquelon', 'Saint Vincent and the Grenadines',
 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal',
 'Serbia', 'Seychelles', 'Sierra Leone' ,'Singapore' ,'Sint Maarten',
 'Slovakia' ,'Slovenia', 'Solomon Islands', 'Somalia' ,'South Africa',
 'South Sudan', 'Spain', 'Sri Lanka', 'St. Barth', 'Sudan', 'Suriname',
 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic' ,'Taiwan',
 'Tajikistan' ,'Tanzania' ,'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga',
 'Trinidad and Tobago' ,'Tunisia' ,'Turkey', 'Turks and Caicos Islands',
 'Tuvalu', 'UAE', 'UK', 'USA' ,'Uganda', 'Ukraine', 'Uruguay', 'Uzbekistan',
 'Vanuatu', 'Venezuela' ,'Vietnam' ,'Wallis and Futuna', 'Western Sahara',
 'Yemen', 'Zambia', 'Zimbabwe'])

# Continent Selection - Dropdown Menu
Continent_list = df.continent.unique()
Continent_selection = st.multiselect('Select Continents', Continent_list, ['Asia', 'Europe', 'Africa' ,'North America', 'South America',
 'Australia-Oceania'])

# Sidebar Filters
st.sidebar.title('Filters')

# Cases - Slider
Cases_list = df['cases']
Cases_selection = st.sidebar.slider('Select Number of Cases', 9, 111820082, (9, 111820082))

# Deaths - Slider
Deaths_list = df['deaths']
Deaths_selection = st.sidebar.slider('Select Number of Deaths', 0, 1219487, (0, 1219487))

# Recovered - Slider
Recovered_list = df['recovered']
Recovered_selection = st.sidebar.slider('Select Number of Recovered', 0, 109814428, (0, 109814428))

# Critical - Slider
Critical_list = df['critical']
Critical_selection = st.sidebar.slider('Select Number of Critical Patients', 0, 940, (0, 940))

# Data Overview 
st.write('Data Overview')
st.write(df.describe())

# Filtered Data
filtered_df = df[ (df['country'].isin(Country_list)) 
& (df['continent'].isin(Continent_list)) 
& (df['cases'] <= Cases_list) 
& (df['deaths'] <= Deaths_list) 
& (df['recovered'] <= Recovered_list) 
& (df['critical'] <= Critical_list) ]
st.write('Filtered Data', filtered_df)

# Bar Chart
chart = alt.Chart(filtered_df).mark_bar().encode(
    x='country',
    y='cases',
    color='continent',
    tooltip=['country', 'cases', 'deaths', 'recovered', 'critical']
).interactive()
st.altair_chart(chart, use_container_width=True)

# Scatter Plot 
scatter_plot = alt.Chart(filtered_df).mark_circle(size=60).encode( 
    x='cases', 
    y='deaths', 
    color='continent', 
    tooltip=['country', 'cases', 'deaths', 'recovered', 'critical']
).interactive() 
st.altair_chart(scatter_plot, use_container_width=True)

# Pie Chart for cases distribution by continent 
pie_chart = alt.Chart(filtered_df).mark_arc().encode( 
    theta=alt.Theta(field='cases', type='quantitative'), 
    color=alt.Color(field='continent', type='nominal'), 
    tooltip=['continent', 'country', 'cases'] ).properties( width=400, height=400 ) 
st.altair_chart(pie_chart, use_container_width=True)

