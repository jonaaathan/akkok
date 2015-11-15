from django.db import models

# Abstract User Class
class User(models.Model):
	name = models.CharField(max_length=100)
	staff_id = models.IntegerField()
	password = models.CharField(max_length=100)
	class Meta:
		abstract = True

# Actual Manager Class
class Manager(User):
	def get_projects(self):
		return self.project_set
	
class Deverloper(User):
	def get_iterations(self):
		return self.iteration_set


