from django.db import models
from projects.models import Project, Iteration

# Abstract User Class
class User(models.Model):
	name = models.CharField(max_length=100)
	staff_id = models.IntegerField(unique = True)
	password = models.CharField(max_length=100)
	class Meta:
		abstract = True

# Actual Manager Class
class Manager(User):
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


class Developer(User):
	def add_iteration(self, i):
		self.iteration_set.add(i)

	def get_iterations(self):
		return self.iteration_set

	def get_num_iterations(self):
		return self.iteration_set.count()


