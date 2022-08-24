from ninja_extra import NinjaExtraAPI, api_controller, http_get,http_post
from django.contrib.auth import authenticate
from .import models
from .import schemas
from .import authorization


@api_controller('/',tags=["WFD"])
class Station:
    @http_get('/home', auth=authorization.AuthBearer())
    def Home(self,request):
        return{'message':request.auth}
    
    @http_post('/users',response={201: schemas.RegistrationSchemaOut,400: schemas.Error})
    def registration (self, payload: schemas.RegistrationSchemaIn):
        data = payload.dict()
        email = data['email']
        password = data['password']
        phone = data["phone"]
        account_type = data["account_type"]
        station_name = data["station_name"]
        fullname = data["fullname"]
        location = data["location"]
        state = data["state"]
        business_reg_num = data["reg_num"]
        associated_users = models.User.objects.filter(email=email)
        if associated_users:
            return 400, {"message":"User with the email already exist"}
        else:
            if account_type:
                user = models.SuperAdmin.objects.create(email=email, password=password, role = account_type)
                user.set_password(password)
                user.save()
                return 201, {"message":"Registration Successfull for SuperAdmin"}
            elif business_reg_num:
                station_exist = models.StationManager.objects.filter(email=email)
                if station_exist:
                    return 400, {"message":"User with the email already exist"}
                user = models.StationManager.objects.create(email=email, phone = phone, 
                                                            station_name=station_name,
                                                            fullname=fullname,location=location,state=state,
                                                            business_reg_num=business_reg_num)
                
                return 201, {"message":"Registration Successfull for Station Manager"}
            else:
                user = models.User.objects.create(email=email, password=password)
                user.set_password(password)
                user.save()
                return 201, {"message":"Registration Successfull"}

    @http_post('/signin',response={200: schemas.TokenSchema,400: schemas.Error})
    def signin(self, payload: schemas.LoginSchemaIn):
        data = payload.dict()
        email = data['email']
        password = data['password']
        if email is None:
            return 400, {"message":"please enter username"}
        if password is None:
            return 400, {"message":"please enter password"}
        user = authenticate(email=email, password=password)
        if user is not None:
            access = authorization.create_token(email)
            return 200, {'access':access}
        return 400, {"message": "Invalid email or password"}
    


api = NinjaExtraAPI()
api.register_controllers(Station)