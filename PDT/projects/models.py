##Questions:
# After Manager create a project, the project is auto started?
# After a project is started, the phases is auto started?
# After a phases is started, the iteration is auto started?
# #
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

		## disable all active phase
		ps = self.phase_set.filter(active = True)
		for p in ps:
			p.stop()
		self.save()
		return True

	def get_current_phase_str(self): ## tested
		p = self.get_current_phase(request_manager).phase_type
		if p == 0:
			return None
		return Phase.PHASE_OPTIONS[p-1]

	def get_current_phase(self, request_manager): ## tested
		current_phase = self.phase_set.filter(active = True)
		if not current_phase: ## empty list
			return None
		return current_phase[0]

	def next_phase(self, request_manager): ## tested
		if not self.active:
			print("Project Stop")
			return
		curr_phase = self.get_current_phase(request_manager)
		if curr_phase == None:
			next_phase = 1
		else:
			next_phase =  curr_phase.phase_type + 1
			## disable prev phase
			curr_phase.stop()
		
		print(next_phase)
		
		if next_phase <= 4:
			p = Phase(phase_type = next_phase)
			p.project = self
			p.active = True ## auto start
			p.save()
		else:
			self.active = False
			print('project ends')


class Phase(models.Model):
	PHASE_OPTIONS = ['Inception', 'Elaboration', 'Construction', 'Transition']
	phase_type = models.IntegerField()
	## 1 phase has 1 project
	## 1 project has many(max 4) phase
	project = models.ForeignKey(Project)
	## But project has only one active phase
	active = models.BooleanField(default= False)

	def start(self): ## tested
		self.active = True
		self.save()

	def stop(self): ## tested
		self.active = False
		self.save()


class Iteration(models.Model):
	iteration_number = models.IntegerField()
	## 1 iteration has 1 phase
	## 1 phase has many iteration
	phase = models.ForeignKey(Phase)
	## But phase has only one active iteration
	active = models.BooleanField(default = False)

class Iterations_Developers(models.Model):
	## Many to Many: Developers to Projects
	developer = models.ForeignKey('users.Developer')
	iteration = models.ForeignKey(Iteration)
	active = models.BooleanField(default = False)