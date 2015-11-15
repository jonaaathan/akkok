from django.db import models
from projects.models import Project

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=100)
	staff_id = models.IntegerField()
	password = models.CharField(max_length=100)
	project = models.ManyToManyField(Project)
	class Meta:
		abstract = True
