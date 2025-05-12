from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "hello world"





from controller import *


if __name__ == '__main__':
    app.run(debug=True)

# flask --app main.py --debug run

# git commit -am "Updated code" && git push origin main






