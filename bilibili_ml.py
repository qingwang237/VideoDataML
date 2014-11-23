import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import ticker

from sklearn.cluster import KMeans


formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1, 1))


data = np.loadtxt(
    open("data.csv", "rb"), delimiter=",", skiprows=1)

X = np.log(data[:, 1:])
estimator = KMeans(n_clusters=4)
estimator.fit(X)
labels = estimator.labels_

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:, 2], data[:, 3], data[:, 1],
           c=labels.astype(np.float), marker='o')
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)
ax.zaxis.set_major_formatter(formatter)
# ax.set_xscale('log')
# ax.set_yscale('log')
# ax.set_zscale('log')

ax.set_xlabel('Favorites')
ax.set_ylabel('Danmu')
ax.set_zlabel('Total View Counts')


plt.show()
