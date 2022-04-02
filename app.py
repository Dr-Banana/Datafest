import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt

st.title("Zhang_10419_lab3_code")
# Set Up
data = pd.read_csv("https://raw.githubusercontent.com/Dr-Banana/Datafest/main/S5_scores_cleaned.csv")

chart_data =  data.drop(columns=['player_id'])
wk = [0,3,6,12,24]

chart_data
singleSelect = st.selectbox("week", wk)
filter_data = chart_data[chart_data['weeks'] == singleSelect]
tit2 = "Box plot for " + singleSelect 
upper = alt.Chart(filter_data).mark_rect().encode(
    y = alt.Y('emission:Q', bin=alt.Bin(maxbins=30)),
    x = 'year:O',
    color = alt.Color('emission:Q', scale=alt.Scale(scheme='greenblue')),
    tooltip=['country', 'year', 'emission']
).properties(width=550,height=200,
    title= tit1
)
lower = alt.Chart(filter_data).mark_boxplot(size=50,extent=0.5).encode(
    x='country',
    y=alt.Y('emission:Q',scale=alt.Scale(zero=False))
).properties(width=550,
    title= tit2
)

obj = alt.vconcat(upper, lower)
st.altair_chart(lower)
