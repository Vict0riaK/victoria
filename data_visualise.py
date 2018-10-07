import Quandl
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.embed import components

mydata = Quandl.get("ZILLOW/C25709_ZRISFRR", authtoken="QT-coVZNkYPJCs6R9Tkj")
df = pd.DataFrame(mydata)
g = df.plot()
pass
# mydata = Quandl.get("ZILLOW/C25709_ZRISFRR", authtoken="QT-coVZNkYPJCs6R9Tkj", startdate=startdate, enddate=enddate)