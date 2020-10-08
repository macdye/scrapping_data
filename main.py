# %%
import pandas as pd
from S10_SG1_pd import df_S10_SG1
from S09_SG1_pd import df_S09_SG1
from S08_SG1_pd import df_S08_SG1
from S01_SGA_pd import df_S01_SGA
from S02_SGA_pd import df_S02_SGA
from S03_SGA_pd import df_S03_SGA

# %%
df_SG1 = df_S08_SG1.append(df_S09_SG1).reset_index(drop= True)
#df_SG1

# %%
df_SG1 = df_SG1.append(df_S10_SG1).reset_index(drop=True)
#df_SG1
# %%
df_stargate = df_SG1.append(df_S01_SGA).reset_index(drop=True)
#df_stargate
# %%
df_stargate = df_stargate.append(df_S02_SGA).reset_index(drop=True)
#df_stargate

# %%
df_stargate = df_stargate.append(df_S03_SGA).reset_index(drop=True)
df_stargate

#%%
df_series = df_stargate['serie']
df_series = df_series.drop_duplicates().reset_index(drop=True).rename('name')
df_series

# %%
df_diffusion_dates = df_stargate['diffusion_date']
df_diffusion_dates = df_diffusion_dates.drop_duplicates().sort_values().reset_index(drop=True).rename('date')
df_diffusion_dates
# %%
df_directors = df_stargate['director']
df_directors = df_directors.drop_duplicates().sort_values().reset_index(drop=True).rename('name')
df_directors
# %%
df_scenarists = df_stargate['scenarist']
df_scenarists = df_scenarists.apply(lambda x: x.replace('P&er DeLuise', 'Peter DeLuise'))
df_scenarists = df_scenarists.drop_duplicates().sort_values().reset_index(drop=True)
df_scenarists = df_scenarists.apply(lambda x: x.replace(' et ', ' & '))
df_scenarists = df_scenarists.apply(lambda x: x.replace(' &  ', ' & '))
df_scenarists = df_scenarists.apply(lambda x: x.replace(' &', ','))
df_scenarists
# %%
name_list = []
for name in df_scenarists :
  names = name.split(', ')
  for n in names :
    name_list.append(n)
name_list
# %%
df_scenarists = pd.Series(name_list, name='name')
df_scenarists = df_scenarists.apply(lambda x: x.replace(' Brad Wright', 'Brad Wright'))
df_scenarists = df_scenarists.apply(lambda x: x.replace('Jospeh Mallozzi', 'Joseph Mallozzi'))
df_scenarists = df_scenarists.drop_duplicates().sort_values().reset_index(drop=True)
df_scenarists
# %%
