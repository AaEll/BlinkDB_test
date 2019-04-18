#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

params = {'legend.fontsize': 15,
          'legend.linewidth': 1,
          'pdf.fonttype': 42}
plt.rcParams.update(params)



fig, ax = plt.subplots()
fig.patch.set_visible(False)
fig.set_size_inches(10, 0.8)

ax.plot([], [], '-o', color='black', label='LinkBench Co-Run')
ax.plot([], [], '-o', color='grey', markerfacecolor='none', label='PageRank')
ax.plot([], [], '-.', color='black', label='LinkBench Alone')

ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')
ax.legend(loc='upper center',ncol=3,numpoints=1)

fig.tight_layout()
fig.savefig('htap_legend.pdf')


