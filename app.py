from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# ===============================
# LOAD DATA
# ===============================

df = pd.read_csv("nvidia_stock.csv")

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna()
df = df.sort_values("Date")
