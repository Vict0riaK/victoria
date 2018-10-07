import Quandl
import requests
import pandas as pd
import numpy as np
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
import matplotlib.pyplot as plt
import datetime

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
# p = df[['Date','Value']].plot('Date', figsize=(15,8))
df.set_index('Date')
df['Date'] = pd.to_datetime(df['Date'])
output_file("datetime.html")
p = figure(title='Stock prices',
           x_axis_label='date',
           x_axis_type='datetime')

p.line(x=df['Date'].values, y=df['Value'].values,)
show(p)

pass