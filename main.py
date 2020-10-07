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
