#!/usr/bin/env python3

# %%
import sys
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe

import pandas as pd
fn = sys.argv[1]

# %%

gc = gspread.service_account()

sh = gc.open_by_key("17ro_SonlJfmLR6wtts4rkNakKIJ4GCZqbsxf5PGY90I")
wks = sh.sheet1
df = pd.DataFrame(wks.get_all_records())
last_order_num = df.order_num.max()

df_new = pd.read_csv(fn, delimiter=';')
df_new = df_new[['SKU', 'EUI', 'AppKey', 'FW']]
df_new.columns = ['model', 'dev_eui', 'app_key', 'firmware']
df_new['manufacturer'] = 'Elsys'
df_new['order_num'] = last_order_num + 1
#df_new['firmware'] = [fw.split('_')[0] for fw in df_new.firmware.values]

df = pd.concat([df, df_new], ignore_index=True)
set_with_dataframe(wks, df)
df.to_csv('df.csv')