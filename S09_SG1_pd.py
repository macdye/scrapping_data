# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
from datetime import datetime


# %%
from scraping.scrap_S09_SG1 import episodes_S09_SG1


# %%
#episodes_S09_SG1


# %%
df_S09_SG1 = pd.DataFrame(episodes_S09_SG1)
df_S09_SG1


# %%
df_S09_SG1['audience_us'] = df_S09_SG1['audience_us'].apply(lambda x: x.replace(' millions', ''))
df_S09_SG1['audience_us'] = df_S09_SG1['audience_us'].apply(lambda x: x.replace(',', '.'))
df_S09_SG1['diffusion_date'] = df_S09_SG1['diffusion_date'].apply(lambda x: x.replace('\n', ''))
df_S09_SG1.astype({'audience_us':'float'})
df_S09_SG1


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

df_S09_SG1['day'] = df_S09_SG1['diffusion_date'].apply(lambda x: x.split(' ')[0])
df_S09_SG1['month'] = df_S09_SG1['diffusion_date'].apply(lambda x: x.split(' ')[1]).map(month_list)
df_S09_SG1['year'] = df_S09_SG1['diffusion_date'].apply(lambda x: x.split(' ')[2])

df_S09_SG1


# %%
df_S09_SG1['diffusion_date'] = pd.to_datetime(df_S09_SG1[['year', 'month', 'day']])
df_S09_SG1


# %%
df_S09_SG1.insert(0,'serie', 'Stargate SG1')
df_S09_SG1


# %%
df_S09_SG1['audience_fr'] = df_S09_SG1['audience_fr'].apply(lambda x: x.replace('Indisponible.', 'NA'))
df_S09_SG1['director'] = df_S09_SG1['director'].apply(lambda x: x.replace('William Warring', 'William Waring'))
df_S09_SG1['director'] = df_S09_SG1['director'].apply(lambda x: x.replace('And Mikita', 'Andy Mikita'))
df_S09_SG1
