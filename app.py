from flask import Flask, render_template, request, redirect, flash
import Quandl
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

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
      return render_template("result.html",result = result)


@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
  mydata = Quandl.get("ZILLOW/C25709_ZRISFRR", authtoken="QT-coVZNkYPJCs6R9Tkj")

