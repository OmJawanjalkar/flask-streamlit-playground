from flask import Flask,render_template

''' It create an instanceof the flask class,
which will be your "WSGI" application
'''
## WSGI
app=Flask(__name__)

@app.route("/")
def welcome():
  return "<html><H1>I am Om Jawanjalkar & I am the student</H1></html>"

@app.route("/index")
def indexPage():
  return render_template('index.html')

@app.route("/about")
def about():
  return render_template('about.html')

if __name__ =="__main__":
    app.run(debug=True)