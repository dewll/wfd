from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, StationRequest, ApprovedStation
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name',
                    'email','phone','password')
     
    
admin.site.register(User)
admin.site.register(StationRequest)
admin.site.register(ApprovedStation)