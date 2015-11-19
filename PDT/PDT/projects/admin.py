from django.contrib import admin
from projects.models import Project, Phase, Iteration

# Register your models here.
admin.site.register(Project)
admin.site.register(Phase)
admin.site.register(Iteration)