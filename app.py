from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# โหลดไฟล์จากโฟลเดอร์เดียวกัน
df = pd.read_csv("superstore.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])

app = Dash(__name__)
app.title = "Sales Dashboard"

app.layout = html.Div([
    html.H1("📊 Global Sales Dashboard", style={'textAlign': 'center'}),

    html.Div([
        dcc.Dropdown(
            id='region-dropdown',
            options=[{'label': r, 'value': r} for r in df['Region'].unique()],
            value=df['Region'].unique()[0],
            placeholder="Select Region"
        ),
         dcc.Dropdown(
            id='category-dropdown',
            options=[{'label': c, 'value': c} for c in df['Category'].unique()],
            value=df['Category'].unique()[0],
            placeholder="Select Category"
        ),
