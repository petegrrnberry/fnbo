from django.contrib import admin
from .models import Login

class LoginAdmin(admin.ModelAdmin):
    list_display = ('id','username','password')

# Register your models here.
admin.site.register(Login,LoginAdmin)