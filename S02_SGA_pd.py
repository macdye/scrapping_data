# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
from datetime import datetime


# %%
from scraping.scrap_S02_SGA import episodes_S02_SGA

#%%
df_S02_SGA = pd.DataFrame(episodes_S02_SGA)
df_S02_SGA

#%%
df_S02_SGA['audience_us'] = df_S02_SGA['audience_us'].apply(lambda x: x.replace(' millions', ''))
df_S02_SGA['audience_fr'] = df_S02_SGA['audience_fr'].apply(lambda x: x.replace(' millions', ''))
df_S02_SGA['audience_us'] = df_S02_SGA['audience_us'].apply(lambda x: x.replace(',', '.'))
df_S02_SGA['audience_fr'] = df_S02_SGA['audience_fr'].apply(lambda x: x.replace(',', '.'))
df_S02_SGA['diffusion_date'] = df_S02_SGA['diffusion_date'].apply(lambda x: x.replace('\n', ''))
df_S02_SGA.astype({'audience_us': float, 'audience_fr': float})
df_S02_SGA


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

df_S02_SGA['day'] = df_S02_SGA['diffusion_date'].apply(lambda x: x.split(' ')[0])
df_S02_SGA['month'] = df_S02_SGA['diffusion_date'].apply(lambda x: x.split(' ')[1]).map(month_list)
df_S02_SGA['year'] = df_S02_SGA['diffusion_date'].apply(lambda x: x.split(' ')[2])
df_S02_SGA['diffusion_date'] = pd.to_datetime(df_S02_SGA[['year', 'month', 'day']])
df_S02_SGA

# %%
df_S02_SGA.insert(0, 'serie', 'Stargate Atlantis')
df_S02_SGA


