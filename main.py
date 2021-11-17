from flask import Flask, render_template, request, url_for, redirect
import random, string

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/contact", methods= ["GET", "POST"])
def contact():
  return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=random.randint(2000, 9000))
