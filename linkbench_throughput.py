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
tpt_rocksdb = [0.097588, 0.142451, 0.195590, 0.234207, 0.256926, 0.234715, 0.438031, 0.881419]
tpt_livegraph = [0.047314, 0.051131, 0.064784, 0.084691, 0.112838, 0.181505, 0.255426, 0.373964]
for i in range(len(tpt_rocksdb)):
	tpt_rocksdb[i] = 1000.0 / tpt_rocksdb[i] * num_threads[i]
for i in range(len(tpt_livegraph)):
	tpt_livegraph[i] = 1000.0 / tpt_livegraph[i] * num_threads[i]

ax.plot(num_threads[:len(tpt_rocksdb)], tpt_rocksdb, '-o', color='black', markerfacecolor='none', label='RocksDB')
ax.plot(num_threads[:len(tpt_livegraph)], tpt_livegraph, '-o', color='black', label='LiveGraph')

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim([0.7, 180])
ax.set_ylim([0, 600e3])
ax.set_xlabel('# of Clients', fontsize=9)
ax.set_ylabel('Throughput-LinkBench (req/s)', fontsize=9)
ax.set_xticks(num_threads)
ax.set_xticklabels(['1', '2', '4', '8', '16', '32', '64', '128'], fontsize=9)
ax.set_yticks([6.25e3, 25e3, 100e3, 400e3])
ax.set_yticklabels(['6.25K', '25K', '100K', '400K'], fontsize=9)
ax.tick_params(axis='x', which='both', top='off', bottom='off')
ax.legend(loc='lower right')

fig.tight_layout()
fig.savefig('linkbench_throughput.pdf')
