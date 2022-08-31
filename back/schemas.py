from ninja import Schema


class TokenSchema(Schema):
    access: str

class RegistrationSchemaIn(Schema):
    email: str
    password: str =None
    username: str =None
    phone: str = None
    station_name:str = None
    fullname:str = None
    location:str = None
    state:str = None
    reg_num:int = None
    
    
class RegistrationSchemaOut(Schema):
    message: str
    
class LoginSchemaIn(Schema):
    email: str
    password: str
    
    
class Error(Schema):
    message: str