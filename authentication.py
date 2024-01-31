from functools import wraps
import jwt
from flask import request, abort, current_app
from model.logins import *
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Extract the JWT token from the request headers
        print(request.cookies.get("jwt"))
        token = request.cookies.get("jwt")
        if token is None or False:
            abort(401, "Authentication token is missing")
        return f(*args, **kwargs)

    return decorated
