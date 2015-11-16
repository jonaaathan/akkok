import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PDT.settings")
django.setup()

from users.models import Manager

## main success
nxt_m_id = Manager.objects.count()+1
m = Manager(staff_id=nxt_m_id, password="1234", name="1234")
m.save()

project_id = m.create_project("Demo Project")
project = m.get_project_by_id(project_id)
if m.start_project(project):
	print("The project is started")

for i in range(5):	
	nxt = m.project_next_phase(project)
	if nxt:
		print("The current phase is: " + project.get_current_phase_str())
		print("The nxt phase is: " + str(nxt))
		if m.project_create_phase(project, nxt):
			print("new phase created")
		else:
			print("cannot create new phase")
		if m.project_start_phase(project, nxt):
			print("the phase is started")
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