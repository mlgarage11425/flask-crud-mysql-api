import mysql.connector
import json

class user_model():

    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user="root",password="Omkar@777777",database="rest_api")
            self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)
            print("connection successfull")
        except:
            print("Db is not connected successfully")


    def user_signup_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data found"
        

    def add_user(self, data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")

        return "User created successfully"

    def user_updateuser(self,data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE id={data['id']}")

        #print("Updating user with ID:", data['id'])
        #print("Data received:", data)

        if self.cur.rowcount>0:
            return "user updated successfully"
        else:
            return "failed to update"

