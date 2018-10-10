import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc

# TODO: document it and wrap it as pip package, make ipynb example


def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n + 1)  # +1 otherwise last color is almost like first one


def get_y_min_max(nparr):
    ymin, ymax = np.amin(nparr), np.amax(nparr)
    length = ymax - ymin
    ymin -= 0.05 * length
    ymax += 0.05 * length
    return ymin, ymax



def get_paracoord_plot(values, labels=None, color_dict=None, save_path=None, set_legend=False):
    # TODO: possibility to scale plot (minmax, unit=var, etc.)
    fig, ax = plt.subplots()
    segments = [[(i, values[j, i]), (i + 1, values[j, i + 1])] for j in range(values.shape[0]) for i in range(values.shape[1] - 1)]

    if labels is not None:
        labels = np.array(labels)
        distinct_labels = list(set(labels))
        assert labels.shape[0] == values.shape[0], 'there must be as much labels as rows in values, ' \
                                                   'here: {} labels for {} rows in values'.format(labels.shape[0], values.shape[0])

        if color_dict is not None:
            assert set(list(labels)) == set(color_dict.keys()), 'the keys of color_dict and the labels must be the same'

        else:
            cmap = get_cmap(len(distinct_labels))
            color_dict = {distinct_labels[i]: cmap(i) for i in range(len(distinct_labels))}

        colors = list(itertools.chain.from_iterable([[color_dict[l]] * (values.shape[1] - 1) for l in list(labels)]))
        lcs = []
        for color_value in color_dict.values():
            # Divide segments by color
            segments_color = [segments[i] for i in range(len(segments)) if colors[i] == color_value]
            lc = mc.LineCollection(segments_color, linewidths=2, colors=color_value)
            ax.add_collection(lc)
            lcs.append(lc)
        if set_legend:
            ax.legend(lcs, distinct_labels, bbox_to_anchor=(1, 1))

    else:
        lc = mc.LineCollection(segments, linewidths=2, colors='b')
        ax.add_collection(lc)

    ax.autoscale()

    # TODO: set x-ticker spaced by unit

    ymin, ymax = get_y_min_max(values)
    for i in range(values.shape[1]):
        ax.axvline(x=i, ymin=ymin, ymax=ymax, color='k')

    if save_path is not None:
        plt.savefig(save_path)

    plt.show()




# np array example
values = np.random.random_sample((10, 5))
print(values)
get_paracoord_plot(values)
labels = ['aaa', 'bbb', 'aaa', 'ccc', 'bbb', 'aaa', 'aaa', 'bbb', 'aaa', 'ccc']
get_paracoord_plot(values, labels=labels)
color_dict = {'aaa': 'b', 'bbb': 'r', 'ccc': 'g'}
get_paracoord_plot(values, labels=labels, color_dict=color_dict, save_path='images/random_example.jpg', set_legend=True)