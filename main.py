import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app,db  # Definitions initialization
from flask import Flask, request, jsonify
from flask_cors import CORS

# setup APIs
from api.database import login_api
# Initialize the SQLAlchemy object to work with the Flask app instance
db.init_app(app)

app.register_blueprint(login_api)

# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="127.0.0.1", port="8000")