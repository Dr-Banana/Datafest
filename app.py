import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt

st.title("Zhang_10419_lab3_code")
# Set Up
data = pd.read_csv("https://docs.google.com/spreadsheets/d/1QBWVaIY20qQ5rMYZtNuu6-zN499UFV-drzJgYjPPYR0/edit#gid=0")

# change ".." to number
data
