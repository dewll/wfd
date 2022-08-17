from ninja import Schema


class RegistrationSchemaIn(Schema):
    email: str
    password: str
    phone: str = None
    account_type:str = None
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
    
class LoginSchemaOut(Schema):
    message: str
    
    
class Error(Schema):
    message: str