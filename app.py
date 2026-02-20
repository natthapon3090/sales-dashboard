from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# โหลด Dataset
df = pd.read_csv("nvidia_stock.csv")
df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)
app.title = "NVIDIA Dashboard"

app.layout = html.Div([

    html.H1("📈 NVIDIA Stock Dashboard", style={"textAlign": "center"}),

    html.Div([
        dcc.DatePickerRange(
            id="date-picker",
            start_date=df["Date"].min(),
            end_date=df["Date"].max()
        ),

        dcc.Dropdown(
            id="ma-dropdown",
            options=[
                {"label": "MA 3", "value": 3},
                {"label": "MA 5", "value": 5}
            ],
            value=3
        )
    ], style={"width": "50%", "margin": "auto"}),

    dcc.Graph(id="price-chart"),
    dcc.Graph(id="volume-chart"),
    dcc.Graph(id="ma-chart")

])
