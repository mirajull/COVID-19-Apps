import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['xtick.bottom'] = False
plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = False
plt.rcParams['xtick.labeltop'] = True

sns.set(font_scale=0.5)

df = pd.read_excel("heatmap_ap_north.xlsx", index_col=0, header=0)
fig, ax = plt.subplots(figsize=(8,5.9))
#flatui = ["#e74c3c", "#3498db", "#2ecc71"]
#sns.set_palette(flatui)
#cmap=sns.color_palette()
cmap=sns.color_palette("OrRd", 15)
ax1 = sns.heatmap(df, vmin=0, vmax=15, ax=ax, cbar=False, cmap=cmap, square=True)
plt.tight_layout()
plt.savefig("test.svg",bbox_inches='tight')
plt.show()
