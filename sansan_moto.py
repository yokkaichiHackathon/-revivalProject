import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import matplotlib.pyplot as plt

# Google Sheets APIの設定
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/creds.json', scope)
client = gspread.authorize(creds)


# スプレッドシートを開く
sheet = client.open('Your Spreadsheet Name').sheet1

# データを取得
data = sheet.get_all_records()

# データをDataFrameに変換
df = pd.DataFrame(data)

# グラフを作成
plt.plot(df['ColumnX'], df['ColumnY'])  # ColumnXとColumnYを実際の列名に置き換えてください
plt.title('Graph Title')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()




''' 
注意点
'path/to/your/creds.json'は、ダウンロードしたJSONファイルのパスに置き換えてください。
'Your Spreadsheet Name'は、アクセスしたいスプレッドシートの名前に置き換えてください。
ColumnXとColumnYは、グラフ化したいデータの列名に置き換えてください。
'''