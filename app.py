import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt

st.title("Zhang_10419_lab3_code")
# Set Up
data = pd.read_csv("https://raw.githubusercontent.com/Dr-Banana/Datafest/main/S5_scores_cleaned.csv")

df_1 = data.drop(columns=['player_id'])
wk = [0,3,6,12,24]

chart_data = pd.DataFrame()
for n in range(5):
  count = 0
  mean_list = []
  std_list = []
  df_tmp = df_1[df_1["weeks"]== wk[n]]
  mn = sum(mean_list)/len(mean_list)
  chart_data = {wk[n]:mn}
  chart_data = pd.DataFrame(data=chart_data)
chart_data
