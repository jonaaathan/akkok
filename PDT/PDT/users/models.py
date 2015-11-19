from django.db import models
from projects.models import Project, Iteration
from django.contrib.auth.models import User

# Abstract User Class
class UserProfile(models.Model):
	staff_id = models.IntegerField(unique = True)
	#user = models.OneToOneField(User)#, default=-1)
	user = models.ForeignKey(User, null=True)#, default=-1)
	#name = models.CharField(max_length=100)
	#password = models.CharField(max_length=100)

	def __str__(self):
		return self.user.username

	class Meta:
		abstract = True

# Actual Manager Class
class Manager(UserProfile):
	def __str__(self):
		return self.username
	def get_project_by_id(self, p_id): #tested
		try:
			return self.project_set.get(id=p_id)
		except Project.DoesNotExist:
			return None

	def add_project(self, p): #tested
		p.manager = self
		## edit a model object outside itself need use save()
		p.save()
		return p.id

	def create_project(self, project_name): #tested
		project = Project(name=project_name)
		return self.add_project(project)

	def start_project(self, project): #tested
		return project.start(self)
	
	def stop_project(self, project): #tested
		return project.stop(self)

	def project_create_phase(self, project, phase_type): ## tested
		return project.create_phase(self, phase_type)

	def project_next_phase(self, project): #tested
		return project.next_phase(self)

	def project_start_phase(self, project, phase_type):
		return project.start_phase(self, phase_type)
	
class Developer(UserProfile):
	def add_iteration(self, i):
		self.iteration_set.add(i)

	def get_iterations(self):
		return self.iteration_set

	def get_num_iterations(self):
		return self.iteration_set.count()
