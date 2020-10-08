# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
from datetime import datetime


# %%
from scraping.scrap_S10_SG1 import episodes_S10_SG1


# %%
#episodes_S10_SG1


# %%
df_S10_SG1 = pd.DataFrame(episodes_S10_SG1)
df_S10_SG1


# %%
df_S10_SG1['audience_us'] = df_S10_SG1['audience_us'].apply(lambda x: x.replace(' millions', ''))
df_S10_SG1['audience_us'] = df_S10_SG1['audience_us'].apply(lambda x: x.replace(',', '.'))
df_S10_SG1['diffusion_date'] = df_S10_SG1['diffusion_date'].apply(lambda x: x.replace('\n', ''))
df_S10_SG1.astype({'audience_us': float})
df_S10_SG1


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
    'décembre' : 12}

df_S10_SG1['day'] = df_S10_SG1['diffusion_date'].apply(lambda x: x.split(' ')[0])
df_S10_SG1['month'] = df_S10_SG1['diffusion_date'].apply(lambda x: x.split(' ')[1]).map(month_list)
df_S10_SG1['year'] = df_S10_SG1['diffusion_date'].apply(lambda x: x.split(' ')[2])

df_S10_SG1


# %%
df_S10_SG1['diffusion_date'] = pd.to_datetime(df_S10_SG1[['year', 'month', 'day']])
df_S10_SG1


# %%
df_S10_SG1.insert(0,'serie', 'Stargate SG1')
df_S10_SG1


# %%
df_S10_SG1['audience_fr'] = df_S10_SG1['audience_fr'].apply(lambda x: x.replace('Indisponible.', 'NA'))
df_S10_SG1

# %%
df_director_S10_SG1 = df_S10_SG1['director']
df_director_S10_SG1
# %%
df_essai_sep = df_S10_SG1['scenarist'].str.split(pat=(' & |, '))
df_essai_sep
df_essai_sep[1][0]
