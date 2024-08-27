import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import plotly.express as px

# Google Sheets APIに接続
scope = ["https://docs.google.com/spreadsheets/d/1pQkVMtU9geXt_qahtQMf726RVDEtbyxmg8HaLss78Mk/edit?gid=0#gid=0", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# スプレッドシートのデータを読み込む
sheet = client.open("your-spreadsheet-name").sheet1  # シート名を指定

# A列とB列のデータを取得
a_column = sheet.col_values(1)[1:]  # A列のデータ（ヘッダーを除く）
b_column = sheet.col_values(2)[1:]  # B列のデータ（ヘッダーを除く）

# DataFrameに変換
df = pd.DataFrame({
    'X': a_column,  # 横軸に使用するデータ
    'Y': b_column   # 縦軸に使用するデータ
})

# データの可視化（例: 折れ線グラフ）
fig = px.line(df, x='X', y='Y', title='Custom Line Plot')
fig.show()
