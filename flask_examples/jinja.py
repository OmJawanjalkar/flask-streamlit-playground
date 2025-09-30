### Building Url Dynamically
## Variale
## Jinja 2 Templet

## Jinja Templete Engine
'''
{{ }}  expressinon to print output in html
{%...%} condition, for loops
{#...#} This fpr commant
'''
from flask import Flask,request,render_template,redirect,url_for

''' It create an instanceof the flask class,
which will be your "WSGI" application
'''
## WSGI
app=Flask(__name__)

@app.route("/")
def welcome():
  return "<html><H1>I am Om Jawanjalkar & I am the student</H1></html>"




## Variable Rule
@app.route("/success/<int:score>")
def success(score):
  res=""
  if score>=50:
    res="PASSED"
  else:
    res="FAILED"

  return render_template('result.html',results=res)

@app.route("/successres/<int:score>")
def successres(score):
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    exp = {'score': score, 'res': res}   # dictionary with both values
    return render_template('result1.html', results=exp)



## if confition
@app.route("/successif/<int:score>")
def successif(score):


  return render_template('result.html',results=score)

@app.route("/fail/<int:score>")
def fail(score):

  return render_template('result.html',results=score)

@app.route("/submit", methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + c + data_science) / 4
    return redirect(url_for('successres', score=total_score))









if __name__ =="__main__":
    app.run(debug=True)