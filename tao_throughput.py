#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

params = {'legend.fontsize': 9,
          'legend.linewidth': 2,
          'pdf.fonttype': 42}
plt.rcParams.update(params)

fig, ax = plt.subplots()
fig.set_size_inches(4, 2.5)

num_threads = [1, 2, 4, 8, 16, 32, 64, 128]
tpt_lmdb = [0.005016, 0.004988, 0.004536, 0.004609, 0.008043, 0.017746, 0.035887, 0.072610]
tpt_livegraph = [0.003922, 0.003674, 0.003578, 0.003865, 0.003954, 0.005180, 0.011112, 0.024863]
# 32: 0.005226
# 64: 0.011216
for i in range(len(tpt_lmdb)):
        tpt_lmdb[i] = 1000.0 / tpt_lmdb[i] * num_threads[i]
for i in range(len(tpt_livegraph)):
        tpt_livegraph[i] = 1000.0 / tpt_livegraph[i] * num_threads[i]

ax.plot(num_threads[:len(tpt_lmdb)], tpt_lmdb, '-o', color='black', markerfacecolor='none', label='LMDB')
ax.plot(num_threads, tpt_livegraph, '-o', color='black', label='LiveGraph')

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim([0.7, 180])
ax.set_ylim([0, 10e6])
ax.set_xlabel('# of Clients', fontsize=9)
ax.set_ylabel('Throughput-TAO (req/s)', fontsize=9)
ax.set_xticks(num_threads)
ax.set_xticklabels(['1', '2', '4', '8', '16', '32', '64', '128'], fontsize=9)
ax.set_yticks([0.125e6, 0.5e6, 2e6, 8e6])
ax.set_yticklabels(['125K', '500K', '2M', '8M'], fontsize=9)
ax.tick_params(axis='x', which='both', top='off', bottom='off')
ax.legend(loc='lower right')

fig.tight_layout()
fig.savefig('tao_throughput.pdf')
