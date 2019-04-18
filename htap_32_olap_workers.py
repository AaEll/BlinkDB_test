#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

params = {'legend.fontsize': 15,
          'legend.linewidth': 1,
          'pdf.fonttype': 42}
plt.rcParams.update(params)

fig, ax = plt.subplots()
fig.set_size_inches(4, 2.5)

latency_corun = [0.164245, 0.237357, 0.436652, 0.641406, 0.775183, 0.880378]
latency_alone = [0.085618, 0.102867, 0.155946, 0.209481, 0.26169, 0.284247]

time_pagerank = [11.252377, 12.556378, 13.143194, 13.312559, 13.461941, 13.500465]


ax.plot([1, 2, 4, 8, 16, 32], latency_corun, '-o', color='black', label='LinkBench Co-run')
ax.plot([1, 2, 4, 8, 16, 32], latency_alone, '--.', color='black', label='LinkBench Alone')

ax.set_xscale('log')
# ax.set_yscale('log')
ax.set_xlim([0.8, 40])
ax.set_ylim([0, 1])
ax.set_xlabel('Request Rate (K req/s)', fontsize=15)
ax.set_ylabel('Latency (ms)', fontsize=15)
ax.set_xticks([0.8, 1, 2, 4, 8, 16, 32, 40])
ax.set_xticklabels(['', '40', '80', '160', '320', '640', '1280', ''], fontsize=12)
ax.set_yticks([0.1, 0.4, 0.7, 1.0])
ax.set_yticklabels(['0.1', '0.4', '0.7', '0.9'], fontsize=15)
ax.tick_params(axis='x', which='both', top='off', bottom='off')

ax2 = ax.twinx()
ax2.plot([1, 2, 4, 8, 16, 32], time_pagerank, '-o', color='grey', markerfacecolor='none', label='PageRank')
# ax2.set_xscale('log')
# ax2.set_yscale('log')
ax2.set_xlim([0.8, 40])
ax2.set_ylim([0, 15])
# ax2.set_xticks([0.8, 1, 2, 4, 8, 16, 32, 40])
# ax2.set_xticklabels(['', '40K', '80K', '160K', '320K', '640K', '1.28M', ''], fontsize=15)
ax2.set_yticks([3, 7, 11, 15])
ax2.set_yticklabels(['3', '7', '11', '15'], fontsize=15)
ax2.set_ylabel('Runtime (s)', fontsize=15)

# legend = ax2.legend(loc='lower center')
# for legend_handle in legend.legendHandles:
#     legend_handle._legmarker.set_markersize(3)
# legend = ax.legend(loc='lower right')
# for legend_handle in legend.legendHandles:
#     legend_handle._legmarker.set_markersize(3)

fig.tight_layout()
fig.savefig('htap_32_olap_workers.pdf')
