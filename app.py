from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', mess = "There is no model Please add one")

if __name__ == "__main__":
    app.run(debug=True)
