import numpy as np
import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import scipy
import ast
import plotly.subplots as sp
import plotly.graph_objects as go

df = pd.read_csv('DATA.csv')
df = preprocessor.preprocess(df)
pop_df = pd.read_csv('population.csv')
pop_df = preprocessor.preprocess1(pop_df)



user_menu = st.sidebar.radio(
    'Select an Option',
    ('NET VS GROSS GDP', 'INDUSTRY WISE COMPARISON', 'POPULATION COMPARISON')
)


if user_menu == 'NET VS GROSS GDP':
    state = helper.state_list(df)
    type = helper.type()

    selected_state = st.sidebar.selectbox('SELECT STATE', state)
    selected_type = st.sidebar.selectbox('SELECT TYPE', type)
     
    overtime = helper.get_dataframe(df,selected_state, selected_type)
    fig = px.line(overtime, x='YEAR', y=selected_type)
    st.plotly_chart(fig)

    selected_state_contrib = overtime[selected_type].sum()
    total_contrib = df[df['STATE'] == selected_state][selected_type].sum()
    total_contrib_across_states = df[selected_type].sum()
    
    labels = [selected_state ,'Other States']
    values = [selected_state_contrib, total_contrib_across_states - selected_state_contrib]
    
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    st.plotly_chart(fig)

    


if user_menu == 'INDUSTRY WISE COMPARISON':
    state = helper.state_list(df)
    type = helper.industry_type()
    year = helper.year(df)
    selected_state = st.sidebar.selectbox('SELECT STATE', state)
    selected_columns = st.multiselect("Select to check",type)
    industry = helper.get_state(df,selected_state)

    # LINE CHART
    if selected_columns:                                     
        chart_data = industry[['YEAR'] + selected_columns]
        fig = px.line(chart_data, x='YEAR', y=selected_columns)
        st.plotly_chart(fig)

    # PIE chart
    if selected_columns:
        chart_data = industry[industry['YEAR'] == max(industry['YEAR'])]
        chart_data = chart_data[selected_columns].sum().reset_index()
        chart_data.columns = ['Columns', 'Value']
        fig = px.pie(chart_data, values='Value', names='Columns', title='Pie Chart for the Latest Year')
        st.plotly_chart(fig)

    #BAR CHART
    chart_data = industry[['YEAR'] + selected_columns]
    growth_rates = chart_data[selected_columns].pct_change().mean() * 100
    growth_rates = growth_rates.reset_index()
    growth_rates.columns = ['Columns', 'Growth Rate']
    growth_rates['Growth Rate'] = growth_rates['Growth Rate'].astype(int)
    fig = px.bar(growth_rates, x='Columns', y='Growth Rate', title='Average Growth Rate Over the Years',color='Growth Rate', color_continuous_scale=px.colors.sequential.Plasma)
    st.plotly_chart(fig)


if user_menu == 'POPULATION COMPARISON':
    state = helper.pop_state(pop_df)
    year = helper.pop_year(pop_df)
    type = helper.pop_type()
    selected_state = st.sidebar.selectbox('Select State', state)
    selected_columns = st.selectbox("Select to check",type)
    population = helper.get_pop(pop_df,selected_state)
    
    # if selected_state:
    #     fig = px.line(population, x='year', y=selected_columns, color_discrete_sequence=['brown'])
    #     st.plotly_chart(fig)

    fig = px.line(population, x='year', y=selected_columns, 
              title='Population trend over years', 
              labels={'year': 'Year', 'selected_columns': 'Population'}, 
              color_discrete_sequence=['red'])

    fig.update_layout(annotations=[dict(x=year, y=value, text=f'increased by', 
    showarrow=True , arrowhead=1, ax=-50, ay=-50) 
    for year, value in zip(population.year, population[selected_columns])])
    st.plotly_chart(fig)



    


