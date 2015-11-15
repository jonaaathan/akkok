from django.db import models



class Project(models.Model):
	name = models.CharField(max_length = 100)
	start_date = models.DateTimeField(null = True, blank = True)
	end_date = models.DateTimeField(null = True, blank = True)

class Pharse(models.Model):
	pharse_type = models.CharField(max_length = 100)
	## 1 pharse has 1 project
	## 1 project has many pharse
	project = models.ForeignKey(Project)
	## But project has only one active pharse
	active = models.BooleanField(default= False)

class Iteration(models.Model):
	iteration_number = models.IntegerField()
	## 1 iteration has 1 pharse
	## 1 pharse has many iteration
	pharse = models.ForeignKey(Pharse)
	## But pharse has only one active iteration
	active = models.BooleanField(default = False)
