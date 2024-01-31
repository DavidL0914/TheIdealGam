import sqlite3
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api
from werkzeug.security import generate_password_hash, check_password_hash
from model.logins import *
import jwt
from authentication import token_required
from flask import current_app

# specify the  path to the database file
db_file_path = 'example.db'
print(db_file_path)
# connect to the db
login_api = Blueprint("login_api", __name__, url_prefix="/api/login")
api = Api(login_api)

conn = sqlite3.connect(db_file_path, check_same_thread=False)
cursor = conn.cursor()

class UserDeletion(Resource):
    def delete(self, username):
        conn = sqlite3.connect(db_file_path, check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()
        if not existing_user:
            conn.close()
        cursor.execute('DELETE FROM users WHERE username = ?', (username,))
        conn.commit()
        conn.close()
class UserRegistration(Resource):
    def post(self):
        conn = sqlite3.connect(db_file_path, check_same_thread=False)
        cursor = conn.cursor()
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return make_response(jsonify(error='Username and password are required'), 400)

        # Connect to the database


        # Check if the username is already taken
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            return make_response(jsonify(error='Username is already taken'), 409)
        # Encrypts the password, and stores it in the database
        hashed_password = generate_password_hash(password)
        cursor.execute('''INSERT INTO users (username, password) VALUES(?, ?)''', (username, hashed_password))
        conn.commit()
        conn.close()
        user_data = {"username": username}
        token = jwt.encode(user_data, current_app.config["SECRET_KEY"], algorithm="HS256")

        return make_response(jsonify(message='Registration successful', token=token), 201)
    
    class Visualize(Resource):   
        @token_required 
        def get(self):
            data = visualize_users_data()
            print(data)
            print("hello")
            return jsonify({'users_data': data})
class UserCheck(Resource):
    def get(self, username):
        conn = sqlite3.connect(db_file_path, check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()
        conn.close()

        if existing_user:
            return jsonify({"exists": True})
        else:
            return jsonify({"exists": False})
class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return make_response(jsonify(error='Username and password are required'), 400)

        conn = sqlite3.connect(db_file_path, check_same_thread=False)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()
        if user and check_password_hash(user[1], password):  # Assuming hashed password is at index 2
            user_data = {"username": username}
            token = jwt.encode(user_data, current_app.config["SECRET_KEY"], algorithm="HS256")
            return make_response(jsonify(message='Login successful', token=token), 200)
        else:
            return make_response(jsonify(error='Invalid username or password'), 401)

# Add resource to blueprint
api.add_resource(UserLogin, '/login')
api.add_resource(UserRegistration.Visualize, '/vis')
api.add_resource(UserRegistration, '/register')
api.add_resource(UserDeletion, '/delete/<string:username>')
api.add_resource(UserCheck, '/checkuser/<string:username>')