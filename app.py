from flask import Flask, render_template, request, redirect, flash
import requests
import Quandl
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
# import matplotlib

app = Flask(__name__)


class ReusableForm(Form):
    name = TextField('Name:',)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    # form = ReusableForm(request.form)
    # print (form.errors)
    # if request.method == 'POST':
    #     startdate = request.form['Start Date']
    #     enddate = request.form['End Date']
        #
        # print (startdate)
        #
        # if form.validate():
        #     Save the comment here.
            # flash('Hello ' + startdate)
        # else:
        #     flash('All the form fields are required. ')
    #
    # return render_template('input.html', form=form)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   # if request.method == 'POST':
      result = request.form
      startdate = result["start"]
      print(startdate)
      enddate = result["end"]
      mydata = Quandl.get("ZILLOW/C25709_ZRISFRR", authtoken="QT-coVZNkYPJCs6R9Tkj")
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

      p.line(x=df['Date'].values, y=df['Value'].values, line_width=2,legend='Close')


      # render template
      script, div = components(p)

      # INSERT CODE HERE WHICH PLOTS A DATA




      # END OF PLOTTING DATA

      return render_template("result.html", plot_script=script, plot_div=div,)


@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)


