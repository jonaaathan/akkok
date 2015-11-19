from django.contrib import admin
from users.models import Manager, Developer

# Register your models here.
admin.site.register(Manager)
admin.site.register(Developer)