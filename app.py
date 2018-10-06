from flask import Flask, render_template, request, redirect, flash
import Quandl
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.embed import components

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
      plot = figure(plot_height=300, sizing_mode='scale_width')

      x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
      y = [2 ** v for v in x]

      plot.line(x, y, line_width=4)

      script, div = components(plot)
      # INSERT CODE HERE WHICH PLOTS A DATA




      # END OF PLOTTING DATA

      return render_template("result.html", result = result, script=script, div=div)


@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)


