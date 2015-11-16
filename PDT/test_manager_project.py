import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PDT.settings")
django.setup()

from users.models import User, Manager

## main success
nxt_m_id = Manager.objects.count()+1
## reg

## login


m = Manager(staff_id=nxt_m_id, password="1234", name="1234")
m.save()

project_id = m.create_project("Demo Project")
project = m.get_project_by_id(project_id)
if m.start_project(project):
	print("The project is started")

for i in range(5):
	## get next phase of the project
	nxt = project.next_phase()
	if nxt:
		print("The nxt phase is: " + str(nxt))
		## get create a new phase
		if project.create_phase(m, nxt):
			print("new phase created")
		else:
			print("cannot create new phase")
		## switch to the new phase
		if project.switch_phase(m, nxt):
			print("current active phase: " + str(len(project.phase_set.filter(active=True))))
			print("the phase is switched to: "+ project.get_current_phase_str())
			for j in range(5):
				phase = project.get_current_phase()
				nxt_t = phase.next_iteration()
				if phase.create_iteration(m, nxt_t):
					print("\tnew iteration created")
					if phase.switch_iteration(m, nxt_t):
						print("\tthe phase is switched to: "+project.get_current_phase().get_current_iteration_str())
						print("\tcurrent active iteration: " + str(len(project.get_current_phase().iteration_set.filter(active=True))))
			
				else:
					print("cannot create new iteration")
	else:
		print("Cannot go nxt phase")

if not project.get_status:
	print("The project is finished")


## project edited by other Manager
print("")

nxt_m_id = Manager.objects.count()+1
m = Manager(staff_id=nxt_m_id, password="1234", name="1234")
m.save()
if m.start_project(project):
	print("The project is started")
else:
	print("The project cannot be started by other Manager")