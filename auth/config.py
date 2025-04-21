# auth/config.py

import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

COGNITO_REGION = os.getenv("COGNITO_REGION")
COGNITO_USER_POOL_ID = os.getenv("COGNITO_USER_POOL_ID")
COGNITO_CLIENT_ID = os.getenv("COGNITO_CLIENT_ID")
COGNITO_DOMAIN = os.getenv("COGNITO_DOMAIN")

# URL del issuer (usado para verificar tokens)
COGNITO_ISSUER = f"https://cognito-idp.{COGNITO_REGION}.amazonaws.com/{COGNITO_USER_POOL_ID}"

# JWKS URL para obtener las claves públicas de verificación
JWKS_URL = f"{COGNITO_ISSUER}/.well-known/jwks.json"
