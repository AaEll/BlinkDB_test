#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

params = {'legend.fontsize': 15,
          'legend.linewidth': 1,
          'pdf.fonttype': 42}
plt.rcParams.update(params)

fig, ax = plt.subplots()
fig.set_size_inches(4, 2.5)

latency_corun = [0.284247, 0.285612, 0.298169, 0.324806, 0.486928, 0.880378]
latency_alone = [0.283809, 0.283809]

time_pagerank = [223, 121, 61.574392, 31.324632, 18.211686, 13.288465]

ax.plot([1, 2, 4, 8, 16, 32], latency_corun, '-o', color='black', label='LinkBench Co-run')
ax.plot([1, 32], latency_alone, '--.', color='black', label='LinkBench Alone')

ax.set_xscale('log')
# ax.set_yscale('log')
ax.set_xlim([0.8, 40])
# ax.set_ylim([0, 0.37])
ax.set_ylim([0, 1])
ax.set_xlabel('# of OLAP workers', fontsize=15)
ax.set_ylabel('Latency (ms)', fontsize=15)
ax.set_xticks([0.8, 1, 2, 4, 8, 16, 32, 40])
ax.set_xticklabels(['', '1', '2', '4', '8', '16', '32', ''], fontsize=15)
# ax.set_yticks([0.32])
# ax.set_yticklabels(['0.32'], fontsize=15)
ax.set_yticks([0.1, 0.4, 0.7, 1.0])
ax.set_yticklabels(['0.1', '0.4', '0.7', '0.9'], fontsize=15)
ax.tick_params(axis='x', which='both', top='off', bottom='off')

ax2 = ax.twinx()
ax2.plot([1, 2, 4, 8, 16, 32], time_pagerank, '-o', color='grey', markerfacecolor='none', label='PageRank')
# ax2.set_xscale('log')
# ax2.set_yscale('log')
ax2.set_xlim([0.8, 40])
ax2.set_ylim([0, 260])
# ax2.set_xticks([0.8, 1, 2, 4, 8, 16, 32, 40])
# ax2.set_xticklabels(['', '40K', '80K', '160K', '320K', '640K', '1.28M', ''], fontsize=15)
ax2.set_yticks([10, 60, 120, 180, 240])
ax2.set_yticklabels(['10', '60', '120', '180', '240'], fontsize=15)
ax2.set_ylabel('Runtime (s)', fontsize=15)

# legend = ax2.legend(loc='upper left')
# for legend_handle in legend.legendHandles:
#     legend_handle._legmarker.set_markersize(3)
# legend = ax.legend(loc='upper center')
# for legend_handle in legend.legendHandles:
#     legend_handle._legmarker.set_markersize(3)

fig.tight_layout()
fig.savefig('htap_fixed_rr.pdf')
