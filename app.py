from flask import Flask, request
app = Flask(__name__)
@app.route("/")

def home():
    email="check4obi@yahoo.com"
    mobile="2347036483444"
    return "These are the company contact details" + email + "," + mobile

email + "," + mobile

@app.route("/calculate")

def calculate():
    a = 56
    b = 34
    cal= a + b
    return "This is the sum total:" + str(cal)


if __name__== '__name__':
    app.run(debug=True, port=5004, host="0.0.0.0")

