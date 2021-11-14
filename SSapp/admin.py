
from django.contrib import admin
from .models import criminfo, usrinfo, User,crtinfo    
from .models import Contact,Contact2
from .models import Todo


admin.site.register(Todo)
admin.site.register(User)


@admin.register(Contact2)
class Contact2Disp(admin.ModelAdmin):
    list_display = ('id','name','email','phone','desc','date')

@admin.register(Contact)
class ContactDisp(admin.ModelAdmin):
    list_display = ('id','name','email','phone','desc','date')

@admin.register(usrinfo)
class UserDisp(admin.ModelAdmin):
    list_display = ('id', 'full_Name', 'city', 'address', 'phone', 'email')

@admin.register(criminfo)
class CrimDisp(admin.ModelAdmin):
    list_display = ('id', 'hospital_Name', 'city', 'address', 'phone', 'email', 'no_of_cases', 'desc1', 'desc2')#'username')

@admin.register(crtinfo)
class CrtDisp(admin.ModelAdmin):
    list_display = ('id', 'full_Name', 'city','address' ,'phone', 'email')

