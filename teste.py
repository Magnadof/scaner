import requests

url_excel_online = 'https://1drv.ms/x/s!ApJISqN4bsr4gdkdM33YesEBS3O2Gw?e=7pYuJg'
local_file_path = 'local_file.xlsx'

# Faz o download do conteúdo do arquivo
response = requests.get(url_excel_online)
with open(local_file_path, 'wb') as f:
    f.write(response.content)

import pandas as pd

local_file_path = 'local_file.xlsx'

df=pd.read_excel('local_file_path.xlsx')
print(df)
