from django.contrib import admin
from .models import customer,UserProfileInfo
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(customer)
