import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc

# TODO: document it and wrap it as pip package, make ipynb example



def get_paracoord_plot(values):
    # TODO: possibility to give label for each point and color accordingly, find color automatically or according to given dict
    # TODO: possibility to scale plot (minmax, unit=var, etc.)
    segments = [[(i, values[j, i]), (i + 1, values[j, i + 1])] for i in range(values.shape[1] - 1) for j in range(values.shape[0])]

    lc = mc.LineCollection(segments, linewidths=2)  # add `colors` with list of colors
    fig, ax = plt.subplots()

    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)

    for i in range(values.shape[1]):
        ax.axvline(x=i, ymin=-1, ymax=1)  # TODO: compute optimal ymin and ymax

    plt.show()
    # TODO: possibility to save plot


# np array example
values = np.random.random_sample((10, 5))
print(values)
get_paracoord_plot(values)