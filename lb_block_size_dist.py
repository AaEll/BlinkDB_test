
numbers = map(int, '''
0
0
15081387
7566512
1498751
312011
120354
49091
26627
18269
14221
11433
8502
5139
2422
814
190
32
10
0
2
'''.strip().split())

import numpy as np
import matplotlib.pyplot as plt

params = {'legend.fontsize': 15,
          'legend.linewidth': 2,
          'pdf.fonttype': 42}
plt.rcParams.update(params)

fig, ax = plt.subplots()
fig.set_size_inches(4, 2.5)

ax.plot(range(len(numbers)), numbers, '-', color='black')

ax.set_xlabel('MALL Block Size (Bytes)', fontsize=15)
ax.set_ylabel('# of Blocks', fontsize=15)

ax.set_yscale('log')
ax.set_yticks([10, 1000, 1e5, 1e7])
ax.set_yticklabels(['10', '1K', '100K', '10M'], fontsize=15)
ax.set_xticks([0, 5, 10, 15, 20])
ax.set_xticklabels(['32', '1K', '32K', '1M', '32M'], fontsize=15)

fig.tight_layout()
fig.savefig('lb_block_size_dist.pdf')
