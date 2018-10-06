from flask import Flask, render_template, request, redirect, flash
import Quandl
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import pandas as pd
import numpy as np
import bokeh.charts as bc
from bokeh.resources import CDN
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
      df = pd.DataFrame({
                            'x': 2 * np.pi * i / 100,
                            'sin': np.sin(2 * np.pi * i / 100),
                            'cos': np.cos(2 * np.pi * i / 100),
                        } for i in range(0, 101))
      # Create the plot
      plot = bc.Line(title='Triganometric fun!',
                     data=df, x='x', ylabel='y')
      # Generate the script and HTML for the plot
      script, div = components(plot)

      # INSERT CODE HERE WHICH PLOTS A DATA




      # END OF PLOTTING DATA

      return render_template("result.html", result = result, script=script, div=div)


@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)


