# %%
import gspread
import pandas as pd

# %%

gc = gspread.service_account()

sh = gc.open_by_key("17ro_SonlJfmLR6wtts4rkNakKIJ4GCZqbsxf5PGY90I")

df = pd.DataFrame(sh.sheet1.get_all_records())
# %%
new_rec = {'manufacturer': ['Elsys'], 'model': ['erslite']}
df = pd.concat([df, pd.DataFrame(new_rec)], ignore_index=True)
df