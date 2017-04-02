# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
#import pickle

reload(sys)
sys.setdefaultencoding('utf-8')
corr_matrix = pd.read_csv('growth_correlation.csv', index_col = 0)
data1 = corr_matrix.values  # turn into an array matix
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
heatmap = ax1.pcolor(data1, cmap=plt.cm.RdYlGn)
fig1.colorbar(heatmap)
ax1.set_xticks(np.arange(data1.shape[1]) + 0.5, minor=False)
ax1.set_yticks(np.arange(data1.shape[0]) + 0.5, minor=False)
ax1.invert_yaxis()
ax1.xaxis.tick_top()
column_labels = corr_matrix.columns
#row_labels = corr_matrix.index
ax1.set_xticklabels(column_labels)
ax1.set_yticklabels(column_labels)

plt.xticks(rotation=90)
heatmap.set_clim(-1,1)
plt.tight_layout()
#plt.savefig("correlations.png")
#pickle.dump(ax1, file('gdp_corr.pickle', 'w'))
plt.show()
#ax1 = pickle.load(file('gdp_corr.pickle'))
#plt.show()
