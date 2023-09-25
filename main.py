from flask import Flask, render_template, request
import calc_func


app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/calculator', methods = ["POST", "GET"])
def calculator():
  if request.method == "POST":
    month = int(request.form["month"])
    interest = float(request.form["interest"])
    total = int(request.form["total"])
    x = calc_func.calc(month, interest, total)
    return render_template('calculator.html', x=x)
    
  return render_template('calculator.html')

@app.route('/moreinfo')
def moreinfo():
    return render_template('moreinfo.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)