from django.contrib import admin

# Register your models here.
from login.models import UserProfile
class UserProfileAdmin (admin.ModelAdmin):
    list_display=('user','role')

admin.site.register(UserProfile,UserProfileAdmin)