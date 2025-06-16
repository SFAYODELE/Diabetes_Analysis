import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as pt
import numpy as np
import plotly.express as px


st.title("DIABETES ANALYSIS")


#import my csv file
df = pd.read_csv("diabetes_pyton.csv")


st.markdown("## Overview")

st.markdown("### First 5 observations")
st.write(df.head())

st.markdown("### Last 5 observations")
st.write(df.tail())

st.markdown("### Description of numeric data types")
st.write(df.describe())

st.markdown("## Data shape")
st.write(df.shape)

st.markdown("## Univariate Analysis")

st.markdown("### Blood Pressure")

st.write(df["BloodPressure"].describe())


bp = px.bar(df['BloodPressure'], y ='BloodPressure',title="Distribution of Blood Pressure")

st.plotly_chart(bp, use_container_width=True)