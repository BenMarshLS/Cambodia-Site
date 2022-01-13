from flask import Flask, render_template, request, url_for, redirect

import random, string, sqlite3

app = Flask(__name__)

#SQL failure
#connection = sqlite3.connect('names.db')
#db = connection.cursor()
#db.execute("CREATE TABLE names (column1 name varchar(255), column2 yod int, column3 obit bool);")
#query = db.execute("SELECT DISTINCT name, yod, obit from names").fetchall()
#for name, yod, obit in query:
    #print(name, yod, obit)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/contact", methods= ["GET", "POST"])
def contact():
  return render_template("contact.html")

@app.route("/charity", methods= ["GET", "POST"])
def charity():
  return render_template("charity.html")

@app.route("/memory", methods= ["GET", "POST"])
def memory():
  return render_template("memory.html")

@app.route("/info", methods= ["GET", "POST"])
def info():
  return render_template("info.html")

@app.route("/obit", methods= ["GET", "POST"])
def obit():
  return render_template("obit.html")

@app.route("/why", methods= ["GET", "POST"])
def why():
  return render_template("why.html")

@app.route("/article", methods= ["GET", "POST"])
def article():
  return render_template("article.html")

@app.route("/addinfo", methods= ["GET", "POST"])
def addinfo():
  return render_template("addinfo.html")

#connection.commit()  
#connection.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000)