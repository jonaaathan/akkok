##Questions:
# After Manager create a project, the project is auto started?
# After a project is started, the phases is auto started?
# After a phases is started, the iteration is auto started?
# #
from django.db import models
from datetime import datetime


# class ProjectIterface():
# 	def create_project(self, manager, project_name):
		

class Project(models.Model):
	## 1 project has 1 manager
	## 1 manager has many projects
	## use 'users.Manager' to avoid circular import issuse
	manager = models.ForeignKey('users.Manager') 
	name = models.CharField(max_length = 100)
	start_date = models.DateTimeField(null = True, blank = True)
	end_date = models.DateTimeField(null = True, blank = True)
	active = models.BooleanField(default=False)
	curr_phase = models.IntegerField(default=0)

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
			p.stop(request_manager)
		self.save()
		return True

	def get_current_phase_str(self): ## tested
		p = self.get_current_phase()
		if not p:
			return "The project doesnt has any phase"
		return str(p)
		

	def get_current_phase(self): ## tested
		current_phase = self.phase_set.filter(phase_type = self.curr_phase)
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

	def next_phase(self): ## tested
		next_phase =  self.curr_phase + 1
		if next_phase <= 4:
			return next_phase
		else:
			return None

	def switch_phase(self, request_manager, phase_type):
		if request_manager != self.manager:
			return False
		## stop all other active phase
		phases = self.phase_set.filter(active = True)
		for p in phases:
			p.stop(request_manager)
		## get the object
		phase = self.phase_set.filter(phase_type = phase_type)
		if not phase:
			return False
		if phase[0].start(request_manager):
			self.curr_phase = phase_type
			self.save()
			return True
		else:
			return False


class Phase(models.Model):
	PHASE_OPTIONS = ['Inception', 'Elaboration', 'Construction', 'Transition']
	phase_type = models.IntegerField()
	## 1 phase has 1 project
	## 1 project has many(max 4) phase
	project = models.ForeignKey(Project)
	## But project has only one active phase
	active = models.BooleanField(default= False)
	curr_iteration = models.IntegerField(default = 0)
	def __str__(self):
		return Phase.PHASE_OPTIONS[self.phase_type-1]

	def get_status(self): #tested
		return self.active

	def start(self, request_manager): ## tested
		if self.project.manager != request_manager:
			return False
		self.active = True
		self.save()
		return True

	def stop(self, request_manager): ## tested
		if self.project.manager != request_manager:
			return False
		self.active = False
		self.save()
		return True

	def create_iteration(self, request_manager, iteration_number):
		if self.project.manager != request_manager:
			return False
		## check repeat
		if iteration_number in [i.iteration_number for i in self.iteration_set.all()]:
			return False
		## create
		iteration = Iteration(iteration_number = iteration_number)
		iteration.phase = self
		iteration.save()
		return True

	def switch_iteration(self, request_manager, iteration_number):
		if self.project.manager != request_manager:
			return False
		## stop all other active iteration
		iterations = self.iteration_set.filter(active = True)
		for i in iterations:
			i.stop(request_manager)
		## get the object
		iteration = self.iteration_set.filter(iteration_number = iteration_number)

		if not iteration:
			return False
		if iteration[0].start(request_manager):
			self.curr_iteration = iteration_number
			self.save()
			return True	
		else:
			return False

	def next_iteration(self):
		lst =[i.iteration_number for i in self.iteration_set.all()]
		if not lst:
			return 1
		return max(lst) + 1

	def get_current_iteration(self): ## tested
		current_iteration = self.iteration_set.filter(iteration_number = self.curr_iteration)
		if not current_iteration: ## empty list
			return None
		return current_iteration[0]

	def get_current_iteration_str(self): ## tested
		i = self.get_current_iteration()
		if not i:
			return "The pharse doesnt has any iteration"
		return str(i)

class Iteration(models.Model):
	iteration_number = models.IntegerField()
	## 1 iteration has 1 phase
	## 1 phase has many iteration
	phase = models.ForeignKey(Phase)
	## But phase has only one active iteration
	active = models.BooleanField(default = False)
	def __str__(self):
		return str(self.phase) + "-" + str(self.iteration_number)
	
	def start(self, request_manager):
		if request_manager != self.phase.project.manager:
			return False
		self.active = True
		self.save()
		return True
	
	def stop(self, request_manager):
		if request_manager != self.phase.project.manager:
			return False
		self.active = False
		self.save()
		return True

class Timer(models.Model):
	## Many to Many: Developers to Projects
	developer = models.ForeignKey('users.Developer')
	iteration = models.ForeignKey(Iteration)
	active = models.BooleanField(default = False)