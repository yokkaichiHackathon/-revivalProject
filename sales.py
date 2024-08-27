import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import matplotlib.pyplot as plt

# Google Sheets APIの設定
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/nakag/Downloads/sales_data.json', scope)
client = gspread.authorize(creds)

# スプレッドシートを開く
sheet = client.open('sales_dummy').sheet1

# データを取得
data = sheet.get_all_records()

# データをDataFrameに変換
df = pd.DataFrame(data)

# グラフを作成
plt.plot(df['店舗の種類'], df['売り上げ（円）'])  # 実際の列名に置き換えてください
plt.title('売り上げのグラフ')
plt.xlabel('店舗の種類')
plt.ylabel('売り上げ（円）')
plt.xticks(rotation=45)  # X軸ラベルが重ならないように回転
plt.tight_layout()  # レイアウト調整
plt.show()
