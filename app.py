from flask import Flask, render_template, request, redirect, flash
import Quandl
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

app = Flask(__name__)


class ReusableForm(Form):
    name = TextField('Name:',)

@app.route('/')
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
   if request.method == 'POST':
      result = request.form
      startdate = result["start"]
      enddate = result["end"]
      mydata = Quandl.get("ZILLOW/C25709_ZRISFRR", authtoken="QT-coVZNkYPJCs6R9Tkj", startdate=startdate, enddate=enddate)
      # fig = figure(plot_width=600, plot_height=600)
      fig = mydata.plot()

      # init a basic bar chart:
      # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars

      # fig.vbar(
      #     x=[1, 2, 3, 4],
      #     width=0.5,
      #     bottom=0,
      #     top=[1.7, 2.2, 4.6, 3.9],
      #     color='navy'
      # )

      # grab the static resources
      js_resources = INLINE.render_js()
      css_resources = INLINE.render_css()

      # render template
      script, div = components(fig)

      # INSERT CODE HERE WHICH PLOTS A DATA




      # END OF PLOTTING DATA

      return render_template("result.html", result = result, plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,)


@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)


