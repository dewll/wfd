from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length = 20, unique=False, blank=True, null = True)
    first_name = models.CharField(max_length = 20,null = True, blank=True)
    last_name = models.CharField(max_length = 20,null = True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length = 20,null = True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
class SuperAdmin(User):
    TYPE1 = 'T1'
    TYPE2 = 'T2'
    CHOICE_FIELD = [
        (TYPE1,'ADMIN1'),
        (TYPE2,'ADMIN2'),
    ]
    role = models.CharField(max_length=50, choices = CHOICE_FIELD, default = TYPE1, )
    
    class Meta:
        db_table = "SuperAdmin"
        
    def __str__(self):
        return self.email
    
class StationManager(User):
    station_name = models.CharField(max_length = 20)
    fullname = models.CharField(max_length = 100)
    location = models.CharField(max_length = 150)
    state = models.CharField(max_length = 150)
    business_reg_num = models.IntegerField()
    
    class Meta:
        db_table = "StationManager"
        
    def __str__(self):
        return self.email
