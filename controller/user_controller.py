from main import app
from flask import request

from model.user_model import user_model

obj = user_model()

@app.route('/user/signup')
def user_signup_controler():
    return obj.user_signup_model()


@app.route('/user/adduser', methods=["POST"])
def user_adduser():
    return obj.add_user(request.form)