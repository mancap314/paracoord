import itertools
import numpy as np
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
from matplotlib import collections  as mc

# TODO: document it and wrap it as pip package, make ipynb example


def get_cmap(n, name='hsv'):
    """
    Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name.
    """
    return plt.cm.get_cmap(name, n + 1)  # +1 otherwise last color is almost like first one


def get_y_min_max(nparr):
    """
    takes the min and max value of a numpy array and adds 5% of the length of (min, max) to the min and to the max
    """
    ymin, ymax = np.amin(nparr), np.amax(nparr)
    length = ymax - ymin
    ymin -= 0.05 * length
    ymax += 0.05 * length
    return ymin, ymax



def get_paracoord_plot(values, labels=None, color_dict=None, save_path=None, format='png', dim=(100, 50), linewidths=1, set_legend=False, box=False, show_vertical_axis=True, ylims=None, do_scale=None, show=True):
    """
    build parallel coordinates image corresponding to `values`
    :param values: 2-dimensional numpy array
    :param labels: optional, array containing labels for each row of `values`
    :param color_dict: dict, optional, ignored if ` labels` not provided. {label -> color} dict.
    If `labels` is provided but not `color_dict`, the color of each label will be automatically chosen
    :param save_path: path to the file where the resulting image will be stored.
    If not provided, image will not be stored
    :param format: str. format of the saved image (if saved), must belong to ['png', 'jpg', 'svg']
    :param dim: (int, int), dimension (in pixels) of the resulting image (for some reasons, the persisted images will not have exactly this size)
    :param linewidths: int, width (int px) of the plotted line(s)
    :param set_legend: boolean, optional, ignored if `labels`not provided. If to set a color legend for the labels or not
    :param box: boolean. If to set a frame (x-axis, y-axis etc.) for the resulting image
    :param show_vertical_axis: boolean. If to plot the vertical axis of the coordinates
    :param ylims: (ymin, ymax). If not provided, will be set to the result to `get_y_min_nax(values)
    :param do_scale: boolean. If True, `ylims` is ignored and `values` are centered (vertically) around their mean with std deviation of 1
    :param show: boolean. If to show the image though it is saved. If the image is not saved then it is shown anyway.
    :return: parallel coordinates image corresponding to `values`
    """
    dpi = 100
    figsize = (dim[0] / dpi, dim[1] / dpi)
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

    segments = [[(i, values[j, i]), (i + 1, values[j, i + 1])] for j in range(values.shape[0])
                for i in range(values.shape[1] - 1)]

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
            lc = mc.LineCollection(segments_color, linewidths=linewidths, colors=color_value)
            ax.add_collection(lc)
            lcs.append(lc)
        if set_legend:
            ax.legend(lcs, distinct_labels, bbox_to_anchor=(1, 1))

    else:
        lc = mc.LineCollection(segments, linewidths=linewidths, colors='b')
        ax.add_collection(lc)

    ax.autoscale()

    if do_scale:
        values = scale(values, axis=0, copy=True)

    if ylims is None or do_scale:
        ymin, ymax = get_y_min_max(values)
    else:
        ymin, ymax = ylims[0], ylims[1]

    if show_vertical_axis:
        for i in range(values.shape[1]):
            ax.axvline(x=i, ymin=ymin, ymax=ymax, color='k')

    if not box:
        plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='off')
        plt.box(False)

    plt.xlim(0, values.shape[1])
    plt.ylim(ymin, ymax)

    if save_path is not None:
        assert format in ['png', 'jpg', 'svg'], 'format must belong to [\'png\', \'jpg\', \'svg\']'
        plt.savefig(save_path, bbox_inches='tight', format=format, pad_inches=0)
        if show:
            plt.show()
    else:
        plt.show()

    # Clear the current axes.
    plt.cla()
    # Clear the current figure.
    plt.clf()
    # Closes all the figure windows.
    plt.close('all')
