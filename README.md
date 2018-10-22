# paracoord: Plot 2-dimensional arrays in Parallel coordinates

## Purpose
This package is an attempt to implement the idea of 
[parallel coordinates](https://link.springer.com/article/10.1007/s11416-009-0127-3) 
from [Sébastien Tricaud](https://www.splunk.com/blog/author/stricaud.html) and [
Philippe Saadé](mailto:psaade@gmail.com) to general purposes.

## Example
```
from paracoord import get_paracoord_plot


# Create 10x5 random array
values = np.random.random_sample((10, 5))
print(values)

# Plot parallel coordinates of those values
get_paracoord_plot(values)

# Set arbitrary labels for those 10 5-dimensional vectors
labels = ['aaa', 'bbb', 'aaa', 'ccc', 'bbb', 'aaa', 'aaa', 'bbb', 'aaa', 'ccc']
# Plot them in parallel coordinates with automatically chosen colors
get_paracoord_plot(values, labels=labels)
# Plot them with self defined color dict and save the resulting plot
color_dict = {'aaa': 'b', 'bbb': 'r', 'ccc': 'g'}
get_paracoord_plot(values, labels=labels, color_dict=color_dict, save_path='random_example.jpg', set_legend=True)
```

## Options
* `values`: 2-dimensional numpy array
* `labels`: optional, array containing labels for each row of `values`
* `color_dict`: dict, optional, ignored if ` labels` not provided. {label -> color} dict.
If `labels` is provided but not `color_dict`, the color of each label will be automatically chosen
* `save_path`: path to the file where the resulting image will be stored.
If not provided, image will not be stored
* `set_legend`: boolean, optional, ignored if `labels`not provided. If to set a color legend for the labels or not
* `box`: boolean. If to set a frame (x-axis, y-axis etc.) for the resulting image
* `ylims`: (ymin, ymax). If not provided, will be set to the result to `get_y_min_nax(values)`


## Installation
```
pip install paracoord
```

## Final note
Enjoy, do whatever you want with it as long as you don't hold me responsible for the consequences :)
Suggestions, remarks, critics, pull requests appreciated