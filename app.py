from flask import Flask, render_template

app = Flask(__name__)


####Routing Functions####\


@app.route('/')
def home():
    
    return render_template('home.html', mess = "There is no model Please add one")


@app.route("/start", methods=['GET'])
def start():
    return "This is start page"

@app.route("/add", methods=['GET', 'POST'])
def add():
    return "This is add page"

if __name__ == "__main__":
    app.run(debug=True)
