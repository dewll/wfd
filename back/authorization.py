from ninja.security import HttpBearer
from django.conf import settings
import datetime
from datetime import timedelta
import jwt


class AuthBearer(HttpBearer):
    
    '''defining call method to manually call authenticate method during testing
        due to the authenticate method not been called during testing but on
        production we don't need the call method.
    '''
    # def __call__(self, request):
    #     auth_value = request.META['headers']['HTTP_AUTHORIZATION']
    #     parts = auth_value.split(" ")
    #     token = " ".join(parts[1:])
    #     return self.authenticate(request, token)
    
    def authenticate(self,  request, token):
        try:
            #JWT secret key is set up in settings.py
            JWT_SIGNING_KEY = getattr(settings, "SIGNING_KEY", None)
            payload = jwt.decode(token, JWT_SIGNING_KEY, algorithms=["HS256"])
            email: str = payload.get("sub")
            if email is None:
                return None
        except jwt.PyJWTError as e:
            return None
        return email
 

def create_token(email):
    JWT_SIGNING_KEY = getattr(settings, "SIGNING_KEY", None)
    JWT_ACCESS_EXPIRY = getattr(settings, "ACCESS_TOKEN_LIFETIME", 15)
    to_encode_access = {"sub": email}
    access_expire = datetime.datetime.utcnow() + timedelta(minutes=JWT_ACCESS_EXPIRY)
    to_encode_access.update({"exp": access_expire})
    encoded_access_jwt = jwt.encode(to_encode_access, JWT_SIGNING_KEY, algorithm="HS256")
    return encoded_access_jwt
