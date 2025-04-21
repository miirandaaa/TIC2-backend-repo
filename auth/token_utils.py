# auth/token_utils.py

import json
import time
import urllib.request
import logging
from typing import Dict, List

from jose import jwk, jwt
from jose.utils import base64url_decode
from pydantic import BaseModel

from auth.config import JWKS_URL, COGNITO_ISSUER, COGNITO_CLIENT_ID
from utils.exceptions import *

class JWK(BaseModel):
    alg: str
    e: str
    kid: str
    kty: str
    n: str
    use: str

class CognitoValidator:
    def __init__(self):
        self.jwks = self._fetch_jwks()

    # Fetches the JSON Web Key Set (JWKS) from Cognito to validate the token signature
    def _fetch_jwks(self) -> List[JWK]:
        with urllib.request.urlopen(JWKS_URL) as file:
            res = json.loads(file.read().decode("utf-8"))
            if not res.get("keys"):
                raise Exception("The JWKS endpoint does not contain any keys.")
            return [JWK(**key) for key in res["keys"]]

    # Validates the JWT token by checking its structure, signature, and claims
    def validate_token(self, token: str) -> Dict:
        self._check_structure(token)
        self._verify_signature(token)
        claims = self._verify_claims(token)
        return claims

    # Checks if the JWT structure is valid
    def _check_structure(self, token: str):
        try:
            # Check that the token has the right format (header, payload, and signature)
            jwt.get_unverified_header(token)
            jwt.get_unverified_claims(token)
        except jwt.JWTError:
            raise InvalidJWTError("Token structure is invalid.")

    # Verifies the signature of the JWT using the JWKS
    def _verify_signature(self, token: str) -> Dict:
        headers = jwt.get_unverified_header(token)
        kid = headers["kid"]

        # Find the key that matches the 'kid' (key ID)
        key = next((jwk.construct(j.dict()) for j in self.jwks if j.kid == kid), None)
        if not key:
            raise InvalidKidError(f"No matching signing key found for kid {kid}")

        # Extract the signature part from the token
        message, encoded_sig = str(token).rsplit(".", 1)
        signature = base64url_decode(encoded_sig.encode("utf-8"))

        # Verify the signature
        if not key.verify(message.encode("utf8"), signature):
            raise SignatureError("Signature verification failed.")

        return headers

    # Verifies the claims of the JWT token to ensure it is valid
    def _verify_claims(self, token: str) -> Dict:
        claims = jwt.get_unverified_claims(token)

        # Check token expiration
        if claims["exp"] < time.time():
            raise TokenExpiredError("Token has expired.")

        # Verify the issuer
        if claims["iss"] != COGNITO_ISSUER:
            raise InvalidIssuerError("Invalid issuer.")

        # Verify the client ID or audience
        if claims.get("client_id") != COGNITO_CLIENT_ID and claims.get("aud") != COGNITO_CLIENT_ID:
            raise InvalidAudienceError("Invalid audience.")

        # Verify that the token is an access token
        if claims["token_use"] != "access":
            raise InvalidTokenUseError("Token use must be 'access'.")

        return claims

# Helper function to verify the token using CognitoValidator
def verify_token(token: str) -> Dict:
    validator = CognitoValidator()
    return validator.validate_token(token)
