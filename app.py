from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

# @app.route("/graphs")
# def graphs():
#     return render_template('graphs.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
