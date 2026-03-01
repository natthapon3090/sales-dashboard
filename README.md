NVIDIA Stock Dashboard

โปรเจกต์นี้เป็น Web Dashboard สำหรับแสดงข้อมูลหุ้น NVIDIA โดยใช้ Dash และ Plotly ในการสร้างกราฟแบบ Interactive ผู้ใช้สามารถเลือกช่วงวันที่ และเลือกค่า Moving Average ได้

โครงสร้างโปรแกรม

โปรแกรมนี้ประกอบด้วยไฟล์หลัก:

app.py → โค้ดหลักของ Dashboard

nvidia_stock.csv → ข้อมูลหุ้น NVIDIA

requirements.txt → รายการ Library ที่ต้องใช้

การทำงานของโปรแกรม
1. โหลดข้อมูล (Load Data)

โปรแกรมจะอ่านข้อมูลหุ้นจากไฟล์ CSV

df = pd.read_csv("nvidia_stock.csv")

จากนั้นแปลง Date ให้เป็นชนิดวันที่

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

ลบข้อมูลที่ผิดพลาด

df = df.dropna()

เรียงข้อมูลตามวันที่

df = df.sort_values("Date")

ส่วนนี้ทำให้ข้อมูลพร้อมใช้งานก่อนนำไปสร้างกราฟ 

app

2. สร้าง Dashboard

โปรแกรมใช้ Dash ในการสร้าง Web Application

app = Dash(__name__)
app.title = "NVIDIA Dashboard"

กำหนด Layout ของหน้าเว็บ

ประกอบด้วย

หัวข้อ Dashboard

ตัวเลือกช่วงวันที่

ตัวเลือก Moving Average

กราฟ 3 แบบ

app.layout = html.Div([
ส่วนเลือกวันที่
dcc.DatePickerRange(
    id="date-picker",
    start_date=df["Date"].min(),
    end_date=df["Date"].max()
)

ใช้เลือกช่วงวันที่ของข้อมูล

ส่วนเลือก Moving Average
dcc.Dropdown(
    id="ma-dropdown",
    options=[
        {"label": "MA 20", "value": 20},
        {"label": "MA 50", "value": 50}
    ],
    value=20
)

ใช้เลือกค่า Moving Average

เช่น

MA 20

MA 50

ส่วนแสดงกราฟ
dcc.Graph(id="price-chart")
dcc.Graph(id="volume-chart")
dcc.Graph(id="ma-chart")

มีทั้งหมด 3 กราฟ:

ราคาปิด

Volume

Moving Average

3. Callback Function

Callback ใช้สำหรับอัปเดตกราฟเมื่อมีการเปลี่ยนค่า

@app.callback(

รับค่า Input จาก

วันที่เริ่มต้น

วันที่สิ้นสุด

Moving Average

Input("date-picker", "start_date"),
Input("date-picker", "end_date"),
Input("ma-dropdown", "value")

จากนั้นกรองข้อมูลตามช่วงวันที่

filtered_df = df[
    (df["Date"] >= start_date) &
    (df["Date"] <= end_date)
].copy()

ส่วนนี้ทำให้แสดงเฉพาะข้อมูลที่เลือก 

app

4. การสร้างกราฟ
กราฟราคาปิด
fig1 = px.line(filtered_df, x="Date", y="Close")

แสดงราคาปิดของหุ้น

กราฟ Volume
fig2 = px.bar(filtered_df, x="Date", y="Volume")

แสดงปริมาณการซื้อขาย

กราฟ Moving Average

คำนวณค่า Moving Average

filtered_df["MA"] = filtered_df["Close"].rolling(ma_value).mean()

สร้างกราฟ

fig3 = px.line(filtered_df, x="Date", y=["Close", "MA"])

แสดง

ราคาปิด

ค่า Moving Average

5. การรันโปรแกรม
if __name__ == "__main__":
    app.run(debug=True)

ใช้รัน Dash Server 

app

เมื่อรันแล้วจะเปิด Web Server

เช่น

http://127.0.0.1:8050
Library ที่ใช้

ติดตั้งจากไฟล์ requirements.txt

dash
plotly
pandas
dash-bootstrap-components

ใช้สำหรับ

Dash → สร้าง Web App

Plotly → สร้างกราฟ

Pandas → จัดการข้อมูล 

requirements

วิธีรันโปรแกรม
1. ติดตั้ง Python

ต้องใช้ Python 3.8 ขึ้นไป

ตรวจสอบ:

python --version
2. ติดตั้ง Library

เปิด Terminal แล้วพิมพ์

pip install -r requirements.txt
3. รันโปรแกรม

พิมพ์คำสั่ง

python app.py
4. เปิด Dashboard

เปิด Browser แล้วเข้า

http://127.0.0.1:8050

จะเห็น Dashboard หุ้น NVIDIA

ความสามารถของโปรแกรม

เลือกช่วงวันที่ได้

เลือก Moving Average ได้

แสดงกราฟแบบ Interactive

Zoom ได้

Hover ดูค่าได้
