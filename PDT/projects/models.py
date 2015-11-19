##Questions:
# After Manager create a project, the project is auto started?
# After a project is started, the phases is auto started?
# After a phases is started, the iteration is auto started?
# #
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
class Project(models.Model):
	## 1 project has 1 manager
	## 1 manager has many projects
	## use 'users.Manager' to avoid circular import issuse
	manager = models.ForeignKey(User) 
	name = models.CharField(max_length = 100)
	start_date = models.DateTimeField(null = True, blank = True)
	end_date = models.DateTimeField(null = True, blank = True)
	active = models.BooleanField(default=False)
	curr_phase = models.IntegerField(default=0)

	def __str__(self):
		return self.name

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

		## disable all active phase
		ps = self.phase_set.filter(active = True)
		for p in ps:
			p.stop(self)
		self.save()
		return True

	def get_current_phase_str(self): ## tested
		p = self.curr_phase
		if p == 0:
			return "The project doesnt has any phase"
		return Phase.PHASE_OPTIONS[p-1]

	def get_current_phase(self): ## tested
		current_phase = self.phase_set.filter(phase_type = 1)
		if not current_phase: ## empty list
			return None
		return current_phase[0]

	def create_phase(self, request_manager, phase_type): ## tested
		if request_manager != self.manager:
			return False
		## check for repeat phase type
		phase_types_lst = [p.phase_type for p in self.phase_set.all()]
		if phase_type in phase_types_lst :
			return False
		## create phase
		p = Phase(phase_type = phase_type)
		p.project = self
		p.save()
		return True

	def next_phase(self, request_manager): ## tested
		if request_manager != self.manager:
			return None
		if not self.active:
			return None
		## get next phase type
		next_phase =  self.curr_phase + 1

		if next_phase <= 4:

			return next_phase
		else:
			self.active = False
			return None

	def start_phase(self, request_manager, phase_type):
		if request_manager != self.manager:
			return False
		## stop all other phase
		if self.phase_set.count():
			phases = self.phase_set.all()
			for p in phases:
				p.stop(self)
		## get the object
		phase = self.phase_set.filter(phase_type = phase_type)
		if not phase:
			return False
		if phase[0].start(self):
			self.curr_phase = phase_type
			return True



class Phase(models.Model):
	PHASE_OPTIONS = ['Inception', 'Elaboration', 'Construction', 'Transition']
	phase_type = models.IntegerField()
	## 1 phase has 1 project
	## 1 project has many(max 4) phase
	project = models.ForeignKey(Project)
	## But project has only one active phase
	active = models.BooleanField(default= False)

	def __str__(self):
		return self.phase_type

	def get_status(self): #tested
		return self.active

	def start(self, request_project): ## tested
		if request_project != self.project:
			return False
		self.active = True
		self.save()
		return True

	def stop(self, request_project): ## tested
		if request_project != self.project:
			return False
		self.active = False
		self.save()
		return True


class Iteration(models.Model):
	iteration_number = models.IntegerField()
	## 1 iteration has 1 phase
	## 1 phase has many iteration
	phase = models.ForeignKey(Phase)
	## But phase has only one active iteration
	active = models.BooleanField(default = False)

	def __str__(self):
		return self.iteration_number

class Iterations_Developers(models.Model):
	## Many to Many: Developers to Projects
	developer = models.ForeignKey(User)
	iteration = models.ForeignKey(Iteration)
	active = models.BooleanField(default = False)

	def __str__(self):
		return self.developer