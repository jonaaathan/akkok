from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from users.models import UserProfile

class ProfileInline(admin.StackedInline):
	model =  UserProfile
	can_delete = False
	verbose_name_plural = 'profile'

class  UserAdmin(UserAdmin):
	inlines = (ProfileInline, )
# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

#admin.site.register(Manager)
#admin.site.register(Developer)