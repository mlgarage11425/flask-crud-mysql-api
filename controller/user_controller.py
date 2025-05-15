from main import app
from flask import request

from model.user_model import user_model

obj = user_model()

@app.route('/user/readuser')
def user_signup_controler():
    return obj.user_signup_model()


@app.route('/user/createuser', methods=["POST"])
def user_adduser():
    return obj.add_user(request.form)



@app.route('/update', methods=["PUT"])
def user_updateuser():
    return obj.user_updateuser(request.form)


@app.route('/delete/<id>', methods=["DELETE"])
def user_deleteuser(id):
    return obj.user_deleteuser(id)