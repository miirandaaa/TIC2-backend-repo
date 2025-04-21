# services/user_service.py

import boto3
from botocore.exceptions import ClientError

from models.user_model import User
from utils.exceptions import *
from auth.config import COGNITO_USER_POOL_ID, COGNITO_CLIENT_ID, COGNITO_REGION


""" 
    UserService es la clase encargada de manejar la lógica de negocio relacionada con los usuarios para la parte relacionada con la base de datos.
    Esta clase contiene métodos para agregar, eliminar y actualizar usuarios en la base de datos
    y también para interactuar con AWS Cognito para la gestión de usuarios
"""

class UserService:
    def __init__(self):
        # Conexión con Cognito
        self.cognito_client = boto3.client('cognito-idp', region_name = COGNITO_REGION)  
        self.cognito_pool_id = COGNITO_USER_POOL_ID
        self.cognito_client_id = COGNITO_CLIENT_ID 

    # Metodo que verifica datos internamente para añadir un usuario
    def add_user(self, email, group):

        # Verificar si el usuario ya existe
        existing_user = User.get_by_email(email)
        if existing_user:
            raise AlreadyExistsException(f"El usuario con mail: {email} ya existe.")
        

        # Verificar si el usuario ya existe en Cognito
        try:
            self.cognito_client.admin_get_user(
                UserPoolId=self.cognito_pool_id,
                Username=email
            )
            raise AlreadyExistsException(f"El usuario con mail: {email} ya existe en Cognito.")
        except self.cognito_client.exceptions.UserNotFoundException:
            pass 

        # Crear usuario en Cognito
        temporal_password = "Password123!"
        try:
            self.cognito_client.admin_create_user(
                UserPoolId=self.cognito_pool_id,
                Username=email,
                TemporaryPassword=temporal_password,
                UserAttributes=[
                    { 'Name': 'email', 'Value': email },
                    { 'Name': 'email_verified', 'Value': 'True' }
                ],
        )
        except ClientError as e:
            raise SaveException(f"Error al registrar el usuario en Cognito: {e}")
        
        # Agregar el usuario creado a su grupo admin/user
        try:
            self.cognito_client.admin_add_user_to_group(
                UserPoolId=self.cognito_pool_id,
                Username=email,
                GroupName=group
            )
        except ClientError as e:
            raise SaveException(f"No se pudo agregar a grupo {group}: {e}")

        # Cear el usuario en la base de datos
        new_user = User(email, group)

        new_user.save()

        return new_user
    
    # Metodo que verifica datos internamente para iniciar sesion de un usuario
    def login_user(self, email, password):

        try:
            response = self.cognito_client.initiate_auth(
                ClientId=self.cognito_client_id,
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME': email,
                    'PASSWORD': password
                }
            )

            if 'ChallengeName' in response and response['ChallengeName'] == 'NEW_PASSWORD_REQUIRED':
                return {
                    "status": "NEW_PASSWORD_REQUIRED",
                    "session": response['Session']
                }
            
            return {
                "access_token": response['AuthenticationResult']['AccessToken'],
                "id_token": response['AuthenticationResult']['IdToken'],
                "refresh_token": response['AuthenticationResult']['RefreshToken']
            }

        except ClientError as e:
            raise InvalidInputException(f"Error al autenticar al usuario: {e}")
        

    def change_password(self, email, new_password, session):
        try:
            response = self.cognito_client.respond_to_auth_challenge(
                ClientId=self.cognito_client_id,
                ChallengeName='NEW_PASSWORD_REQUIRED',
                Session=session,
                ChallengeResponses={
                    'USERNAME': email,
                    'NEW_PASSWORD': new_password
                }
            )

            return {
                "access_token": response['AuthenticationResult']['AccessToken'],
                "id_token": response['AuthenticationResult']['IdToken'],
                "refresh_token": response['AuthenticationResult']['RefreshToken']
            }

        except ClientError as e:
            raise InvalidInputException(f"Error al cambiar la contraseña: {e}")