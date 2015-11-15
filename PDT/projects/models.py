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
		self.save()
		return True
	
	def stop(self, request_manager): #tested
		## not your project!
		if request_manager != self.manager:
			return False
		self.active = False
		self.end_date = datetime.now()

		## disable all active phrase
		ps = self.phrase_set.filter(active = True)
		for p in ps:
			p.stop()
		self.save()
		return True

	def get_current_phrase_str(self): ## tested
		p = self.get_current_phrase(request_manager).phrase_type
		if p == 0:
			return None
		return Phrase.PHRASE_OPTIONS[p-1]

	def get_current_phrase(self, request_manager): ## tested
		current_phrase = self.phrase_set.filter(active = True)
		if not current_phrase: ## empty list
			return None
		return current_phrase[0]

	def next_phrase(self, request_manager): ## tested
		if not self.active:
			print("Project Stop")
			return
		curr_phrase = self.get_current_phrase(request_manager)
		if curr_phrase == None:
			next_phrase = 1
		else:
			next_phrase =  curr_phrase.phrase_type + 1
			## disable prev phrase
			curr_phrase.stop()
		
		print(next_phrase)
		
		if next_phrase <= 4:
			p = Phrase(phrase_type = next_phrase)
			p.project = self
			p.active = True ## auto start
			p.save()
		else:
			self.active = False
			print('project ends')


class Phrase(models.Model):
	PHRASE_OPTIONS = ['Inception', 'Elaboration', 'Construction', 'Transition']
	phrase_type = models.IntegerField()
	## 1 phrase has 1 project
	## 1 project has many phrase
	project = models.ForeignKey(Project)
	## But project has only one active phrase
	active = models.BooleanField(default= False)

	def start(self): ## tested
		self.active = True
		self.save()

	def stop(self): ## tested
		self.active = False
		self.save()

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