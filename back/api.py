from ninja_extra import NinjaExtraAPI, api_controller, http_get,http_post
from django.contrib.auth import authenticate
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .import models
from .import schemas
from .import authorization



@api_controller('/',tags=["WFD"])
class Station:
    @http_get('/home', auth=authorization.AuthBearer())
    def Home(self,request):
        return{'message': request.auth}
    
    @http_post('/users',response={201: schemas.RegistrationSchemaOut,400: schemas.Error})
    def registration (self,request,payload: schemas.RegistrationSchemaIn):
        data = payload.dict()
        email = data['email']
        password = data['password']
        phone = data["phone"]
        station_name = data["station_name"]
        fullname = data["fullname"]
        location = data["location"]
        state = data["state"]
        business_reg_num = data["reg_num"]
        associated_users = models.User.objects.filter(email=email)
        if associated_users:
            return 400, {"message":"User with the email already exist"}
        else:
            if business_reg_num:
                station_request_exist = models.StationRequest.objects.filter(email=email)
                if station_request_exist:
                    return 400, {"message":"User with the email already exist"}
                try:
                    user = models.StationRequest.objects.create(email=email, phone = phone, 
                                                                station_name=station_name,
                                                                fullname=fullname,location=location,state=state,
                                                                business_reg_num=business_reg_num)
                    return 201, {"message":"Form submitted Successfully"}
                except:
                    return 400, {"message":"Something went wrong"}
            else:
                try:
                    user = models.User.objects.create(email=email, password=password)
                    user.set_password(password)
                    user.save()
                    return 201, {"message":"Registration Successfull"}
                except:
                    return 400, {"message":"Something went wrong"}
                
    @http_post('/signin', url_name="signin",response={200: schemas.TokenSchema,400: schemas.Error})
    def signin(self,request,payload: schemas.LoginSchemaIn):
        data = payload.dict()
        email = data['email']
        password = data['password']
        if email is None:
            return 400, {"message":"please enter email"}
        if password is None:
            return 400, {"message":"please enter password"}
        user = authenticate(email=email, password=password)
        #and all(user.approved_station.exist() or user.is_admin)
        if user is not None and  (user.approved_station.exists() or user.user_type == '0'):
            access = authorization.create_token(email)
            return 200, {'access':access}
        return 400, {"message": "Invalid email or password"}
    
    @http_get('/reset_password/{uidb64}/{token}', url_name="password_reset")
    def password_reset(self,request,uidb64,token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = models.User.objects.get(pk=uid)
        except(TypeError, ValueError):
            user = None
        if user is not None and default_token_generator.check_token(user,token):
            print("You are about to reset Your password")
    


api = NinjaExtraAPI()
api.register_controllers(Station)