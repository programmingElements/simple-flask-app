from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__, template_folder='templates')

background_color = os.environ.get('BACKGROUND_COLOR');


@app.route('/')
def index():
  mylist = [10, 20, 30, 40, 50]
  return render_template('index.html', color=background_color, mylist=mylist)

@app.route('/home')
def home():
  some_text = "Hello World!"
  return render_template('home.html', some_text=some_text)

@app.template_filter('reverse_string')
def reverse_string(s):
  return s[::-1]

@app.template_filter('repeat')
def repeat(s,times=2):
  return s * times

@app.template_filter('alternate_case')
def alternate_case(s):
  return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

@app.route('/redirect_endpoint')
def redirect_endpoint():
  return redirect(url_for('home'))


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5001, debug=True)