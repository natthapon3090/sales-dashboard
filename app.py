from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# โหลด CSV จาก Kaggle
df = pd.read_csv("nvidia_stock.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna()

app = Dash(__name__)
app.title = "NVIDIA Dashboard"

app.layout = html.Div([
