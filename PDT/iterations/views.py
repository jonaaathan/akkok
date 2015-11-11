from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from iterations.models import Iteration
# Create your views here.
def index(request):
	iterations = Iteration.objects.all()
	context = {'iterations' : iterations}
	return render(request, 'index.html',context) # iterations list

def new(request):
	return render(request, 'new.html') # iterations list

def create(request):
	iteration = Iteration(name=request.POST['name'])
	iteration.save()
	return redirect('iterations:index')

def detail(request, iteration_id):
    return HttpResponse("You're looking at iteration %s." % iteration_id)

def start(request, iteration_id):
    return HttpResponse("You're Starting on iteration %s." % iteration_id)

def pause(request, iteration_id):
    return HttpResponse("You're Pausing on iteration %s." % iteration_id)

def end(request, iteration_id):
    return HttpResponse("You're Ending on iteration %s." % iteration_id)