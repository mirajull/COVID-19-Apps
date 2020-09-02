import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['xtick.bottom'] = False
plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = False
plt.rcParams['xtick.labeltop'] = True

sns.set(font_scale=0.8)

df = pd.read_excel("heatmap_ca_south.xlsx", index_col=0, header=0)

fig, ax = plt.subplots(figsize=(12, 7))
#flatui = ["#e74c3c", "#3498db", "#2ecc71"]
#flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
#cmap=sns.light_palette("red", as_cmap=True)
#cmap=sns.color_palette("flatui")
ax1 = sns.heatmap(df,  vmin=0, vmax=20, ax=ax, cbar=False, cmap="OrRd", square=True)
plt.tight_layout()
plt.savefig("test.svg",bbox_inches='tight')
plt.show()
