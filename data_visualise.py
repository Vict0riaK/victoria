import Quandl
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.embed import components

mydata = Quandl.get("ZILLOW/C25709_ZRISFRR", authtoken="QT-coVZNkYPJCs6R9Tkj")
plot = figure(plot_height=300, sizing_mode='scale_width')

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2 ** v for v in x]

plot.line(x, y, line_width=4)

script, div = components(plot)