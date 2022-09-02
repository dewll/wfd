from django.db import models
from django.contrib.auth.models import AbstractUser
from . import send_approval_mail

# Create your models here.

class User(AbstractUser):
    SUPER_ADMIN = '0'
    STATION_MANAGER = '1'
    USER_TYPE =[
         (SUPER_ADMIN,'SUPER_ADMIN'),
         (STATION_MANAGER,'STATION_MANAGER'),
    ]
    username = models.CharField(max_length = 20, unique=False, blank=True, null = True)
    first_name = models.CharField(max_length = 20,null = True, blank=True)
    last_name = models.CharField(max_length = 20,null = True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length = 20,null = True, blank=True)
    user_type = models.CharField(max_length=50, choices = USER_TYPE, default = SUPER_ADMIN, )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email

    
class StationRequest(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length = 20)
    station_name = models.CharField(max_length = 100)
    fullname = models.CharField(max_length = 100)
    location = models.CharField(max_length = 150)
    state = models.CharField(max_length = 150)
    business_reg_num = models.IntegerField()
    is_approved = models.BooleanField(default=False)
    
    def save(self, *args,**kwargs):
        associated_users = ApprovedStation.objects.filter(email=self.email)
        if self.is_approved == True:
            if associated_users:
                pass
            else:
                email = self.email
                phone = self.phone
                station_name = self.station_name
                fullname = self.fullname
                location = self.location
                state = self.state
                business_reg_num = self.business_reg_num
                station_manager = User.objects.create(email=email,password =email,user_type ='1')
                station_manager.set_password(email)
                station_manager.save()
                approve(email,phone,station_name,
                        fullname,location,state,
                        business_reg_num,station_manager)
        super().save(*args,**kwargs)
    
    class Meta:
        db_table = "StationRequest"
        
    def __str__(self):
        return self.email
    
    
class ApprovedStation(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length = 20)
    station_name = models.CharField(max_length = 20)
    fullname = models.CharField(max_length = 100)
    location = models.CharField(max_length = 150)
    state = models.CharField(max_length = 150)
    business_reg_num = models.IntegerField()
    station_manager = models.ForeignKey(User, related_name = "approved_station",
                                        on_delete = models.CASCADE, null = False)
    
    class Meta:
        db_table = "ApprovedStation"
    
    def __str__(self):
        return self.email
    
def approve(email,phone,station_name,fullname,location,state,business_reg_num,station_manager):
    ApprovedStation.objects.create(email=email,phone=phone,
                                station_name=station_name,
                                fullname=fullname,location=location,
                                state=state,business_reg_num=business_reg_num,
                                station_manager=station_manager)
    #send_approval_mail.send_mail(email,fullname)
