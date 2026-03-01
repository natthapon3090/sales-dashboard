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
app.title = "NVIDIA Dashboard"

app.layout = html.Div([

    html.H1("NVIDIA Stock Dashboard", style={"textAlign": "center"}),

    html.Div([
        dcc.DatePickerRange(
            id="date-picker",
            start_date=df["Date"].min(),
            end_date=df["Date"].max()
        ),

        dcc.Dropdown(
            id="ma-dropdown",
            options=[
                {"label": "MA 20", "value": 20},
                {"label": "MA 50", "value": 50}
            ],
            value=20
        )
    ], style={"width": "60%", "margin": "auto"}),

    dcc.Graph(id="price-chart"),
    dcc.Graph(id="volume-chart"),
    dcc.Graph(id="ma-chart")

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
)
def update_dashboard(start_date, end_date, ma_value):

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    filtered_df = df[
        (df["Date"] >= start_date) &
        (df["Date"] <= end_date)
    ].copy()

    # กราฟ 1: ราคาปิด
    fig1 = px.line(filtered_df, x="Date", y="Close",
                   title="Closing Price")

    # กราฟ 2: Volume
    fig2 = px.bar(filtered_df, x="Date", y="Volume",
                  title="Trading Volume")

    # กราฟ 3: Moving Average
    filtered_df["MA"] = filtered_df["Close"].rolling(ma_value).mean()

    fig3 = px.line(filtered_df, x="Date", y=["Close", "MA"],
                   title="Moving Average")

    return fig1, fig2, fig3
