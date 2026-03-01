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

# ===============================
# APP SETUP
# ===============================

app = Dash(__name__)

])

# ===============================
# CALLBACK
# ===============================

@app.callback(
    Output("price-chart", "figure"),
    Output("volume-chart", "figure"),
    Output("ma-chart", "figure"),
    Input("date-picker", "start_date"),
    Input("date-picker", "end_date"),
    Input("ma-dropdown", "value")
