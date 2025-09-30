from flask import Flask

''' It create an instanceof the flask class,
which will be your "WSGI" application
'''
## WSGI
app=Flask(__name__)

@app.route("/")
def welcome():
  return "Welcome the this flask course why. this should be amzing and i want this course"

@app.route("/index")
def indexPage():
  return "Wlecome to the index page"

if __name__ =="__main__":
    app.run(debug=True)