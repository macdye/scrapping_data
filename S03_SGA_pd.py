# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
from datetime import datetime


# %%
from scraping.scrap_S03_SGA import episodes_S03_SGA

#%%
df_S03_SGA = pd.DataFrame(episodes_S03_SGA)
df_S03_SGA

#%%
df_S03_SGA['audience_fr'] = df_S03_SGA['audience_fr'].apply(lambda x: x.replace('Indisponible.', 'NA'))
df_S03_SGA['audience_us'] = df_S03_SGA['audience_us'].apply(lambda x: x.replace(' millions', ''))
df_S03_SGA['audience_us'] = df_S03_SGA['audience_us'].apply(lambda x: x.replace(',', '.'))
df_S03_SGA['diffusion_date'] = df_S03_SGA['diffusion_date'].apply(lambda x: x.replace('\n', ''))
df_S03_SGA.astype({'audience_us': float})
df_S03_SGA


# %%
month_list = {
    'janvier' : 1,
    'février' : 2,
    'mars' : 3,
    'avril' : 4,
    'mai' : 5,
    'juin' : 6,
    'juillet' : 7,
    'août' : 8,
    'septembre' : 9,
    'octobre' : 10,
    'novembre' : 11,
    'décembre' : 12
}

df_S03_SGA['day'] = df_S03_SGA['diffusion_date'].apply(lambda x: x.split(' ')[0])
df_S03_SGA['month'] = df_S03_SGA['diffusion_date'].apply(lambda x: x.split(' ')[1]).map(month_list)
df_S03_SGA['year'] = df_S03_SGA['diffusion_date'].apply(lambda x: x.split(' ')[2])
df_S03_SGA['diffusion_date'] = pd.to_datetime(df_S03_SGA[['year', 'month', 'day']])
df_S03_SGA


# %%
df_S03_SGA.insert(0, 'serie', 'Stargate Atlantis')
df_S03_SGA


