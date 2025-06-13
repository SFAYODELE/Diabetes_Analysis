import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as pt
import numpy as np


st.title("DIABETES ANALYSIS")
#import my csv file
df = pd.read_csv("diabetes_pyton.csv")
st.write(df.head())