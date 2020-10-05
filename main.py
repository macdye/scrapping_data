# %%
import pandas as pd
from S10_SG1_pd import df_S10_SG1
from S09_SG1_pd import df_S09_SG1
from S08_SG1_pd import df_S08_SG1

# %%
df_SG1 = df_S08_SG1.append(df_S09_SG1).reset_index(drop= True)
df_SG1

# %%
df_SG1 = df_SG1.append(df_S10_SG1).reset_index(drop=True)
df_SG1
# %%
