from flask import Flask, render_template, request, redirect
import quandl

app = Flask(__name__)

@app.route('/')
def index():
  # return render_template('index.html')
    print (mydata)
@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
  mydata = quandl.get("ZILLOW/C25709_ZRISFRR", authtoken="QT-coVZNkYPJCs6R9Tkj")

