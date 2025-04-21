# auth/decorators.py

from flask import g
from functools import wraps
from flask import request, jsonify
from auth.token_utils import verify_token

def auth_verfication(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_header = request.headers.get("Authorization", None)

        if not auth_header:
            return jsonify({"error": "Authorization header missing"}), 401

        token_parts = auth_header.split()

        if token_parts[0].lower() != "bearer" or len(token_parts) != 2:
            return jsonify({"error": "Invalid authorization header"}), 401

        token = token_parts[1]
        verification = verify_token(token)

        if isinstance(verification, tuple): 
            return jsonify(verification[0]), verification[1]
        
        g.current_user = verification

        return f(*args, **kwargs)

    return decorator