import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt

st.title("Zhang_10419_lab3_code")
# Set Up
data = pd.read_csv("https://raw.githubusercontent.com/Dr-Banana/Datafest/main/S5_scores_cleaned.csv")

df_1 = df_1.drop(columns=['player_id'])
df_1
chart_data = pd.DataFrame()
