import os

file_path = 'C:/Users/nakag/Downloads/sales_data.json'

if os.path.exists(file_path):
    print("ファイルが存在します。")
else:
    print("ファイルが見つかりません。パスを確認してください。")