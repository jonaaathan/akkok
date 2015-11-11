from django.db import models
from datetime import timedelta
# Create your models here.
class Iteration(models.Model):
	# Enums
	PAUSE = "P"
	RUNNING = "R"
	END = "E"
	iteration_states = (
		(PAUSE, 'Paused'),
		(RUNNING, 'Running'),
		(END, 'END'),
		)
	# Models
	name = models.CharField(max_length=100)
	running = models.CharField(max_length=1, choices=iteration_states, default=PAUSE)
	create_date = models.DateTimeField(auto_now_add=True)
	total_duration = models.DurationField(default=timedelta(seconds=0))	