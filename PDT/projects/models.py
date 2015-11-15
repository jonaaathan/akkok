from django.db import models
from datetime import datetime
class Project(models.Model):
	## 1 project has 1 manager
	## 1 manager has many projects
	## use 'users.Manager' to avoid circular import issuse
	manager = models.ForeignKey('users.Manager') 
	name = models.CharField(max_length = 100)
	start_date = models.DateTimeField(null = True, blank = True)
	end_date = models.DateTimeField(null = True, blank = True)
	active = models.BooleanField(default=False)
	## getters
	def get_status(self): #tested
		return self.active
	## operations
	def get_duration(self): #tested
		if not self.start_date or not self.end_date:
			return 0
		return self.end_date - self.start_date

	def start(self, request_manager): #tested
		## not your project!
		if request_manager != self.manager:
			return False
		self.active = True
		self.start_date = datetime.now()
		return True
	
	def stop(self, request_manager): #tested
		## not your project!
		if request_manager != self.manager:
			return False
		self.active = False
		self.end_date = datetime.now()
		return True




class Phrase(models.Model):
	phrase_type = models.CharField(max_length = 100)
	## 1 phrase has 1 project
	## 1 project has many phrase
	project = models.ForeignKey(Project)
	## But project has only one active phrase
	active = models.BooleanField(default= False)

class Iteration(models.Model):
	iteration_number = models.IntegerField()
	## 1 iteration has 1 phrase
	## 1 phrase has many iteration
	phrase = models.ForeignKey(Phrase)
	## But phrase has only one active iteration
	active = models.BooleanField(default = False)

class Iterations_Developers(models.Model):
	## Many to Many: Users to Projects
	developer = models.ForeignKey('users.Developer')
	iteration = models.ForeignKey(Iteration)
	active = models.BooleanField(default = False)