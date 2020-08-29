import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['xtick.bottom'] = False
plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = False
plt.rcParams['xtick.labeltop'] = True

sns.set(font_scale=0.5)

df = pd.read_excel("heatmap_ap_south.xlsx", index_col=0, header=0)
fig, ax = plt.subplots(figsize=(8,5.9))
ax1 = sns.heatmap(df,  vmin=0, vmax=15, ax=ax, cbar=False, cmap="YlGnBu", square=True)
plt.tight_layout()
plt.savefig("test.svg",bbox_inches='tight')
plt.show()
