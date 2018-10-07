import Quandl
import requests
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.embed import components
import matplotlib.pyplot as plt

# mydata = Quandl.get("ZILLOW/C25709_ZRISFRR", authtoken="QT-coVZNkYPJCs6R9Tkj")
# df = pd.DataFrame(mydata)
# g = df.plot()
# pass
# # mydata = Quandl.get("ZILLOW/C25709_ZRISFRR", authtoken="QT-coVZNkYPJCs6R9Tkj", startdate=startdate, enddate=enddate)


api_url = 'https://www.quandl.com/api/v3/datasets/ZILLOW/C25709_ZRISFRR.json?api_key=QT-coVZNkYPJCs6R9Tkj'
session = requests.Session()
session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
raw_data = session.get(api_url)

a = raw_data.json()
a1 = a['dataset']
df = pd.DataFrame(a1['data'], columns=a1['column_names'])
df['Date'] = pd.to_datetime(df['Date'])
p = figure(title='Stock prices',
           x_axis_label='date',
           x_axis_type='datetime')

p.line(x=df['Date'].values, y=df['Value'].values,)
plt.show()

pass