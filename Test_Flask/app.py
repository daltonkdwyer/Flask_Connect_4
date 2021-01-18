from flask import Flask, render_template, request

app = Flask(__name__)

number_list = []
number = ''

@app.route("/")
def index():
    print(number)
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    print(request)
    number = request.form.get("number")
    number = int(number) * 2
    number_list.append(number)
    return render_template("result.html", number_list=number_list)
